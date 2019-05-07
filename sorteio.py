import random

# pega o valor mínimo
minimo = int(input("Valor mínimo: "))
# pega o valor máximo
maximo = int(input("Valor máximo: "))

# calcula o numero aleatório
num = random.randint(minimo, maximo)

# mostra na tela
print(num)