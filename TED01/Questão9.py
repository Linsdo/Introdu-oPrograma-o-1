valor1 = float(input('Insira um número: '))
valor2 = float(input('Insira outro número: '))
valor3 = float(input('Insira outro número: '))

if valor1 > valor2 and valor1 > valor3 and valor2 > valor3:
    print(valor3,valor2,valor1)
elif valor1 > valor2 and valor1 > valor3 and valor2 < valor3:
    print(valor2,valor3,valor1)
elif valor2 > valor1 and valor2 > valor3 and valor1 > valor3:
    print(valor3,valor1,valor2)
elif valor2 > valor1 and valor2 > valor3 and valor1 < valor3:
    print(valor1,valor3,valor2)
elif valor3 > valor1 and valor3 > valor2 and valor1 > valor2:
    print(valor2,valor1,valor3)
elif valor3 > valor1 and valor3 > valor2 and valor1 > valor2:
    print(valor2,valor1,valor3)
else:
    print('Ocorreu um erro.')