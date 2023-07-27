# crie um programa onde 4 jogadores jogam um dado
# guarde esses resultados um um dicionario 
# no final, coloque me um dicionario em ordem (1°, 2°, ...)
import random 

dict = {}

for k in range(0,4):
    player = input('digite seu nome: ')
    dataResult = random.randrange(6)
    dict[player] = dataResult

for i in sorted(dict, key = dict.get):
    print(i, dict[i])





