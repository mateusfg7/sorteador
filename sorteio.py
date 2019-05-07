import random # biblioteca de ramdomisação de numeros

# pega o valor mínimo
minimo = int(input("Valor mínimo: \033[01;32m"))
# pega o valor máximo
maximo = int(input("\033[00;00;00mValor máximo: \033[01;32m"))
# pega o numero de sorteios
numSort = int(input("\033[00;00;00mNumero de sorteios: \033[01;32m"))

idSort = 1 # identificação do sorteio

print("\033[00;00;00m\n")

# loop de sorteio
for x in range(numSort):
	# calcula o numero aleatório
	num = random.randint(minimo, maximo)
	# mostra na tela
	print("\033[00;31mSorteio {}: \033[01;37;41m{}\033[00;00;00m".format(idSort, num))
	idSort += 1

print("\n")