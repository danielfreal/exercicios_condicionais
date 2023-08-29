maior = 0
menor = 0

for p in range(1, 4):
    num = float(input('Informe o {}° número: '.format(p)))

    if p == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))