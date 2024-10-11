import pandas as pd

dados = {
    'cargos': ['assistente', 'auxiliar', 'gerente'],
    'salários': [2500, 1000, 750]
}

dados_bi = pd.DataFrame(dados)
print(dados_bi)

# dados_cargos = pd.Series(dados['salários'])
# print(dados_cargos.values)

# df_linha = dados_bi.loc[1]
# print(df_linha)

print(dados_bi.iloc[1]['cargos'])
print(dados_bi.iloc[1]['salários'])