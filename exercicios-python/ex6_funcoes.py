# Funções

def saudacao(nome):
    return f"Olá, {nome}!"

def idade_para_100(idade):
    return 100 - idade

usuario = input("Digite seu nome: ")
print(saudacao(usuario))

idade = int(input("Digite sua idade: "))
faltam = idade_para_100(idade)
print(f"Faltam {faltam} anos para você completar 100 anos.")
