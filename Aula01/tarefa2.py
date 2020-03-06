nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))

resultado = (nota1 + nota2)/2

if(resultado >= 7):
  print('Aprovado')
elif(resultado <= 6 and resultado >= 4): 
 print('Voce esta na final')
elif (resultado <= 3):
  print('Reprovado')