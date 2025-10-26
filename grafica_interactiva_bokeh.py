import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool, Select
from bokeh.layouts import column
from bokeh.io import curdoc
import os

# === Ruta absoluta del archivo CSV ===

csv_path = r"c:\Users\Laura\Desktop\Data Scientist\Analisis exploratorio de datos con Python\US_Accidents_March23.csv"

# === Verificación por si el archivo no se encuentra ===
if not os.path.exists(csv_path):
    raise FileNotFoundError(f"No se encontró el archivo CSV en: {csv_path}")

# === Cargar datos ===
df = pd.read_csv(csv_path, parse_dates=['Start_Time'], rows=1000000)

# === Filtrar accidentes graves ===
df_graves = df[df['Severity'] == 4].copy()

# === Agrupar por Estado y Día ===
df_graves_grouped = (
    df_graves.groupby(['State', pd.Grouper(key='Start_Time', freq='D')])
    .size()
    .reset_index(name='Grave_Accidents')
)

# === Calcular total por estado para filtrar los top 10 ===
top_states = (
    df_graves_grouped.groupby('State')['Grave_Accidents']
    .sum()
    .nlargest(10)
    .index
)

df_top = df_graves_grouped[df_graves_grouped['State'].isin(top_states)]

# === Crear fuente inicial (primer estado del top 10) ===
state_default = top_states[0]
source = ColumnDataSource(df_top[df_top['State'] == state_default])

# === Crear figura ===
p = figure(
    x_axis_type='datetime',
    title=f"Accidentes graves diarios en {state_default}",
    width=800, height=400,
    background_fill_color="#f9fafc"
)

p.line('Start_Time', 'Grave_Accidents', source=source, line_width=2, color="#0077b6")
p.circle('Start_Time', 'Grave_Accidents', source=source, size=5, color="#00b4d8", alpha=0.8)

p.xaxis.axis_label = "Fecha"
p.yaxis.axis_label = "Número de accidentes graves"

p.add_tools(HoverTool(
    tooltips=[("Fecha", "@Start_Time{%F}"), ("Accidentes", "@Grave_Accidents")],
    formatters={"@Start_Time": "datetime"}
))

# === Selector de estado ===
select = Select(title="Selecciona un estado:", value=state_default, options=list(top_states))

def update_plot(attr, old, new):
    new_state = select.value
    new_data = df_top[df_top['State'] == new_state]
    source.data = ColumnDataSource(new_data).data
    p.title.text = f"Accidentes graves diarios en {new_state}"

select.on_change('value', update_plot)

# === Layout final ===
layout = column(select, p)

# 🔹 Agregar layout al documento Bokeh
curdoc().add_root(layout)
curdoc().title = "Accidentes graves por estado"
