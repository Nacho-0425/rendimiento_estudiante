import pandas as pd

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