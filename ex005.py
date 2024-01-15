# 5. Faça um Programa que converta metros para centímetros.
tipo = input('Você deseja:\nA) Converter METRO para CENTÍMETRO\nB) Converter CENTÍMETRO para METRO\nR: ')
if tipo == 'A':
    number1 = input('Informe o valor em METROS que você deseja converter: ')
    convertido = int(float(number1)) * 100
    print(f'{number1}m em CENTÍMETROS equivale a {convertido}cm.')
elif tipo == 'B':
    number1 = input('Informe o valor em CENTÍMETROS que você deseja converter: ')
    convertido = int(float(number1)) / 100
    print(f'{number1}cm em METROS equivale a {convertido}m.')