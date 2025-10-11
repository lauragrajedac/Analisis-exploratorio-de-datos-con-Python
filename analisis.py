# Proyecto: Análisis de Accidentes en EE.UU.

# 1. Cargar librerías
import pandas as pd
import numpy as np
from bokeh.layouts import row
from bokeh.models import CustomJSTickFormatter, Label
from bokeh.palettes import DarkText, Vibrant3 as colors
from bokeh.plotting import figure, show
from bokeh.sampledata.titanic import data as df
## 2. Cargar y explorar los datos
df = pd.read_csv(r'C:\Users\Laura\Desktop\Data Scientist\Analisis exploratorio de datos con Python\US_Accidents_March23.csv') #---, nrows=100000

print(df.head())
# print(df.columns) ----Index(['ID', 'Source', 'Severity', 'Start_Time', 'End_Time', 'Start_Lat',     
#        'Start_Lng', 'End_Lat', 'End_Lng', 'Distance(mi)', 'Description',      
#        'Street', 'City', 'County', 'State', 'Zipcode', 'Country', 'Timezone', 
#        'Airport_Code', 'Weather_Timestamp', 'Temperature(F)', 'Wind_Chill(F)',
#        'Humidity(%)', 'Pressure(in)', 'Visibility(mi)', 'Wind_Direction',     
#        'Wind_Speed(mph)', 'Precipitation(in)', 'Weather_Condition', 'Amenity',
#        'Bump', 'Crossing', 'Give_Way', 'Junction', 'No_Exit', 'Railway',
#        'Roundabout', 'Station', 'Stop', 'Traffic_Calming', 'Traffic_Signal',
#        'Turning_Loop', 'Sunrise_Sunset', 'Civil_Twilight', 'Nautical_Twilight',
#        'Astronomical_Twilight'],
#       dtype='object')
# print(df.info())------>

#  #   Column                 Non-Null Count   Dtype  
# ---  ------                 --------------   -----  
#  0   ID                     100000 non-null  object
#  1   Source                 100000 non-null  object
#  2   Severity               100000 non-null  int64
#  3   Start_Time             100000 non-null  object
#  4   End_Time               100000 non-null  object
#  5   Start_Lat              100000 non-null  float64
#  6   Start_Lng              100000 non-null  float64
#  7   End_Lat                0 non-null       float64
#  8   End_Lng                0 non-null       float64
#  9   Distance(mi)           100000 non-null  float64
#  10  Description            100000 non-null  object
#  11  Street                 100000 non-null  object
#  12  City                   99999 non-null   object
#  13  County                 100000 non-null  object
#  14  State                  100000 non-null  object
#  15  Zipcode                99993 non-null   object
#  16  Country                100000 non-null  object
#  17  Timezone               99993 non-null   object
#  18  Airport_Code           99993 non-null   object
#  19  Weather_Timestamp      98946 non-null   object
#  20  Temperature(F)         98409 non-null   float64
#  21  Wind_Chill(F)          4322 non-null    float64
#  22  Humidity(%)            98144 non-null   float64
#  23  Pressure(in)           98708 non-null   float64
#  24  Visibility(mi)         98154 non-null   float64
#  25  Wind_Direction         98936 non-null   object
#  26  Wind_Speed(mph)        76180 non-null   float64
#  27  Precipitation(in)      7368 non-null    float64
#  28  Weather_Condition      98396 non-null   object
#  29  Amenity                100000 non-null  bool
#  30  Bump                   100000 non-null  bool
#  31  Crossing               100000 non-null  bool
#  32  Give_Way               100000 non-null  bool
#  33  Junction               100000 non-null  bool
#  34  No_Exit                100000 non-null  bool
#  35  Railway                100000 non-null  bool
#  36  Roundabout             100000 non-null  bool
#  37  Station                100000 non-null  bool
#  38  Stop                   100000 non-null  bool
#  39  Traffic_Calming        100000 non-null  bool
#  40  Traffic_Signal         100000 non-null  bool
#  41  Turning_Loop           100000 non-null  bool
#  42  Sunrise_Sunset         99999 non-null   object
#  43  Civil_Twilight         99999 non-null   object
#  44  Nautical_Twilight      99999 non-null   object
#  45  Astronomical_Twilight  99999 non-null   object
# dtypes: bool(13), float64(12), int64(1), object(20)
# memory usage: 26.4+ MB


