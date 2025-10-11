import pandas as pd
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, HoverTool, Select, RadioButtonGroup
from bokeh.plotting import figure
from bokeh.layouts import column, row
from bokeh.palettes import Category10

# === 1. Cargar tus datos ===
df = pd.read_csv('Accidentes por estado y severidad.csv', parse_dates=['Start_Time'])

# Si no tienes una columna de conteo, la creamos
if 'Accidents_Count' not in df.columns:
    df['Accidents_Count'] = 1

# === 2. Función para obtener top 10 estados ===
def get_top_states(mode='total'):
    if mode == 'total':
        top = df.groupby('State')['Accidents_Count'].sum().nlargest(10).index
    else:  # por día
        top = df.groupby('State')['Accidents_Count'].mean().nlargest(10).index
    return df[df['State'].isin(top)]

# === 3. Crear dataset inicial (modo total) ===
mode = 'total'
df_filtered = get_top_states(mode)

# === 4. Crear fuente de datos ===
source = ColumnDataSource(df_filtered)

# === 5. Configurar figura ===
p = figure(
    x_axis_type='datetime',
    width=900,
    height=500,
    title='Accidentes graves por día - Top 10 estados',
    toolbar_location='above'
)

# Añadir líneas por estado
colors = Category10[10]
for i, estado in enumerate(df_filtered['State'].unique()):
    subset = df_filtered[df_filtered['State'] == estado]
    src = ColumnDataSource(subset)
    p.line(
        'Start_Time', 'Accidents_Count',
        source=src, line_width=2, color=colors[i % 10],
        legend_label=estado
    )

# Hover (tooltip)
p.add_tools(HoverTool(
    tooltips=[
        ('Estado', '@State'),
        ('Fecha', '@Start_Time{%F}'),
        ('Accidentes graves', '@Accidents_Count')
    ],
    formatters={'@Start_Time': 'datetime'}
))

p.legend.location = 'top_left'
p.legend.click_policy = 'hide'
p.xaxis.axis_label = "Fecha"
p.yaxis.axis_label = "Número de accidentes graves"

# === 6. Control de filtro ===
filter_selector = RadioButtonGroup(labels=["Total", "Por día"], active=0)

def update_filter(attr, old, new):
    mode = 'total' if filter_selector.active == 0 else 'day'
    new_data = get_top_states(mode)
    source.data = ColumnDataSource(new_data).data
    p.title.text = f"Accidentes graves ({'totales' if mode=='total' else 'por día promedio'}) - Top 10 estados"

filter_selector.on_change('active', update_filter)

# === 7. Layout final ===
layout = column(filter_selector, p)

curdoc().add_root(layout)
curdoc().title = "Accidentes graves por estado"
