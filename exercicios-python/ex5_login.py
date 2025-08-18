# While com Parada - Login com tentativas

senha_correta = "python123"
tentativas = 0
max_tentativas = 3
acesso = False

while tentativas < max_tentativas:
    tentativa = input("Digite a senha: ")
    if tentativa == senha_correta:
        print("Acesso liberado!")
        acesso = True
        break
    else:
        print("Senha incorreta.")
        tentativas += 1

if not acesso:
    print("Acesso bloqueado!")
