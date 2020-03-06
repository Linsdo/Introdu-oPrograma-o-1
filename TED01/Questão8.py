valor1 = float(input('Insira um número: '))
valor2 = float(input('Insira outro número: '))
soma = valor1 + valor2
calculo1 = soma + 8
calculo2 = soma - 5

if soma > 20:
    print(calculo1)
elif soma <= 20:
    print(calculo2)
else:
    print('Ocorreu um erro.')