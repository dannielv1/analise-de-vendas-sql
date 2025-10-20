import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ler os dados da tabela
df = pd.read_csv(r'C:\Users\danni\OneDrive\Documentos\Daniel\II\Análise de Vendas\vendascsv.csv', sep=';')
print(df.head())


# Total de vendas por região
faturamento = df.groupby('Regiao')['Valor'].sum().reset_index()
sns.barplot(data=faturamento, x='Regiao', y='Valor')
plt.title('Faturamento por Região')
plt.show()

# Produtos mais vendidos
produtos = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
produtos.plot(kind='bar', title='Produtos mais vendidos')
plt.show()