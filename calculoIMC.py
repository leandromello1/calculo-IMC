print("Programa para calcular IMC")

print("Por favor informe seu peso: ")
peso = float(input())

print("Por favor digite sua altura em centímetros: ")
altura = float(input())

IMC = peso / ((altura / 100)**2)
print("Seu IMC é: ", IMC)

if IMC >= 25:
    print ("Você precisa emagrecer!")
else:
    print ("Você não precisa emagrecer!")

print("Fim do programa.")