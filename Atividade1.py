import os

notas = {}


for i in range(3):
    os.system('cls')
    aluno = input('Digite o nome do aluno: ')
    nota1 = float(input('Informe nota 1: '))
    nota2 = float(input('Informe nota 2: '))
    nota3 = float(input('Informe nota 3: '))
    nota4 = float(input('Informe nota 4: '))
    media = float((nota1 + nota2 + nota3 + nota4) / 4)

    notas[aluno] = {
        'NOTA 1': nota1,
        'NOTA 2': nota2,
        'NOTA 3': nota3,
        'NOTA 4': nota4,
        'MÉDIA': media
    }



print(notas)