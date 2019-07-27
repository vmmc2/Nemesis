#!/usr/bin/python
import Cache as ch 
import numpy as np 

def print_cont_arquivo(lista):
	"""Funcao que serve para verificar se o arquivo foi lido corretamente"""
	for endereco in lista:
		print(endereco)

def imprime_lista(lista):
	for address, modo in lista:
		print("Address: {}  ---- Modo de Acesso: {}".format(address, modo))

def main():

	print("Bem vindo ao Nemesis: Um simulador de cache baseado na arquitetura de processadores RISC-V.")
	print(" ")
	print("O Nemesis busca simular operacoes de escrita e de leitura em uma Cache de 1024 palavras")
	print(" ")
	print("Nele, seremos capazes de ver o estado final da Cache depois de termos realizado todas as operacoes de escrita e de leitura solicitadas pelo usuario.")
	print(" ")
	print("Alem disso, o Nemesis tambem fornece as importante taxas de Hit Rate e Miss Rate.")
	print(" ")
	print("Ele tambem prove a quantidade de acessos realizados, a quantidade de hits e de misses (divididos em misses compulsorios e misses por conflito).")
	print(" ")
	print("Trabalharemos com um endereco de tamanho de 32 bits. Logo, o valor decimal inserido deve ser algo entre 0 ate 2e31 - 1. Com ambas as extremidades inclusas.")
	print(" ")
	print("Importante lembrar tambem que um bloco presente em uma cache se apresenta dividido em palavras/words. Cada palavra por sua vez apresenta 32 bits, podendo, portanto")
	print("representar valores numa faixa de -2e31 ate 2e31 - 1.")
	print(" ")
	print("O Nemesis conta com as seguintes variedades para implementar e trabalhar com um cache de 1024 palavras:")
	print("  ")
	print("*******************************************************************  NEMESIS SIMULATOR *****************************************************************")
	print("*               A                             B                                        C                                          D                    *")
	print("*         Direct-Mapping  -------  Two-Way Set Associative  --------------- Four-Way Set Associative --------------------  Fully Associative           *")
	print("*(I)      1 words/block                1 words/block                             1 words/block                               1 words/block             *")
	print("*(II)     2 words/block                2 words/block                             2 words/block                               2 words/block             *")
	print("*(III)    4 words/block                4 words/block                             4 words/block                               4 words/block             *")
	print("*(IV)     8 words/block                8 words/block                             8 words/block                               8 words/block             *")
	print("*                                                                                                                                                      *")
	print("********************************************************************************************************************************************************")
	print(" ")
	print("O Nemesis suporta tanto escritas como leituras.")
	print("Primeiramente, o usuario devera informar se o input sera por meio do terminal ou por meio de um arquivo do tipo .txt")
	print(" ")
	print(" ")
	print("OBS:. No caso de um arquivo do tipo .txt favor nomear o arquivo da seguinte maneira: 'entrada.txt' (sem aspas). Alem disso, o arquivo de entrada deve estar dentro da mesma pasta do projeto.")
	print("Ademais, o arquivo devera ser organizado da segunte maneira, a primeira linha devera conter um numero n (quantidade de acessos a cache) e nas n linhas seguintes deveremos ter dois numeros e uma letra")
	print("separados por um espaco de acordo com o seguinte layout:")
	print("NUM_ADDRESS        MODO_DE_ACESSO.")
	print("Tanto o endereco como o dado devem ser escrito de acordo com a base numerica decimal. O MODO_DE_ACESSO funciona assim: w(write) e r(read)")
	print(" ")
	print(" ")
	print("No caso de um input pelo terminal, o layout deve ser o mesmo do layout da entrada por meio de um arquivo .txt")
	print("Apos processar tanto as escritas como as leituras, o Nemesis ficara encarregada de apresentar o estado final da cache e mais: A quantidade de hits, misses(separados em misses por conflito e")
	print("misses compulsorios, hit rate e miss rate.")
	print("Input por um arquivo do tipo .txt: 1 ------------- Input pelo terminal: 2")
	type_input = int(input())
	lista_de_enderecos = []
	#INPUT SERA DADO ATRAVES DE UM ARQUIVO .TXT
	if type_input == 1:
		file = open("input.txt", 'r')
		"""Aqui efetuamos a leitura linha por linha do arquivo. Para que em seguida, possamos efetuar o parsing"""
		f_content = file.readline()
		while len(f_content) > 0:
			lista_de_enderecos.append(f_content)
			f_content = file.readline()
		file.close()
	#INPUT SERA DADO PELO TERMINAL
	elif type_input == 2: 
		qtd_enderecos = eval(input("Digite a quantidade de enderecos a serem acessados: "))
		for i in range(0, qtd_enderecos):
			num_address, mode = input().split()
			num_address = int(num_address)
			mode = str(mode)
			lista_de_enderecos.append((num_address, mode))
		imprime_lista(lista_de_enderecos)
	#ATE AGORA TA PEGANDO O INPUT PELO TERMINAL CERTINHO
	#VAMOS TESTAR AGORA A SELECAO DO MODO DA CACHE
	print("Selecione qual modo de Cache voce deseja simular: Por exemplo, se vc deseja simular uma Cache Direct-Mapping que apresenta 1 words/block, insira A1. Para mais exemplos, consulte a tabela acima.")
	modo_cache = input()


	''' '''
	'''VARIAVEIS QUE SERAO UTILIZADAS PARA COMPUTAR O MISS RATE, HIT RATE, ETC ETC'''
	QTD_ACESSOS = qtd_enderecos
	QTD_HITS = 0
	QTD_MISSES = 0
	QTD_MISSES_COMPULSORIOS = 0
	QTD_MISSES_CONFLITO = 0
	''' '''

	#CACHE DO TIPO A1

	if modo_cache == "A1": #CACHE DIRECT-MAPPING WITH 1 WORDS/BLOCK
		#PRIMEIRO PASSO: INICIALIZAR A CACHE
		memory = ch.Cache("A1")
		#memory.print_cache()
		#SEGUNDO PASSO, HORA DE CALCULAR OS HITS E OS MISSES....
		for num_address, mode in lista_de_enderecos:
			#CALCULA O ENDERECO PRIMEIRO. NO CASO TEM QUE CALCULAR O INDEX:
			binary_address = np.binary_repr(num_address, 32)
			sentence = f"Binary Address: {binary_address} ---- Decimal Address: {num_address}"
			#MASSA, JA PASSEI O ENDERECO PARA BINARIO. HORA DE INSERIR NA CACHE...
			if mode == 'w':
				#MODO ESCRITA: SO TEM QUE JOGAR NA CACHE
				memory.write_cache(num_address, binary_address, "A1")
			elif mode == 'r':
				hit_miss = memory.read_cache(num_address, binary_address, "A1")
				if hit_miss == 1: #TIVEMOS UM HIT
					QTD_HITS += 1
				elif hit_miss == 2: #TIVEMOS UM MISS COMPULSORIO
					QTD_MISSES += 1
					QTD_MISSES_COMPULSORIOS += 1
				elif hit_miss == 3: #TIVEMOS UM MISS POR CONFLITO
					QTD_MISSES += 1
					QTD_MISSES_CONFLITO += 1			
		memory.print_cache()

	#CACHE DO TIPO A2

	elif modo_cache == "A2":#CACHE DIRECT-MAPPING WITH 2 WORDS/BLOCK
		#PRIMEIRO PASSO: INICIALIZAR A CACHE
		memory = ch.Cache("A2")
		#SEGUNDO PASSO, HORA DE CALCULAR OS HITS E OS MISSES....
		for num_address, mode in lista_de_enderecos:
			#CALCULA O ENDERECO PRIMEIRO. NO CASO TEM QUE CALCULAR O INDEX:
			binary_address = np.binary_repr(num_address, 32)
			sentence = f"Binary Address: {binary_address} ---- Decimal Address: {num_address}"
			#MASSA, JA PASSEI O ENDERECO PARA BINARIO. HORA DE INSERIR NA CACHE...
			if mode == 'w':
				#MODO ESCRITA: SO TEM QUE JOGAR NA CACHE
				memory.write_cache(num_address, binary_address, "A2")
			elif mode == 'r':
				hit_miss = memory.read_cache(num_address, binary_address, "A2")
				if hit_miss == 1: #TIVEMOS UM HIT
					QTD_HITS += 1
				elif hit_miss == 2: #TIVEMOS UM MISS COMPULSORIO
					QTD_MISSES += 1
					QTD_MISSES_COMPULSORIOS += 1
				elif hit_miss == 3: #TIVEMOS UM MISS POR CONFLITO
					QTD_MISSES += 1
					QTD_MISSES_CONFLITO += 1
		memory.print_cache()

	#CACHE DO TIPO A3

	elif modo_cache == "A3":#CACHE DIRECT-MAPPING WITH 4 WORDS/BLOCK
		#PRIMEIRO PASSO: INICIALIZAR A CACHE
		memory = ch.Cache("A3")
		#SEGUNDO PASSO, HORA DE CALCULAR OS HITS E OS MISSES....
		for num_address, mode in lista_de_enderecos:
			#CALCULA O ENDERECO PRIMEIRO. NO CASO TEM QUE CALCULAR O INDEX:
			binary_address = np.binary_repr(num_address, 32)
			sentence = f"Binary Address: {binary_address} ---- Decimal Address: {num_address}"
			#MASSA, JA PASSEI O ENDERECO PARA BINARIO. HORA DE INSERIR NA CACHE...
			if mode == 'w':
				#MODO ESCRITA: SO TEM QUE JOGAR NA CACHE
				memory.write_cache(num_address, binary_address, "A3")
			elif mode == 'r':
				hit_miss = memory.read_cache(num_address, binary_address, "A3")
				if hit_miss == 1: #TIVEMOS UM HIT
					QTD_HITS += 1
				elif hit_miss == 2: #TIVEMOS UM MISS COMPULSORIO
					QTD_MISSES += 1
					QTD_MISSES_COMPULSORIOS += 1
				elif hit_miss == 3: #TIVEMOS UM MISS POR CONFLITO
					QTD_MISSES += 1
					QTD_MISSES_CONFLITO += 1
		memory.print_cache()

	#CACHE DO TIPO A4

	elif modo_cache == "A4":#CACHE DIRECT-MAPPING WITH 8 WORDS/BLOCK
		#PRIMEIRO PASSO: INICIALIZAR A CACHE
		memory = ch.Cache("A4")
		#SEGUNDO PASSO, HORA DE CALCULAR OS HITS E OS MISSES....
		for num_address, mode in lista_de_enderecos:
			#CALCULA O ENDERECO PRIMEIRO. NO CASO TEM QUE CALCULAR O INDEX:
			binary_address = np.binary_repr(num_address, 32)
			sentence = f"Binary Address: {binary_address} ---- Decimal Address: {num_address}"
			#MASSA, JA PASSEI O ENDERECO PARA BINARIO. HORA DE INSERIR NA CACHE...
			if mode == 'w':
				#MODO ESCRITA: SO TEM QUE JOGAR NA CACHE
				memory.write_cache(num_address, binary_address, "A4")
			elif mode == 'r':
				hit_miss = memory.read_cache(num_address, binary_address, "A4")
				if hit_miss == 1: #TIVEMOS UM HIT
					QTD_HITS += 1
				elif hit_miss == 2: #TIVEMOS UM MISS COMPULSORIO
					QTD_MISSES += 1
					QTD_MISSES_COMPULSORIOS += 1
				elif hit_miss == 3: #TIVEMOS UM MISS POR CONFLITO
					QTD_MISSES += 1
					QTD_MISSES_CONFLITO += 1
		memory.print_cache()

	#CACHE DO TIPO B1

	'''elif modo_cache == "B1":#CACHE TWO-WAY SET ASSOCIATIVE WITH 1 WORDS/BLOCK
		pass
	elif modo_cache == "B2":#CACHE TWO-WAY SET ASSOCIATIVE WITH 2 WORDS/BLOCK
		pass
	elif modo_cache == "B3":#CACHE TWO-WAY SET ASSOCIATIVE WITH 4 WORDS/BLOCK
		pass
	elif modo_cache == "B4":#CACHE TWO-WAY SET ASSOCIATIVE WITH 8 WORDS/BLOCK
		pass
	elif modo_cache == "C1":#CACHE FOUR-WAY SET ASSOCIATIVE WITH 1 WORDS/BLOCK
		pass
	elif modo_cache == "C2":#CACHE FOUR-WAY SET ASSOCIATIVE WITH 2 WORDS/BLOCK
		pass
	elif modo_cache == "C3":#CACHE FOUR-WAY SET ASSOCIATIVE WITH 4 WORDS/BLOCK
		pass
	elif modo_cache == "C4":#CACHE FOUR-WAY SET ASSOCIATIVE WITH 8 WORDS/BLOCK
		pass
	elif modo_cache == "D1":#CACHE EIGHT-WAY SET ASSOCIATIVE WITH 1 WORDS/BLOCK
		pass
	elif modo_cache == "D2":#CACHE EIGHT-WAY SET ASSOCIATIVE WITH 2 WORDS/BLOCK
		pass
	elif modo_cache == "D3":#CACHE EIGHT-WAY SET ASSOCIATIVE WITH 4 WORDS/BLOCK
		pass
	elif modo_cache == "D4":#CACHE EIGHT-WAY SET ASSOCIATIVE WITH 8 WORDS/BLOCK
		pass
	else:
		print("O modo de cache inserido nao eh valido.")'''


if __name__ == "__main__":
	main()
