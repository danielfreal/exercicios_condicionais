km = int(input('informe a quilometragem exercida: '))

if km <= 80:
    ('Não há histórico de multas')
else:
    multa = (km - 80) * 7
    print(f'O valor da multa será de R${multa:.2f}')    