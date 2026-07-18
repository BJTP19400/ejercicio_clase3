import pandas as pd
def cargar_datos(ruta_archivo):
"""
Lee el dataset de e-shop clothing 2008.
Argumentos: ruta_archivo (str)
Retorna: DataFrame de pandas
"""
try:
# Nota: Ajustar el separador (sep) según el formato real del archivo (pueden ser espacios o comas)
df = pd.read_csv(ruta_archivo, sep=';')
print("Datos cargados exitosamente.")
return df
except Exception as e:
print(f"Error al cargar el archivo: {e}")

return None

def sales_funnel_analysis(df):
"""Analiza la pérdida de usuarios entre las páginas 1 y 5 de la tienda."""
return df['PAGE'].value_counts().sort_index()

def price_impact_by_location(df):
"""Relaciona la ubicación de la foto (1-6) con el interés en productos caros."""
return pd.crosstab(df['LOCATION'], df['PRICE 2'])

