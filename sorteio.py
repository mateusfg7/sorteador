import random

valorMinimo = int(input("Valor mínimo: \033[01;32m"))

valorMaximo = int(input("\033[00;00;00mValor máximo: \033[01;32m"))

numeroDeSorteios = int(input("\033[00;00;00mNumero de sorteios: \033[01;32m"))

idSorteio = 1

print("\033[00;00;00m\n")


for x in range(numeroDeSorteios):
	
	numeroSorteado = random.randint(valorMinimo, valorMaximo)
	
	print("\033[00;31mSorteio {}: \033[01;37;41m{}\033[00;00;00m".format(idSorteio, numeroSorteado))
	idSorteio += 1

print("\n")