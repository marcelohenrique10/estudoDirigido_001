def cadastrar(lista, item):
    if not item:
        print("✖ Nome não pode ser vazio.")
        return
    
    if item in lista:
        print("✖ Item já existe.")
        return

    lista.append(item)
    print("✔ Item cadastrado!")

def listar(lista):
    if not lista:
        print("Lista vazia.")
    else:
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")

def remover(lista, numero):
    if 1 <= numero <= len(lista):
        removido = lista.pop(numero - 1)
        print(f"✔ Item '{removido}' removido!")
    else:
        print("✖ Número inválido.")
