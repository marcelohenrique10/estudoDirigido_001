# Laço de Repetição - Tabuada

numero = int(input("Digite um número para ver a tabuada: "))

print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# Tarefa extra: todas as tabuadas de 1 a 10
print("\n--- Todas as tabuadas de 1 a 10 ---")
for n in range(1, 11):
    print(f"\nTabuada do {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
