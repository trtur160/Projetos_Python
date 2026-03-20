import time

print("BEM VINDO A 'Calculadora de divisão'")

print("Carregando...")
time.sleep(3)

dividendo = int(input("Digite o dividendo: "))

while True:
    divisor = int(input("Digite o divisor: "))
    if divisor > 0:
        break
    else:
        print("O divisor é menor que zero")
          
 
resultado = dividendo / divisor
print(f"O resultado da 'Disão' é: {resultado:.2f}")