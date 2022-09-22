#Terceiro desafio de python do bootcamp DIO

#Declarando variaveis 

consumo = 12

#Entrada dos dados
entrada = input().split()

#Calculando a distancia
distancia_percorrida = int(entrada[0])*int(entrada[1])

#Calculando quantidade de combustivel
quantidade_combustivel = distancia_percorrida/consumo

#Exibindo resultado
print(f'{quantidade_combustivel:.3f}')
