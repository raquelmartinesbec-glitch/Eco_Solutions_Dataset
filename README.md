# ⚡ Proyecto de Análisis y Limpieza de Datos - Ecoenergy Solutions Dataset

Este repositorio documenta un flujo completo de análisis, manipulación y limpieza de datos basado en el dataset de Ecoenergy Solutions, una empresa dedicada a soluciones energéticas sostenibles.

## 📋 Descripción del Proyecto

El objetivo principal es analizar patrones de consumo energético, aplicar técnicas de limpieza y normalización, y generar datasets ficticios para proteger la confidencialidad de la información real de clientes y operaciones.

### 🔒 Confidencialidad y Privacidad de Datos

**IMPORTANTE**: Este repositorio NO contiene datos reales de clientes ni instalaciones. Por seguridad y cumplimiento de normativas:

- ✅ Se utilizan exclusivamente **datos ficticios** generados sintéticamente
- ✅ Los datos ficticios **replican la estructura** del dataset real sin comprometer información sensible
- ✅ No se incluyen nombres, direcciones, información financiera ni datos personales reales
- ✅ El generador de datos sintéticos permite recrear escenarios de análisis sin riesgos de privacidad

## 🗂️ Estructura del Proyecto

```
Ecoenergy_Solutions_Dataset/
├── 📓 notebooks/                    # Jupyter Notebooks para análisis exploratorio
│   └── 01_data_cleaning_analysis.ipynb
├── 🐍 scripts/                     # Scripts de procesamiento y generación
│   ├── preprocessing.py
│   └── secure_data_processor.py
├── 📊 data/                        # Datasets ficticios generados
│   └── data_sample.csv
├── 📋 reports/                     # Informes y documentación
│   └── Informe_Ecoenergy_Solutions_Dataset.pdf
├── 🔧 .gitignore                   # Configuración de archivos ignorados
├── 📝 README.md                    # Este archivo
└── 📦 requirements.txt             # Dependencias del proyecto
```

## 🚀 Instalación y Uso

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### 1. Configuración del Entorno
```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd Ecoenergy_Solutions_Dataset

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Generar Datos Ficticios
```bash
# Ejecutar el generador de datos
python scripts/secure_data_processor.py
```

### 3. Análisis Exploratorio
```bash
# Abrir Jupyter Notebook
jupyter notebook notebooks/01_data_cleaning_analysis.ipynb
```

## 📊 Estructura del Dataset Ficticio

El dataset generado contiene las siguientes columnas:

| Columna            | Tipo     | Descripción                                 |
|--------------------|----------|---------------------------------------------|
| `id`               | integer  | Identificador único de instalación          |
| `product_type`     | string   | Tipo de producto energético                 |
| `energy_output`    | integer  | Producción energética estimada (kWh)        |
| `installation_date`| date     | Fecha de instalación                        |
| `efficiency_rating`| float    | Eficiencia estimada del sistema             |
| `maintenance_status`| string  | Estado de mantenimiento                     |

## 🧹 Proceso de Limpieza de Datos

El pipeline de limpieza incluye:

1. **Identificación de valores faltantes**: Análisis de patrones de datos ausentes
2. **Eliminación de columnas no utilizables**: Columnas con >60% de valores faltantes
3. **Normalización de fechas**: Conversión a formato estándar y extracción de características temporales
4. **Estandarización numérica**: Aplicación de StandardScaler para variables numéricas
5. **Codificación categórica**: LabelEncoder para variables categóricas
6. **Eliminación de duplicados**: Identificación y remoción de registros duplicados

## 🔍 Características del Análisis

- **Análisis Exploratorio**: Estadísticas descriptivas, distribuciones y patrones de consumo
- **Calidad de Datos**: Identificación de inconsistencias y valores atípicos
- **Visualizaciones**: Gráficos para entender el comportamiento energético
- **Simulación de Problemas**: Recreación de escenarios de datos sucios para práctica

## 📊 Dashboard Interactivo

Consulta el dashboard en Looker Studio aquí:  
[Ver Dashboard en Looker Studio](https://lookerstudio.google.com/s/tquO7nog_vE)

## 🛡️ Consideraciones de Seguridad

- Los datos ficticios se generan usando librerías como `numpy` y funciones personalizadas
- No se almacenan credenciales ni información sensible en el repositorio
- El `.gitignore` está configurado para excluir archivos de configuración locales
- El informe original se incluye como excepción para documentación del proyecto

## 🤝 Contribuciones

Este proyecto está diseñado para fines educativos y de análisis. Las contribuciones son bienvenidas siguiendo las mejores prácticas de desarrollo colaborativo.

## 📄 Licencia

Proyecto desarrollado con fines académicos y de aprendizaje en manipulación y limpieza de datos.

---

*⚠️ Recordatorio: Este repositorio contiene únicamente datos ficticios. Cualquier similitud con personas, instalaciones o consumos reales es pura coincidencia.*