#Calculadora

Num1 = int(input("Digite um número:"))
Num2 = int(input("Digite outro número:"))

soma = "+"
subtração = "-"

operação = str(input("Qual operação você quer + ou -: "))

if operação == soma:
   print(f"A soma é:", Num1 + Num2)

elif operação == subtração:
   print(f"O valor é: ", Num1 - Num2)

else:
  print(f"Valor inválido")

