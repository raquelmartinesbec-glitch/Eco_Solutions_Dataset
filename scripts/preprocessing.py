import pandas as pd
import numpy as np
from datetime import datetime

# Configuración de rutas
DATA_PATH = '../data/data_sample.csv'
CLEANED_PATH = '../data/data_cleaned.csv'

def cargar_datos(path):
    """Carga datos desde archivo CSV"""
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        # Generar datos ficticios si el archivo no existe
        return generar_datos_ficticios()

def generar_datos_ficticios():
    """Genera dataset ficticio para protección de datos"""
    np.random.seed(42)
    data = {
        'id': range(1, 101),
        'product_type': np.random.choice(['Solar_Unit', 'Energy_Storage', 'Converter'], 100),
        'energy_output': np.random.randint(2000, 5000, 100),
        'installation_date': pd.date_range('2024-01-01', periods=100, freq='D')
    }
    return pd.DataFrame(data)

def limpiar_datos(df):
    """Proceso de limpieza de datos"""
    # Eliminar duplicados
    df_clean = df.drop_duplicates()
    
    # Eliminar valores nulos
    df_clean = df_clean.dropna()
    
    # Validar rangos de energy_output
    df_clean = df_clean[df_clean['energy_output'] > 0]
    
    return df_clean

def procesar_datos():
    """Función principal de procesamiento"""
    # Cargar datos
    df = cargar_datos(DATA_PATH)
    
    # Limpiar datos
    df_clean = limpiar_datos(df)
    
    # Guardar datos procesados
    df_clean.to_csv(CLEANED_PATH, index=False)
    
    return df_clean

if __name__ == "__main__":
    procesar_datos()
