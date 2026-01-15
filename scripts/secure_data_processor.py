import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class EcoenergyDataProcessor:
    """Procesador de datos para análisis de Ecoenergy Solutions"""
    
    def __init__(self, data_path='../data/data_sample.csv'):
        self.data_path = data_path
        self.df_original = None
        self.df_processed = None
        
    def generar_datos_ficticios(self, n_samples=100):
        """Genera dataset ficticio para protección de datos"""
        np.random.seed(42)
        
        product_types = ['Solar_Unit', 'Energy_Storage', 'Converter']
        
        data = {
            'id': range(1, n_samples + 1),
            'product_type': np.random.choice(product_types, n_samples),
            'energy_output': np.random.randint(2000, 5000, n_samples),
            'installation_date': pd.date_range('2024-01-01', periods=n_samples, freq='D'),
            'efficiency_rating': np.random.uniform(0.7, 0.95, n_samples),
            'maintenance_status': np.random.choice(['Good', 'Average', 'Needs_Check'], n_samples)
        }
        
        return pd.DataFrame(data)
    
    def cargar_datos(self):
        """Carga datos desde archivo o genera ficticios"""
        try:
            self.df_original = pd.read_csv(self.data_path)
        except FileNotFoundError:
            self.df_original = self.generar_datos_ficticios()
        
        return self.df_original
    
    def validar_datos(self, df):
        """Validaciones de calidad de datos"""
        # Validar energy_output positivo
        df = df[df['energy_output'] > 0]
        
        # Validar efficiency_rating en rango válido
        if 'efficiency_rating' in df.columns:
            df = df[(df['efficiency_rating'] >= 0) & (df['efficiency_rating'] <= 1)]
        
        return df
    
    def limpiar_datos(self):
        """Proceso completo de limpieza"""
        if self.df_original is None:
            raise ValueError("Debe cargar datos primero")
        
        df_clean = self.df_original.copy()
        
        # Eliminar duplicados
        df_clean = df_clean.drop_duplicates()
        
        # Eliminar valores nulos críticos
        df_clean = df_clean.dropna(subset=['id', 'product_type', 'energy_output'])
        
        # Validaciones específicas
        df_clean = self.validar_datos(df_clean)
        
        self.df_processed = df_clean
        return df_clean
    
    def generar_estadisticas(self):
        """Estadísticas generales no sensibles"""
        if self.df_processed is None:
            raise ValueError("Debe procesar datos primero")
        
        stats = {
            'total_registros': len(self.df_processed),
            'tipos_productos': self.df_processed['product_type'].nunique(),
            'energia_promedio': self.df_processed['energy_output'].mean(),
            'productos_por_tipo': self.df_processed['product_type'].value_counts().to_dict()
        }
        
        return stats
    
    def guardar_datos_procesados(self, output_path='../data/data_cleaned.csv'):
        """Guardar datos procesados"""
        if self.df_processed is None:
            raise ValueError("Debe procesar datos primero")
        
        self.df_processed.to_csv(output_path, index=False)
        
    def ejecutar_pipeline_completo(self):
        """Ejecuta el pipeline completo de procesamiento"""
        # Cargar datos
        self.cargar_datos()
        
        # Limpiar y procesar
        self.limpiar_datos()
        
        # Generar estadísticas
        stats = self.generar_estadisticas()
        
        # Guardar resultados
        self.guardar_datos_procesados()
        
        return stats

def main():
    """Función principal para ejecutar el procesamiento"""
    processor = EcoenergyDataProcessor()
    
    try:
        stats = processor.ejecutar_pipeline_completo()
        
        # Log solo información no sensible
        print("=== Procesamiento Completado ===")
        print(f"Total de registros procesados: {stats['total_registros']}")
        print(f"Tipos de productos únicos: {stats['tipos_productos']}")
        print("Datos guardados exitosamente")
        
    except Exception as e:
        print(f"Error en procesamiento: {type(e).__name__}")

if __name__ == "__main__":
    main()