#ENTRADA DE DADOS
nome = input("Digite seu nome:\n")
peso = float(input(nome+", digite seu peso em kg: \n"))
altura = float(input(nome+", digite sua altura em metros: \n"))

#CALCULO
imc = peso/(altura*altura)

print("\nCalculando..........\n")
print(nome+", seu resultado foi:")

#ESTRUTURA DE DECISÃO
if imc>40:
    print("Obesidade Grau 3")
elif imc>35 and imc<39:
    print("Obesidade Grau 2")
elif imc>30 and imc<34.9:
    print("Obesidade Grau 1")
elif imc>25 and imc<29.9:
    print("Sobrepeso")
elif imc>18.5 and imc<24.9:
    print("Peso Normal")
elif imc<18.5:
    print("Abaixo do peso")