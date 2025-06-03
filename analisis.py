# Proyecto: Análisis de Accidentes en EE.UU.

# 1. Cargar librerías
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar visualizaciones
plt.style.use('ggplot')
sns.set()

# 2. Cargar el dataset
df = pd.read_csv('US_Accidents_Dec21_updated.csv')  # Cambia el nombre si el archivo es diferente
df.shape
## 2. Cargar y explorar los datos
# ¿Cuántos accidentes hay por estado?

# ¿Cuál es la hora del día con más accidentes?

# ¿Qué días de la semana son más peligrosos?

# ¿Afecta el clima (lluvia, niebla) a la cantidad de accidentes?

# ¿En qué condiciones de visibilidad ocurren más accidentes?
## 3. Limpieza básica de datos
## 4. Análisis exploratorio (EDA)
## 5. Visualizaciones
## 6. Conclusiones