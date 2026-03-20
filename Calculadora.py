n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

adição = (n1 + n2)
multiplicação = (n1 * n2)
divisão = (n1 / n2)
subtração = (n1 - n2)

operação = input(str("(+) Adição \n(-)Subtração \n(*)Multiplicação \n(/)Divisão \nDigite qual operação: "))

if operação == "+":
   print(n1 + n2)
elif operação == "-":
   print(n1 - n2)
elif operação == "*":
   print(n1 * n2)
elif operação == "/":
   print(n1 / n2)
else:
   print("Operação incorreta")

