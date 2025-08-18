#Condicional simples

idade = int(input("Qual a sua idade?: "))
cidade = input("Qual é a sua cidade?: ").strip()

if idade >= 60: 
    print(f"Você é idoso, tem {idade} e mora em {cidade}.") 
elif idade >= 18: 
    print(f"Você é adulto, tem {idade} e mora em {cidade}.") 
else: 
    print(f"Você é menor de idade, tem {idade} e mora em {cidade}")

    