matriz = [[0,0,0],[0,0,0],[0,0,0]]

somapar = 0

maior = 0

scol = 0

for l in range(0,3):

    for c in range(0,3):

        matriz[l][c] = int(input('Digite um valor:'))

print('-='*30)

for l in range(0,3):

    for c in range(0,3):

        print(f'[{matriz[l][c]:^5}]', end='')

        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]

    print()

print('-='*30)

print(f' A soma dos velores pares é {somapar}')

for l in range(0,3):

    scol += matriz[l][2]

print(f' A soma dos valores da terceira coluna é: {scol}')

for c in range(0,3):

    if c==0:

        maior = matriz[1][c]

    elif matriz[1][c] > maior:

        maior = matriz[1][c]

print(f' o maior valor da sugunda linha é {maior}')
