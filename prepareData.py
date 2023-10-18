import pandas as pd

# Substitua 'seuarquivo.csv' pelo nome do seu arquivo CSV
nome_arquivo = 'unemployed_population_1978-12_to_2023-07.csv'

# Carregando o arquivo CSV em um DataFrame
dataframe = pd.read_csv(nome_arquivo)

# Obtendo as colunas a partir da segunda coluna em diante
colunas = dataframe.columns[1:]

# Dicionário para armazenar os resultados
resultados = {
    'Coluna': [],
    'Média': [],
    'Moda': [],
    'Mediana': [],
    '25% Quartil': [],
    '50% Quartil': [],
    '75% Quartil': [],
    'Mínimo': [],
    'Máximo': [],
    'Variância': [],
    'Desvio Padrão': []
}

# Calculando estatísticas para cada coluna
for coluna in colunas:
    resultados['Coluna'].append(coluna)
    
    # Média
    media = dataframe[coluna].mean()
    resultados['Média'].append(media)

    # Moda
    moda = dataframe[coluna].mode().values[0]
    resultados['Moda'].append(moda)

    # Mediana
    mediana = dataframe[coluna].median()
    resultados['Mediana'].append(mediana)

    # Quartis (25%, 50%, 75%)
    quartis = dataframe[coluna].quantile([0.25, 0.5, 0.75])
    resultados['25% Quartil'].append(quartis[0.25])
    resultados['50% Quartil'].append(quartis[0.5])
    resultados['75% Quartil'].append(quartis[0.75])

    # Mínimo e Máximo
    minimo = dataframe[coluna].min()
    maximo = dataframe[coluna].max()
    resultados['Mínimo'].append(minimo)
    resultados['Máximo'].append(maximo)

    # Variância
    variancia = dataframe[coluna].var()
    resultados['Variância'].append(variancia)

    # Desvio Padrão
    desvio_padrao = dataframe[coluna].std()
    resultados['Desvio Padrão'].append(desvio_padrao)

# Criando um DataFrame a partir dos resultados
resultados_dataframe = pd.DataFrame(resultados)

# Salvando os resultados em um novo arquivo CSV
resultados_dataframe.to_csv('resultados_estatisticos.csv', index=False)
