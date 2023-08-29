caneta_azul = 0
caneta_preta = 0
tot_final = 0
qtde_C_A = int(input('Informe a quantidade de canetas azuis: '))
caneta_azul = qtde_C_A * 2.00

qtde_C_P = int(input('Informe a quantidade de canetas pretas: '))
caneta_preta =  qtde_C_P * 2.50

tot_final = caneta_azul + caneta_preta
print('O preço final das compras é de: {}'.format(tot_final))