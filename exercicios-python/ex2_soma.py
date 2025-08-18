#Teoria: int() converte texto para número inteiro.

num1 = float(input("Digite o primeiro número: ")) 
num2 = float(input("Digite o segundo número: ")) 

opcao = input("Escolha a operação [+,-,*,/]: ").strip()

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2


if opcao == "+":
    print(f"A soma é {soma}")
elif opcao == "-":
    print(f"A subtração é {subtracao}")
elif opcao == "*":
    print(f"A multiplicação é {multiplicacao}")
elif opcao == "/":
    print(f"A divisão é {divisao}")

