import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt

# Carregando os dados do arquivo CSV
df = pd.read_csv("medias.csv")

# Dividindo os dados em características (features) e rótulo (target)
X = df[["high_school", "bachelor's_degree"]]
y = df["media"]

# Dividindo os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinando o modelo de regressão linear
model = LinearRegression()
model.fit(X_train, y_train)

# Fazendo previsões nos dados de teste
y_pred = model.predict(X_test)

# Calculando o erro médio quadrático (Mean Squared Error)
mse = mean_squared_error(y_test, y_pred)

# Calculando o viés (bias) e a variância do modelo
bias = np.mean((y_pred - np.mean(y_test))**2)
variance = np.var(y_pred)

# Exibindo o viés e a variância
print(f"Viés (Bias): {bias:.2f}")
print(f"Variância (Variance): {variance:.2f}")

# Criando um gráfico de dispersão (scatter plot) para visualização
plt.figure(figsize=(8, 6))
sns.scatterplot(x=X_test["high_school"], y=y_test, label="High School", alpha=0.7)
sns.scatterplot(x=X_test["bachelor's_degree"], y=y_test, label="Bachelor's Degree", alpha=0.7)
sns.lineplot(x=X_test["high_school"], y=y_pred, label="Predicted High School")
sns.lineplot(x=X_test["bachelor's_degree"], y=y_pred, label="Predicted Bachelor's Degree")
plt.xlabel("Valores de Educação")
plt.ylabel("Média")
plt.legend()
plt.title("Relevância da Educação na Média")
plt.show()
