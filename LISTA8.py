numero = [[],[]]

valor = 0

for c in range(1,8):

    valor = int(input('digite um valor:'))

    if valor % 2 ==0:

        numero[0].append(valor)

    else:

        numero[1].append(valor)

numero[0].sort()

numero[1].sort()

print(f'os valores pares foram:{numero[0]}')

print(f'os valores pares foram:{numero[1]}')
