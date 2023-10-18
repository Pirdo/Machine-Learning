# Machine Learning

### Problema

O problema analisado, é verificar a importância da educação em relação ao desemprego nos Estados Unidos.

### Dataset

Este conjunto de dados fornece informações sobre as taxas de desemprego para diferentes grupos demográficos nos Estados Unidos.

Os dados são provenientes da Biblioteca de Dados do Estado de Trabalho da Economic Policy Institute e de pesquisas econômicas realizadas pelo Federal Reserve Bank de St. Louis.

O conjunto de dados contém taxas de desemprego para vários grupos etários, níveis de educação, gêneros, raças e outros.

O dataset possui 537 linhas totais, onde 536 apresentam dados, e contém 122 colunas.

### Arquivos

Arquivo do Dataset: `unemployed_population_1978-12_to_2023-07.csv`

Para instalar todas as bibliotecas necessárias, execute o comando a seguir:

```
pip install pandas numpy scikit-learn seaborn matplotlib
```

Para vizualizar as 15 primeiras linhas do Dataset, execute o arquivo `showLines.py`, ele irá gerar um CSV.

Para vizualizar quantos elementos existem por classe, execute o arquivo `showAmountOfRegisters.py`, ele irá gerar um CSV.

Para sumarizar os dados do Dataset por média, moda, mediana, quartil, mínimo, máximo, variância, desvio padrão, execute o arquivo `prepareData.py`, ele irá gerar um CSV.

Para executar o modelo de ML, execute o arquivo `modelo.py`, ele pega os dados do arquivo CSV `medias.csv`, e executa a previsão, exibindo um gráfico.

### Conclusão

Concluímos que o indice de desemprego é maior para pessoas com menor grau de escolaridade. Uma possível solução é incentivar jovens no ensino médio à continuarem para a faculdade, com programas de bolsa e etc.
