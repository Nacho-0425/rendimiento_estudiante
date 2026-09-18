import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv("StudentsPerformance.csv")

# Mostrar las primeras filas
print("--- Primeras 5 filas ---")
print(df.head())

# Mostrar información general (tipos de datos y nulos)
print("\n--- Información del Dataset ---")
print(df.info())

# Resumen estadístico
print("\n--- Resumen Estadístico ---")
print(df.describe())

# Nueva columna con el promedio total
df['average score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

print("\n--- Dataset con Promedio Calculado ---")
print(df[['gender', 'math score', 'reading score', 'writing score', 'average score']].head())

# Crear la carpeta outputs
os.makedirs("outputs", exist_ok=True)

# Crear una gráfica simple y guardarla
df[['math score', 'reading score', 'writing score']].mean().plot(kind='bar')
plt.title('Promedio de Calificaciones')
plt.ylabel('Promedio')

# Guardar la gráfica dentro de outputs
plt.savefig('outputs/promedio_calificaciones.png')
plt.close()

# 1. Gráfica de distribución de calificaciones de matemáticas
plt.figure(figsize=(8, 5))
sns.histplot(df['math score'], kde=True, color='skyblue')
plt.title('Distribución de Calificaciones de Matemáticas')
plt.xlabel('Puntuación de Matemáticas')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.savefig('outputs/distribucion_matematicas.png')
plt.close()

# 2. Gráfica de comparativa de promedio por género
plt.figure(figsize=(8, 5))
sns.boxplot(x='gender', y='average score', data=df, palette='Set2')
plt.title('Rendimiento Promedio por Género')
plt.xlabel('Género')
plt.ylabel('Promedio General')
plt.tight_layout()
plt.savefig('outputs/promedio_por_genero.png')
plt.close()

print("¡Nuevas gráficas guardadas exitosamente en outputs!")