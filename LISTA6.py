from random import randint

lista = list()

jogos = list()

print('SIMULADOR DE JOGOS MEGA SENA')

quant = int(input('Quantos jogos você quer: '))

total = 1

while total <= quant:

    cont = 0

    while True:

        num = randint(1,60)

        if num not in lista:

            lista.append(num)

            cont += 1

        if cont >=6:

            break

    lista.sort()

    jogos.append(lista[:])

    lista.clear()

    total +=1

print(f'Os numeros sorteados para {quant} jogos')

for i, l in enumerate(jogos):

    print(f'jogos{i+1}:{l}')