import os
import math

# Função para limpar a tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Calcula e imprime o IMC
def calcular_imc():
    peso = float(input("Informe seu peso (kg): "))
    altura = float(input("Informe sua altura (m): "))

    imc = round(peso / altura ** 2, 2)
    print(f"Seu IMC é: {imc}\n")

    if imc < 17:
        print("Muito abaixo do peso")
    elif 17 <= imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc < 25:
        print("Peso normal")
    elif 25 <= imc < 30:
        print("Acima do peso")
    elif 30 <= imc < 35:
        print("Obesidade Grau I")
    elif 35 <= imc < 40:
        print("Obesidade Grau II (severa)")
    else:
        print("Obesidade Grau III (mórbida)")

# Loop principal do programa
while True:
    clear_screen()
    calcular_imc()

    verificar = input("\nDeseja calcular outro IMC? (S/N): ").strip().upper()
    if verificar == "N":
        print("Saindo do programa...")
        break
