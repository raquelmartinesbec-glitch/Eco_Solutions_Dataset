import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Dataset
df = pd.read_csv("ecoenergy_consumption_data.csv")

# Exploración Dataset
df.head()
df.info()
df.describe()

# Datos nulos
df.isnull().sum()

# Normalizar fechas
df["billing_date"] = pd.to_datetime(df["billing_date"])
df["year"] = df["billing_date"].dt.year
df["month"] = df["billing_date"].dt.month

# Búsqueda de patrones

# Distribución del consumo
sns.histplot(df["consumption_kwh"])
plt.show()

# Coste total
sns.histplot(df["total_cost"])
plt.show()

# Consumo por región
sns.boxplot(x="region", y="consumption_kwh", data=df)
plt.show()

# Contrato vs Consumo
sns.boxplot(x="contract_type", y="consumption_kwh", data=df)
plt.show()

# Búsqueda de correlaciones
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()

# Detección de valores atípicos
sns.boxplot(df["consumption_kwh"])
plt.show()

sns.boxplot(df["total_cost"])
plt.show()

sns.boxplot(df["co2_emissions"])
plt.show()

# Top 5 regiones por consumo total
top_regions = df.groupby("region")["consumption_kwh"].sum().sort_values(ascending=False).head(5).index
df_top = df[df["region"].isin(top_regions)]

# Top 5 tipos de contrato por consumo total
top_contracts = df.groupby("contract_type")["consumption_kwh"].sum().sort_values(ascending=False).head(5).index
df_top = df[df["contract_type"].isin(top_contracts)]

# Normalizar/ Escalar columnas numéricas
num_cols = ["consumption_kwh", "total_cost", "co2_emissions", "cost_per_kwh"]
scaler = StandardScaler()
df_top[num_cols] = scaler.fit_transform(df_top[num_cols])

# Guardar el dataset limpio
df.to_csv("Ecoenergy_dataset_limpio2.csv", index=False)
