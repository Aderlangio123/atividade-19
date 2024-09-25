# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.

numero = int(input("digite o numero!:  "))

resultado = 1

for n in range(1, numero+1):
    resultado = resultado * n

print(f"O resultado de {numero}! é:", resultado)