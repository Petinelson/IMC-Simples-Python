from click import clear
from os import system
import math

#Metodo Python
while(True):
    clear()
    peso = float(input("informe seu peso: "))
    altura = float(input("informe sua altura: "))

    imc = peso / altura ** 2
    imc = round(imc, 2)
    print(f"Seu imc é: {imc} \n")

    if imc < 17.0:
        print("Muito abaixo do peso")
    elif 17.0 >= imc <= 18.49:
        print("Abaixo do peso")
    elif 18.5 >= imc <= 24.99:
        print("Peso normal")
    elif 25.0 >= imc <= 29.99:
        print("Acima do peso")
    elif 30.0 >= imc <= 34.99:
        print("Obesidade 1")
    elif 35.0 >= imc <= 39.99:
        print("Obesidade 2 (severa)")
    else:
        print("Obesidade 3 (móbida")

    verificar = input("Deseja continuar no sistema (S/N)")
    if verificar == "N":
        break
    else:
      continue
