valor1 = float(input('Insira um número: '))
valor2 = float(input('Insira outro número: '))
calculo1 = valor1 - valor2
calculo2 = valor2 - valor1

if valor1 > valor2:
    print('A diferença entre os números é de:',calculo1)
elif valor1 < valor2:
    print('A diferença entre os números é de:',calculo2)
else:
    print('A diferença entre os valores é 0')