#Primeiro desafio do bootcamp de python da plataforma DIO

#Entrada dos dados
entrada = input().split()

#Separação dos dados em diferentes variaveis
distancia = int(entrada[0])

diametro_torre_1 = int(entrada[1])

diametro_torre_2 = int(entrada[2])

#Calculo do ICM
icm = distancia / (diametro_torre_1 + diametro_torre_2)

#Exibição do resultado

print(f'O ICM entre as duas torres é de {icm:.2f}\n')