import pandas as pd

nome_arquivo = 'unemployed_population_1978-12_to_2023-07.csv'

dataframe = pd.read_csv(nome_arquivo, nrows=15)

dataframe.to_csv('lines.csv')