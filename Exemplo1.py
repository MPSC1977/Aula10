import os

os.system('cls')


dicionario = {
    'nome': 'Patrick',
    'telefone': '21912345678',
    'idade': 18,
    'CPF': '123.456.789-00'
}

# ACESSAR OS VALORES DO DICIONÁRIO
print(dicionario['nome'])
print(dicionario['telefone'])
print(dicionario['idade'])
print(dicionario['CPF'])


# ALTERAR OS VALORES DO DICIONÁRIO
dicionario['nome'] = 'Paula'
print(dicionario)


# CRIANDO NOVAS CHAVES E VALORES PARA O DICIONÁRIO
dicionario['email'] = 'patrickcurvao@gmail.com'
dicionario['CEP'] = '24.430-130'
print(dicionario)


# REMOVER CHAVES DO DICIONÁRIO - del
del dicionario['email']
print(dicionario)


# REMOVER CHAVES DO DICIONÁRIO - pop retorna o valor da chave apagada
print(dicionario.pop('idade', 'não encontrado'))
print(dicionario)