#print(df['Severity'].unique()) ---[3 2 1 4]
##print(df['State'].unique())---['OH' 'WV' 'CA' 'FL' 'GA' 'SC' 'NE' 'IA' 'IL' 'MO' 'WI' 'IN' 'MI' 'NJ'
# 'NY' 'CT' 'MA' 'RI' 'NH' 'PA' 'KY' 'MD' 'VA' 'DC' 'DE' 'TX' 'WA' 'OR'
# 'AL' 'NC' 'AZ' 'TN' 'LA' 'MN' 'CO' 'OK' 'NV' 'UT' 'KS' 'NM' 'AR' 'MS'
# 'ME' 'VT' 'WY' 'ID' 'ND' 'MT' 'SD']



## 3. Limpieza básica de datos
#print( df[['State','Severity']].describe()) 
# Severity
# count  100000.000000
# mean        2.448120
# std         0.499931
# min         1.000000
# 25%         2.000000
# 50%         2.000000
# 75%         3.000000
# max         4.000000
# print(df.loc[(df['State'] == 'OH')&(df['Severity'] == 4)])
# print(df.loc[(df['State'] == 'WV')&(df['Severity'] == 4)])
# print(df.loc[(df['State'] == 'CA')&(df['Severity'] == 4).head()])
#print(df[['Description', 'State','City','Country']].loc[df['Severity'] == 4].reset_index(drop=True))

# print( "Ya se creo un archivo con la descripcion por estado" )


# ¿Cuántos accidentes hay por estado y severidad?
print(df.groupby(['State','Severity'])['Severity'].count())
df.groupby(['State','Severity'])['Severity'].count().to_csv('Por Estado.csv')
print( "Ya se creo un archivo con la descripcion por estado")

# ¿Cuál es la hora del día con más accidentes?
df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce', infer_datetime_format=True)

df_grouped = df.groupby([
    'State',
    'Severity',
    pd.Grouper(key='Start_Time', freq='D')
])['Severity'].count().reset_index(name='Accidents_Count')
#imprimir --- justo despues para que no se modifique la info
df_grouped = df.groupby([
    'State',
    'Severity',
    pd.Grouper(key='Start_Time', freq='D')
])['Severity'].count().reset_index(name='Accidents_Count').to_csv('Accidentes por estado y severidad.csv')

print(df_grouped)

# Filtrar solo los accidentes graves (Severity = 4)
df_graves = df[df['Severity'] == 4]
# Agrupar por Estado y Día
df_graves_grouped = df_graves.groupby([
    'State',
    pd.Grouper(key='Start_Time', freq='D')
]).size().reset_index(name='Grave_Accidents:Severity =4')
#imprimir --- justo despues para que no se modifique la info
df_graves_grouped.to_csv('Accidentes por estado y dia solo severidad 4.csv')

print(df_graves_grouped.head())
# Agrupar solo por día (sin importar el estado)
accidentes_por_dia = df_graves.groupby(
    pd.Grouper(key='Start_Time', freq='D')
).size().reset_index(name='Total_Accidents')

accidentes_por_dia.to_csv('Accidentes agrupados por dia, no importa en donde fue.csv')
# Obtener el día con más accidentes
dia_mas_accidentes = accidentes_por_dia.loc[
    accidentes_por_dia['Total_Accidents'].idxmax()
]

print(accidentes_por_dia.head())
print("📅 Día con más accidentes graves:")
print(dia_mas_accidentes)

#Guardando la info Obtenida



# ¿Qué días de la semana son más peligrosos?

# ¿Afecta el clima (lluvia, niebla) a la cantidad de accidentes?

# ¿En qué condiciones de visibilidad ocurren más accidentes?

#¿Que estado tiene la mayor cantidad de accidentes más severos?

## 4. Análisis exploratorio (EDA)
## 5. Visualizaciones
## 6. Conclusiones