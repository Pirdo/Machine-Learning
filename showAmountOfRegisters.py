import pandas as pd

nome_arquivo = 'unemployed_population_1978-12_to_2023-07.csv'

dataframe = pd.read_csv(nome_arquivo)

contagem_por_coluna = dataframe.nunique()

resultados_dataframe = pd.DataFrame(contagem_por_coluna)

resultados_dataframe.to_csv('registers.csv')