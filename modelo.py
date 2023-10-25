import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
import csv

# Lê o arquivo CSV
df = pd.read_csv("unemployed_population_1978-12_to_2023-07.csv")

# Define a primeira data e a frequência mensal
start_date = "2023-08-01"
freq = "MS"

# Crie um DataFrame com datas mensais
date_range = pd.date_range(start=start_date, periods=len(df), freq=freq)

# Adicione as datas ao DataFrame original
df['Date'] = date_range

# Escolha a coluna de interesse (índice de desemprego)
X = df.index.values.reshape(-1, 1)  # Usamos o índice do DataFrame como entrada
y = df["all"]

# Divide os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crie um modelo de regressão linear
model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())

# Treine o modelo nos dados de treinamento
model.fit(X_train, y_train)

# Faça previsões nos dados de teste
y_pred = model.predict(X_test)

# Calcule as métricas de desempenho
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Imprima as métricas
print(f"MSE (Erro Quadrático Médio): {mse}")
print(f"R² (Coeficiente de Determinação): {r2}")

# Faça previsões para os próximos 10 meses
future_months = np.array(range(len(df), len(df) + 10)).reshape(-1, 1)
future_predictions = model.predict(future_months)

# Crie um DataFrame para as previsões futuras
future_dates = pd.date_range(start=start_date, periods=10, freq=freq)
future_df = pd.DataFrame({
    "Date": future_dates,
    "Predicted_Unemployment_Index": future_predictions
})

# Organize as datas em ordem decrescente
future_df = future_df.sort_values(by='Date', ascending=False)

# Calcule a variância dos valores previstos
variance = np.var(future_df["Predicted_Unemployment_Index"])
print(f"Variância dos valores previstos: {variance}")

# Salve as previsões em um arquivo CSV
future_df.to_csv("unemployment_predictions.csv", index=False, quoting=csv.QUOTE_NONNUMERIC)
