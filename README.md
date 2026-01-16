# Informe Ecoenergy Solutions Dataset

Análisis exploratorio sobre limpieza, normalización y visualización de datos del consumo energético de clientes de Ecoenergy Solutions.

## 🎯 Objetivo

Este proyecto se centra en analizar de manera exploratoria un dataset sobre el consumo energético de clientes. Se busca identificar patrones relevantes utilizando técnicas de limpieza, normalización de datos y análisis estadístico, con representación visual mediante dashboards.

## 📁 Estructura del Proyecto

```
Ecoenergy_Solutions_Dataset/
├── notebooks/           # Jupyter Notebooks para análisis exploratorio
│   └── 01_data_cleaning_analysis.ipynb
├── scripts/            # Scripts de procesamiento y limpieza
│   ├── preprocessing.py
│   └── secure_data_processor.py
├── data/              # Datasets ficticios para protección de datos
│   └── data_sample.csv
├── reports/           # Informes y documentación
│   └── Ecoenergy_Report.pdf
├── .gitignore
├── README.md
└── requirements.txt
```

## 🔍 Metodología Aplicada

### 1. Preparación y Limpieza del Dataset
- Revisión del estado inicial: estructura, tipos de datos y valores faltantes
- Análisis de estadísticas básicas de variables numéricas
- Identificación de problemas en los datos

### 2. Normalización Temporal
```python
df["billing_date"] = pd.to_datetime(df["billing_date"])
df["year"] = df["billing_date"].dt.year
df["month"] = df["billing_date"].dt.month
```
Transformación de fechas de formato string a datetime para facilitar análisis temporales.

### 3. Análisis de Patrones y Correlaciones
- **Distribución del consumo**: Identificación de homogeneidad/heterogeneidad
- **Análisis de costes**: Detección de patrones y tarifas anómalas
- **Consumo por región**: Identificación de regiones con mayor variabilidad
- **Contrato vs Consumo**: Evaluación del impacto del tipo de contrato
- **Matriz de correlaciones**: Análisis de relaciones entre variables clave

### 4. Detección de Valores Atípicos
Análisis mediante boxplots en variables críticas:
- Consumo energético (kWh)
- Coste total
- Emisiones CO2

### 5. Normalización y Reducción de Dimensionalidad
```python
# Top 5 regiones y contratos por consumo
top_regions = df.groupby("region")["consumption_kwh"].sum().sort_values(ascending=False).head(5).index
top_contracts = df.groupby("contract_type")["consumption_kwh"].sum().sort_values(ascending=False).head(5).index

# Escalado de variables numéricas
scaler = StandardScaler()
df_top[num_cols] = scaler.fit_transform(df_top[num_cols])
```


## 📊 Dashboard y Visualizaciones

Puedes consultar el dashboard interactivo en Looker Studio aquí:
[Ver Dashboard en Looker Studio](https://lookerstudio.google.com/s/tquO7nog_vE)

### Indicadores Principales:
1. **Ranking de clientes por consumo**: Identificación de mayores consumidores
2. **Consumo por región**: Diferencias geográficas significativas
3. **Consumo por tipo de contrato**: Impacto del segmento (comercial vs residencial)
4. **Dispersión Consumo vs Coste**: Validación del sistema de facturación
5. **Adopción de renovables**: Análisis por región y tipo de contrato

## 🔑 Conclusiones Principales

- **El consumo es el principal factor determinante del coste**, con una correlación lineal clara
- **Diferencias significativas** entre regiones y tipos de contrato en patrones de consumo
- **Los clientes comerciales** presentan consumos mucho más elevados que los residenciales
- **Las regiones Centro y Norte** muestran mayor demanda energética
- **Los valores atípicos** explican gran parte de la variabilidad en el consumo
- **La reducción de dimensionalidad** permitió extraer insights más claros y evitar errores de visualización
- **Sistema de facturación consistente**: a mayor consumo, mayor coste
- **Adopción desigual de renovables** entre regiones y tipos de contrato

## 🛠️ Tecnologías Utilizadas
- **Python**: Pandas, NumPy, Matplotlib, Plotly, Seaborn
- **Análisis**: Google Colab
- **Visualización**: Looker Studio
- **Normalización**: StandardScaler
- **Control de versiones**: Git

## 📋 Requisitos
Consulta `requirements.txt` para las dependencias necesarias del entorno Python.

## 🔒 Protección de Datos
Este repositorio utiliza datos ficticios generados automáticamente para proteger la información sensible de los clientes reales.
