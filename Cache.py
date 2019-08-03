import numpy as np 

class Block():
	def __init__(self, tipo): #Mesmo esquema: A1. A2. A3. A4. B1,...., E4
		#BLOCK WITH 1 WORD PER BLOCK
		if tipo == 'A1':
			self.index_binary = None
			self.valid_bit = 0
			self.tag_dec = None
			self.tag_bin = None
			self.tag_hex = None
			self.word1 = None
		#BLOCK WITH 2 WORDS PER BLOCK
		elif tipo == 'A2':
			self.index_binary = None
			self.valid_bit = 0
			self.tag_dec = None
			self.tag_bin = None
			self.tag_hex = None
			self.word1 = None
			self.word2 = None
		#BLOCK WITH 4 WORDS PER BLOCK
		elif tipo == 'A3':
			self.index_binary = None
			self.valid_bit = 0
			self.tag_dec = None
			self.tag_bin = None
			self.tag_hex = None
			self.word1 = None
			self.word2 = None
			self.word3 = None
			self.word4 = None
		#BLOCK WITH 8 WORDS PER BLOCK
		elif tipo == 'A4':
			self.index_binary = None
			self.valid_bit = 0
			self.tag_dec = None
			self.tag_bin = None
			self.tag_hex = None
			self.word1 = None
			self.word2 = None
			self.word3 = None
			self.word4 = None
			self.word5 = None
			self.word6 = None
			self.word7 = None
			self.word8 = None


class Set:
	def __init__(self, tipo):
		if tipo == 'B1':
			#TWO-WAY ASSOCIATIVE: 1 WORD/BLOCK
			self.fifo = []
			self.livre = 0
			self.bloco1 = Block('A1')
			self.bloco2 = Block('A1')
		elif tipo == 'B2':
			#TWO-WAY ASSOCIATIVE: 2 WORDS/BLOCK
			self.fifo = []
			self.livre = 0
			self.bloco1 = Block('A2')
			self.bloco2 = Block('A2')
		elif tipo == 'B3':
			#TWO-WAY ASSOCIATIVE: 4 WORDS/BLOCK
			self.fifo = []
			self.livre = 0
			self.bloco1 = Block('A3')
			self.bloco2 = Block('A3')
		elif tipo == 'B4':
			#TWO-WAY ASSOCIATIVE: 8 WORDS/BLOCK
			self.fifo = []
			self.livre = 0
			self.bloco1 = Block('A4')
			self.bloco2 = Block('A4')
		elif tipo == 'C1':
			#FOUR-WAY ASSOCIATIVE: 1 WORD/BLOCK
			self.fifo = []
			self.livre = 0
			self.bloco1 = Block('A1')
			self.bloco2 = Block('A1')
			self.bloco3 = Block('A1')
			self.bloco4 = Block('A1')
		elif tipo == 'C2':
			#FOUR-WAY ASSOCIATIVE: 2 WORDS/BLOCK
			self.fifo = []
			self.livre = 0
			self.bloco1 = Block('A2')
			self.bloco2 = Block('A2')
			self.bloco3 = Block('A2')
			self.bloco4 = Block('A2')
		elif tipo == 'C3':
			#FOUR-WAY ASSOCIATIVE: 4 WORDS/BLOCK
			self.fifo = []
			self.livre = 0
			self.bloco1 = Block('A3')
			self.bloco2 = Block('A3')
			self.bloco3 = Block('A3')
			self.bloco4 = Block('A3')
		elif tipo == 'C4':
			#FOUR-WAY ASSOCIATIVE: 8 WORDS/BLOCK
			self.fifo = []
			self.livre = 0
			self.bloco1 = Block('A4')
			self.bloco2 = Block('A4')
			self.bloco3 = Block('A4')
			self.bloco4 = Block('A4')
		elif tipo == 'D1':
			#FULLY ASSOCIATIVE: VAI TER QUE SER DE OUTRO JEITO...
		elif tipo == 'D2':
			#FULLY ASSOCIATIVE: VAI TER QUE SER DE OUTRO JEITO...
		elif tipo == 'D3':
			#FULLY ASSOCIATIVE: VAI TER QUE SER DE OUTRO JEITO...
		elif tipo == 'D4':
			#FULLY ASSOCIATIVE: VAI TER QUE SER DE OUTRO JEITO...
		
	


class Cache:
	def __init__(self, tipo): #Esse metodo inicial eh responsavel por realizar a inicializacao da cache.
		#Cache Direct-Mapping: 1 word/block
		if tipo == 'A1':
			self.tipo = 'A1'
			self.numero_indices = 1024 #range (0 ate 1023)
			self.numero_sets = None
			self.table = []
			for element in range(0, 1024):
				bloco = Block("A1")
				self.table.append(bloco)
		#Cache Direct-Mapping: 2 words/block
		elif tipo == 'A2':
			self.tipo = 'A2'
			self.numero_indices = 512  #range(0 a 511)
			self.numero_sets = None
			self.table = []
			for element in range(0, 512):
				bloco = Block("A2")
				self.table.append(bloco)
		#Cache Direct-Mapping: 4 words/block
		elif tipo == 'A3':
			self.tipo = 'A3'
			self.numero_indices = 256  #range(0 a 255)
			self.numero_sets = None
			self.table = []
			for element in range(0, 256):
				bloco = Block("A3")
				self.table.append(bloco)
		#Cache Direct-Mapping: 8 words/block
		elif tipo == 'A4':
			self.tipo = 'A4'
			self.numero_indices = 128  #range(0 a 127)
			self.numero_sets = None
			self.table = []
			for element in range(0, 128):
				bloco = Block("A4")
				self.table.append(bloco)
		#Two-Way Set Associative: 1 word per block
		elif tipo == 'B1':
			self.tipo = 'B1'
			self.numero_indices = None
			self.numero_sets = 512
			self.table = []
			for element in range(0, 512):
				novo_set = Set('B1')
				self.table.append(novo_set)
		#Two-Way Set Associative: 2 words per block
		elif tipo == 'B2':
			self.tipo = 'B2'
			self.numero_indices = None
			self.numero_sets = 256
			self.table = []
			for element in range(0, 256):
				novo_set = Set('B2')
				self.table.append(novo_set)
		#Two-Way Set Associative: 4 words per block
		elif tipo == 'B3':
			self.tipo = 'B3'
			self.numero_indices = None
			self.numero_sets = 128
			self.table = []
			for element in range(0, 128):
				novo_set = Set('B3')
				self.table.append(novo_set)
		#Two-Way Set Associative: 8 words per block
		elif tipo == 'B4':
			self.tipo = 'B4'
			self.numero_indices = None
			self.numero_sets = 64
			self.table = []
			for element in range(0. 64):
				novo_set = Set('B4')
				self.table.append(novo_set)
		#Four-Way Set Associaive: 1 word per block
		elif tipo == 'C1':
			self.tipo = 'C1'
			self.numero_indices = None
			self.numero_sets = 256
			self.table = []
			for element in range(0, 256):
				novo_set = Set('C1')
				self.table.append(novo_set)
		#Four-Way Set Associative: 2 words per block
		elif tipo == 'C2':
			self.tipo = 'C2'
			self.numero_indices = None
			self.numero_sets = 128
			self.table = []
			for element in range(0, 128):
				novo_set = Set('C2')
				self.table.append(novo_set)
		#Four-Way Set Associative: 4 words per block
		elif tipo == 'C3':
			self.tipo = 'C3'
			self.numero_indices = None
			self.numero_sets = 64
			self.table = []
			for element in range(0, 64):
				novo_set = Set('C3')
				self.table.append(novo_set)
		#Four-Way Set Associative: 8 words per block
		elif tipo == 'C4':
			self.tipo = 'C4'
			self.numero_indices = None
			self.numero_sets = 32
			self.table = []
			for element in range(0, 32):
				novo_set = Set('C4')
				self.table.append(novo_set)
		#AQUI AS COISAS DA IMPLEMENTACAO MUDARAM UM POUCO... PELO MENOS EM RELACAO AOS OUTROS SET ASSOCIATIVE
		#Fully Associative: 1 word per block
		elif tipo == 'D1':
			self.tipo = 'D1'
			self.numero_indices = 1024
			self.numero_sets = 1
			self.table = []
			self.free = 0
			for element in range(0, 1024):
				bloco = Block("A1")
				self.table.append(bloco)
		#Fully Associative: 2 words per block
		elif tipo == 'D2':
			self.tipo = 'D2'
			self.numero_indices =  512
			self.numero_sets = 1
			self.table = []
			self.free = 0
			for element in range(0, 512):
				bloco = Block("A2")
				self.table.append(bloco)
		#Fully Associative: 4 words per block
		elif tipo == 'D3':
			self.tipo = 'D3'
			self.numero_indices = 256
			self.numero_sets = 1
			self.table = []
			self.free = 0
			for element in range(0, 256):
				bloco = Block("A3")
				self.table.append(bloco)
		#Fully Associative: 8 words per block
		elif tipo == 'D4':
			self.tipo = 'D4'
			self.numero_indices = 128
			self.numero_sets = 1
			self.table = []
			self.free = 0
			for element in range(0, 128):
				bloco = Bloco("A4")
				self.table.append(bloco)

	def print_cache(self):
		if self.tipo == 'A1':
			for i in range (0, 1024):
				sentence = f"Index: {i:04} ---- Valid Bit: {self.table[i].valid_bit} ---- Tag: {self.table[i].tag_bin} ---- Data: {self.table[i].word1}"
				print(sentence)
		elif self.tipo == 'A2':
			for i in range(0, 512):
				sentence = f"Index: {i:03} ---- Valid Bit: {self.table[i].valid_bit} ---- Tag: {self.table[i].tag_bin} ---- Word1: {self.table[i].word1} ---- Word2: {self.table[i].word2}"
				print(sentence)
		elif self.tipo == 'A3':
			for i in range(0, 256):
				sentence = f"Index: {i:03} ---- Valid Bit: {self.table[i].valid_bit} ---- Tag: {self.table[i].tag_bin} ---- Word1: {self.table[i].word1} ---- Word2: {self.table[i].word2}"
				print(sentence)
				sentence2 = f"                                                 Word3: {self.table[i].word3} ---- Word4: {self.table[i].word4}"
				print(sentence2)
				print(" ")
		elif self.tipo == 'A4':
			for i in range(0, 128):
				sentence = f"Index: {i:03} ---- Valid Bit: {self.table[i].valid_bit} ---- Tag: {self.table[i].tag_bin} ---- Word1: {self.table[i].word1} ---- Word2: {self.table[i].word2}"
				print(sentence)
				sentence2 = f"                                                 Word3: {self.table[i].word3} ---- Word4: {self.table[i].word4}"
				print(sentence2)
				sentence2 = f"                                                 Word5: {self.table[i].word5} ---- Word6: {self.table[i].word6}"
				print(sentence2)
				sentence2 = f"                                                 Word7: {self.table[i].word7} ---- Word8: {self.table[i].word8}"
				print(sentence2)
				print(" ")
		else:
			print("Boy, isso ainda nao foi implementado. Segura ai! XD")

	def write_cache(self, num_address, binary_address, tipo_cache):
		if tipo_cache == 'A1':
			#######################################
			##  CONFIGURACAO DO ENDERECO 32 BITS ##
			##    TAG                    INDEX   ##   
			##  22 BITS                 1O BITS  ##
			#######################################
			i = int(binary_address[22:], 2)
			print(f"i: {i} ---- index_binary: {binary_address[22:]} --- full binary address: {binary_address}")
			self.table[i].index_binary = binary_address[22:]
			self.table[i].tag_bin = binary_address[0:22]
			self.table[i].word1 = int(num_address)
			self.table[i].valid_bit = 1;
		elif tipo_cache == 'A2':
			#######################################
			##  CONFIGURACAO DO ENDERECO 32 BITS ##
			##    TAG       INDEX   BLOCK OFFSET ##   
			##  22 BITS    O9 BITS     01 BIT    ##
			#######################################
			i = int(binary_address[22:31],2) #INDEX
			print(f"i: {i} ---- index_binary: {binary_address[22:31]} --- full binary address: {binary_address}")
			self.table[i].index_binary = binary_address[22:31]
			self.table[i].tag_bin = binary_address[0:22]
			self.table[i].valid_bit = 1
			self.table[i].block_offset = binary_address[-1]
			if num_address % 2 == 0:
				self.table[i].word1 = num_address
				self.table[i].word2 = None
			elif num_address % 2 == 1:
				self.table[i].word1 = None
				self.table[i].word2 = num_address
		elif tipo_cache == 'A3':
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                INDEX         BLOCK OFFSET ##   
			##  22 BITS             O8 BITS           02 BIT    ##
			######################################################
			i = int(binary_address[22:30],2) #INDEX
			print(f"i: {i} ---- index_binary: {binary_address[22:30]} --- full binary address: {binary_address}")
			self.table[i].index_binary = binary_address[22:30]
			self.table[i].tag_bin = binary_address[0:22]
			self.table[i].valid_bit = 1
			self.table[i].block_offset = binary_address[-2:]
			if num_address % 4 == 0:
				self.table[i].word1 = num_address
				self.table[i].word2 = None
				self.table[i].word3 = None
				self.table[i].word4 = None
			elif num_address % 4 == 1:
				self.table[i].word1 = None
				self.table[i].word2 = num_address
				self.table[i].word3 = None
				self.table[i].word4 = None
			elif num_address % 4 == 2:
				self.table[i].word1 = None
				self.table[i].word2 = None
				self.table[i].word3 = num_address
				self.table[i].word4 = None
			elif num_address % 4 == 3:
				self.table[i].word1 = None
				self.table[i].word2 = None
				self.table[i].word3 = None
				self.table[i].word4 = num_address
		elif tipo_cache == 'A4':
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                INDEX         BLOCK OFFSET ##   
			##  22 BITS             O7 BITS           03 BIT    ##
			######################################################
			i = int(binary_address[22:29],2) #INDEX
			print(f"i: {i} ---- index_binary: {binary_address[22:29]} --- full binary address: {binary_address}")
			self.table[i].index_binary = binary_address[22:29]
			self.table[i].tag_bin = binary_address[0:22]
			self.table[i].valid_bit = 1
			self.table[i].block_offset = binary_address[-3:]
			if num_address % 8 == 0:
				self.table[i].word1 = num_address
				self.table[i].word2 = None
				self.table[i].word3 = None
				self.table[i].word4 = None
				self.table[i].word5 = None
				self.table[i].word6 = None
				self.table[i].word7 = None
				self.table[i].word8 = None
			elif num_address % 8 == 1:
				self.table[i].word1 = None
				self.table[i].word2 = num_address
				self.table[i].word3 = None
				self.table[i].word4 = None
				self.table[i].word5 = None
				self.table[i].word6 = None
				self.table[i].word7 = None
				self.table[i].word8 = None
			elif num_address % 8 == 2:
				self.table[i].word1 = None
				self.table[i].word2 = None
				self.table[i].word3 = num_address
				self.table[i].word4 = None
				self.table[i].word5 = None
				self.table[i].word6 = None
				self.table[i].word7 = None
				self.table[i].word8 = None
			elif num_address % 8 == 3:
				self.table[i].word1 = None
				self.table[i].word2 = None
				self.table[i].word3 = None
				self.table[i].word4 = num_address
				self.table[i].word5 = None
				self.table[i].word6 = None
				self.table[i].word7 = None
				self.table[i].word8 = None
			elif num_address % 8 == 4:
				self.table[i].word1 = None
				self.table[i].word2 = None
				self.table[i].word3 = None
				self.table[i].word4 = None
				self.table[i].word5 = num_address
				self.table[i].word6 = None
				self.table[i].word7 = None
				self.table[i].word8 = None
			elif num_address % 8 == 5:
				self.table[i].word1 = None
				self.table[i].word2 = None
				self.table[i].word3 = None
				self.table[i].word4 = None
				self.table[i].word5 = None
				self.table[i].word6 = num_address
				self.table[i].word7 = None
				self.table[i].word8 = None
			elif num_address % 8 == 6:
				self.table[i].word1 = None
				self.table[i].word2 = None
				self.table[i].word3 = None
				self.table[i].word4 = None
				self.table[i].word5 = None
				self.table[i].word6 = None
				self.table[i].word7 = num_address
				self.table[i].word8 = None
			elif num_address % 8 == 7:
				self.table[i].word1 = None
				self.table[i].word2 = None
				self.table[i].word3 = None
				self.table[i].word4 = None
				self.table[i].word5 = None
				self.table[i].word6 = None
				self.table[i].word7 = None
				self.table[i].word8 = num_address
		elif tipo_cache == 'B1':
			#TWO-WAY SET ASSOCIATIVE: 1 WORD/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                 SET           SET OFFSET  ##   
			##  22 BITS             O9 BITS           01 BIT    ##
			######################################################
			'''def write_cache(self, num_address, binary_address, tipo_cache):'''
			i = int(binary_address[22:31], 2) #SET NO FORMATO DECIMAL
			tag_dada_bin = binary_address[0:22] #pegando a tag que foi dada
			dado = int(num_address) #dado a ser escrito na forma decimal
			set_offset = binary_address[-1] #bit que indica o set offset
			if self.table[i].livre == 0: #SE TODOS OS BLOCOS DAQUELE SET TAVAM LIVRES... EU COMECO ESCREVENDO PELO PRIMEIRO BLOCO....
				self.table[i].bloco1.word1 = dado
				self.table[i].bloco1.tag_bin  = tag_dada_bin
				self.table[i].bloco1.valid_bit = 1
				self.table[i].livre += 1
				self.table[i].fifo.append(1)
			elif self.table[i].livre == 1:#SE O PRIMEIRO BLOCO DAQUELE SET TAVA OCUPADO... EU COMECO ESCREVENDO PELO SEGUNDO BLOCO....
				self.table[i].bloco2.word1 = dado
				self.table[i].bloco2.tag_bin = tag_dada_bin
				self.table[i].bloco2.valid_bit = 1
				self.table[i].livre += 1				
				self.table[i].fifo.append(2)
			elif self.table[i].livre  >= 2: #se TODOS OS BLOCOS DAQUELE SET ESTAVAM OCUPADOS EU PEGO O QUE FOI USADO HA MAIS TEMPO DE ACORDO COM A FIFO....
				usado_ha_mais_tempo = self.table[i].fifo[0]
				self.table[i].fifo.pop(0)
				if usado_ha_mais_tempo == 1: #TEM QUE SOBRESCREVER O BLOCO 1
					self.table[i].bloco1.word1 = dado
					self.table[i].bloco1.tag_bin  = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].fifo.append(1)
				elif usado_ha_mais_tempo == 2: #TEM QUE SOBRESCREVER O BLOCO 2
					self.table[i].bloco2.word1 = dado
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1				
					self.table[i].fifo.append(2)
		elif tipo_cache == 'B2':
			#TWO-WAY SET ASSOCIATIVE: 2 WORDs/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                 SET           SET OFFSET  ##   
			##  22 BITS             O8 BITS          02 BITS    ##
			######################################################
			'''def write_cache(self, num_address, binary_address, tipo_cache):'''
			i = int(binary_address[22:30], 2) #SET NO FORMATO DECIMAL
			tag_dada_bin = binary_address[0:22]
			dado = int(num_address)
			set_offset = binary_address[-2:]
			if self.table[i].livre == 0: #COMECA ESCREVENDO NO PRIMEIRO BLOCO
				if num_address % 2 == 0:
					#DADO VAI PARA WORD1
					self.table[i].bloco1.word1 = dado
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif num_address % 2 == 1:
					#DADO VAI PARA WORD2
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = dado
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
			elif self.table[i].livre == 1: #ESCREVE NO SEGUNDO BLOCO
				if num_address % 2 == 0:
					#DADO VAI PARA WORD1
					self.table[i].bloco2.word1 = dado
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(2)
				elif num_address % 2 == 1:
					#DADO VAI PARA WORD2
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = dado
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(2)
			elif self.table[i].livre >= 2: #ESCREVE NO BLOCO QUE FOI USADO HA MAIS TEMPO
				usado_ha_mais_tempo = self.table[i].fifo[0]
				self.table[i].fifo.pop(0)
				if usado_ha_mais_tempo == 1: #TEM QUE SOBRESCREVER O BLOCO 1
					if num_address % 2 == 0:
						#DADO VAI PARA WORD1
						self.table[i].bloco1.word1 = dado
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].fifo.append(1)
					elif num_address % 2 == 1:
						#DADO VAI PARA WORD2
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = dado
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].fifo.append(1)
				elif usado_ha_mais_tempo == 2: #TEM QUE SOBRESCREVER O BLOCO 2
					if num_address % 2 == 0:
						#DADO VAI PARA WORD1
						self.table[i].bloco2.word1 = dado
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].fifo.append(2)
					elif num_address % 2 == 1:
						#DADO VAI PARA WORD2
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = dado
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].fifo.append(2)
		elif tipo_cache == 'B3':
			#TWO-WAY SET ASSOCIATIVE: 4 WORDs/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                 SET           SET OFFSET  ##   
			##  22 BITS             O7 BITS          03 BITS    ##
			######################################################
			'''def write_cache(self, num_address, binary_address, tipo_cache):'''
			i = int(binary_address[22:29], 2)
			tag_dada_bin = binary_address[0:22]
			dado = int(num_address)
			set_offset = binary_address[-3:]
			if self.table[i].livre == 0: #COMECA ESCREVENDO NO PRIMEIRO BLOCO
				if num_address % 4 == 0:
					#DADO VAI PARA WORD1
					self.table[i].bloco1.word1 = dado
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif num_address % 4 == 1:
					#DADO VAI PARA WORD2
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = dado
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif num_address % 4== 2:
					#DADO VAI PARA WORD3
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = dado
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif num_address % 4 == 3:
					#DADO VAI PARA WORD4
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = dado
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
			elif self.table[i].livre == 1:#COMECA ESCREVENDO NO SEGUNDO BLOCO
				if num_address % 4 == 0:
					#DADO VAI PARA WORD1
					self.table[i].bloco2.word1 = dado
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(2)
				elif num_address % 4 == 1:
					#DADO VAI PARA WORD2
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = dado
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(2)
				elif num_address % 4 == 2:
					#DADO VAI PARA WORD3
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = dado
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(2)
				elif num_address % 4 == 3:
					#DADO VAI PARA WORD4
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = dado
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(2)
			elif self.table[i].livre >= 2:#ESCREVE NO BLOCO QUE FOI USADO HA MAIS TEMPO
				usado_ha_mais_tempo = self.table[i].fifo[0]
				self.table[i].fifo.pop(0)
				if usado_ha_mais_tempo == 1: #TEM QUE SOBRESCREVER O BLOCO 1
					if num_address % 4 == 0:
					#DADO VAI PARA WORD1
						self.table[i].bloco1.word1 = dado
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif num_address % 4 == 1:
						#DADO VAI PARA WORD2
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = dado
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif num_address % 4== 2:
						#DADO VAI PARA WORD3
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = dado
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif num_address % 4 == 3:
						#DADO VAI PARA WORD4
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = dado
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
				elif usado_ha_mais_tempo == 2: #TEM QUE SOBRESCREVER O BLOCO 2
					if num_address % 4 == 0:
						#DADO VAI PARA WORD1
						self.table[i].bloco2.word1 = dado
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif num_address % 4 == 1:
						#DADO VAI PARA WORD2
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = dado
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif num_address % 4 == 2:
						#DADO VAI PARA WORD3
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = dado
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif num_address % 4 == 3:
						#DADO VAI PARA WORD4
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = dado
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
		elif tipo_cache == 'B4':
			#TWO-WAY SET ASSOCIATIVE: 8 WORDs/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                 SET           SET OFFSET  ##   
			##  22 BITS             O6 BITS          04 BITS    ##
			######################################################
			'''def write_cache(self, num_address, binary_address, tipo_cache):'''
			i = int(binary_address[22:28], 2)
			tag_dada_bin = binary_address[0:22]
			dado = int(num_address)
			set_offset = binary_address[-4:]
			if self.table[i].livre == 0 #O PRIMEIRO BLOCO DESSE SET TA LIVRE
				if num_address % 8 == 0:
					#DADO VAI PARA WORD1
					self.table[i].bloco1.word1 = dado
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.word5 = None
					self.table[i].bloco1.word6 = None
					self.table[i].bloco1.word7 = None
					self.table[i].bloco1.word8 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif num_address % 8 == 1:
					#DADO VAI PARA WORD2
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = dado
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.word5 = None
					self.table[i].bloco1.word6 = None
					self.table[i].bloco1.word7 = None
					self.table[i].bloco1.word8 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif num_address % 8== 2:
					#DADO VAI PARA WORD3
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = dado
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.word5 = None
					self.table[i].bloco1.word6 = None
					self.table[i].bloco1.word7 = None
					self.table[i].bloco1.word8 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif num_address % 8 == 3:
					#DADO VAI PARA WORD4
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = dado
					self.table[i].bloco1.word5 = None
					self.table[i].bloco1.word6 = None
					self.table[i].bloco1.word7 = None
					self.table[i].bloco1.word8 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif num_address % 8 == 4:
					#DADO VAI PARA WORD5
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.word5 = dado
					self.table[i].bloco1.word6 = None
					self.table[i].bloco1.word7 = None
					self.table[i].bloco1.word8 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif num_address % 8 == 5:
					#DADO VAI PARA WORD6
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.word5 = None
					self.table[i].bloco1.word6 = dado
					self.table[i].bloco1.word7 = None
					self.table[i].bloco1.word8 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif num_address % 8 == 6:
					#DADO VAI PARA WORD7
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.word5 = None
					self.table[i].bloco1.word6 = None
					self.table[i].bloco1.word7 = dado
					self.table[i].bloco1.word8 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif num_address % 8 == 7:
					#DADO VAI PARA WORD8
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.word5 = None
					self.table[i].bloco1.word6 = None
					self.table[i].bloco1.word7 = None
					self.table[i].bloco1.word8 = dado
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
			elif self.table[i].livre == 1: #TEM QUE JOGAR NO SEGUNDO BLOCO AGR...
				if num_address % 8 == 0:
					#DADO VAI PARA WORD1
					self.table[i].bloco2.word1 = dado
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.word5 = None
					self.table[i].bloco2.word6 = None
					self.table[i].bloco2.word7 = None
					self.table[i].bloco2.word8 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(2)
				elif num_address % 8 == 1:
					#DADO VAI PARA WORD2
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = dado
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.word5 = None
					self.table[i].bloco2.word6 = None
					self.table[i].bloco2.word7 = None
					self.table[i].bloco2.word8 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(2)
				elif num_address % 8== 2:
					#DADO VAI PARA WORD3
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = dado
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.word5 = None
					self.table[i].bloco2.word6 = None
					self.table[i].bloco2.word7 = None
					self.table[i].bloco2.word8 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(2)
				elif num_address % 8 == 3:
					#DADO VAI PARA WORD4
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = dado
					self.table[i].bloco2.word5 = None
					self.table[i].bloco2.word6 = None
					self.table[i].bloco2.word7 = None
					self.table[i].bloco2.word8 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(2)
				elif num_address % 8 == 4:
					#DADO VAI PARA WORD5
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.word5 = dado
					self.table[i].bloco2.word6 = None
					self.table[i].bloco2.word7 = None
					self.table[i].bloco2.word8 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(2)
				elif num_address % 8 == 5:
					#DADO VAI PARA WORD6
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.word5 = None
					self.table[i].bloco2.word6 = dado
					self.table[i].bloco2.word7 = None
					self.table[i].bloco2.word8 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(2)
				elif num_address % 8 == 6:
					#DADO VAI PARA WORD7
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.word5 = None
					self.table[i].bloco2.word6 = None
					self.table[i].bloco2.word7 = dado
					self.table[i].bloco2.word8 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(2)
				elif num_address % 8 == 7:
					#DADO VAI PARA WORD8
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.word5 = None
					self.table[i].bloco2.word6 = None
					self.table[i].bloco2.word7 = None
					self.table[i].bloco2.word8 = dado
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(2)
			elif self.table[i].livre >= 2: #OS DOIS BLOCOS TAO CHEIOS.... TEM QUE USAR UM DOS DOIS...
				usado_ha_mais_tempo = self.table[i].fifo[0]
				self.table[i].fifo.pop(0)
				if usado_ha_mais_tempo == 1: #TEM QUE SOBRESCREVER O BLOCO 1
					if num_address % 8 == 0:
						#DADO VAI PARA WORD1
						self.table[i].bloco1.word1 = dado
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.word5 = None
						self.table[i].bloco1.word6 = None
						self.table[i].bloco1.word7 = None
						self.table[i].bloco1.word8 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif num_address % 8 == 1:
						#DADO VAI PARA WORD2
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = dado
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.word5 = None
						self.table[i].bloco1.word6 = None
						self.table[i].bloco1.word7 = None
						self.table[i].bloco1.word8 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif num_address % 8== 2:
						#DADO VAI PARA WORD3
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = dado
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.word5 = None
						self.table[i].bloco1.word6 = None
						self.table[i].bloco1.word7 = None
						self.table[i].bloco1.word8 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif num_address % 8 == 3:
						#DADO VAI PARA WORD4
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = dado
						self.table[i].bloco1.word5 = None
						self.table[i].bloco1.word6 = None
						self.table[i].bloco1.word7 = None
						self.table[i].bloco1.word8 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif num_address % 8 == 4:
						#DADO VAI PARA WORD5
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.word5 = dado
						self.table[i].bloco1.word6 = None
						self.table[i].bloco1.word7 = None
						self.table[i].bloco1.word8 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif num_address % 8 == 5:
						#DADO VAI PARA WORD6
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.word5 = None
						self.table[i].bloco1.word6 = dado
						self.table[i].bloco1.word7 = None
						self.table[i].bloco1.word8 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif num_address % 8 == 6:
						#DADO VAI PARA WORD7
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.word5 = None
						self.table[i].bloco1.word6 = None
						self.table[i].bloco1.word7 = dado
						self.table[i].bloco1.word8 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif num_address % 8 == 7:
						#DADO VAI PARA WORD8
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.word5 = None
						self.table[i].bloco1.word6 = None
						self.table[i].bloco1.word7 = None
						self.table[i].bloco1.word8 = dado
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
				elif usado_ha_mais_tempo == 2: #TEM QUE SOBRESCREVER O BLOCO 2
					if num_address % 8 == 0:
						#DADO VAI PARA WORD1
						self.table[i].bloco2.word1 = dado
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.word5 = None
						self.table[i].bloco2.word6 = None
						self.table[i].bloco2.word7 = None
						self.table[i].bloco2.word8 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif num_address % 8 == 1:
						#DADO VAI PARA WORD2
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = dado
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.word5 = None
						self.table[i].bloco2.word6 = None
						self.table[i].bloco2.word7 = None
						self.table[i].bloco2.word8 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif num_address % 8== 2:
						#DADO VAI PARA WORD3
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = dado
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.word5 = None
						self.table[i].bloco2.word6 = None
						self.table[i].bloco2.word7 = None
						self.table[i].bloco2.word8 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif num_address % 8 == 3:
						#DADO VAI PARA WORD4
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = dado
						self.table[i].bloco2.word5 = None
						self.table[i].bloco2.word6 = None
						self.table[i].bloco2.word7 = None
						self.table[i].bloco2.word8 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif num_address % 8 == 4:
						#DADO VAI PARA WORD5
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.word5 = dado
						self.table[i].bloco2.word6 = None
						self.table[i].bloco2.word7 = None
						self.table[i].bloco2.word8 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif num_address % 8 == 5:
						#DADO VAI PARA WORD6
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.word5 = None
						self.table[i].bloco2.word6 = dado
						self.table[i].bloco2.word7 = None
						self.table[i].bloco2.word8 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif num_address % 8 == 6:
						#DADO VAI PARA WORD7
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.word5 = None
						self.table[i].bloco2.word6 = None
						self.table[i].bloco2.word7 = dado
						self.table[i].bloco2.word8 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif num_address % 8 == 7:
						#DADO VAI PARA WORD8
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.word5 = None
						self.table[i].bloco2.word6 = None
						self.table[i].bloco2.word7 = None
						self.table[i].bloco2.word8 = dado
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
		elif tipo_cache == 'C1':
			#FOUR-WAY SET ASSOCIATIVE WITH 1 WORD/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                 SET           SET OFFSET  ##   
			##  22 BITS             O8 BITS          02 BITS    ##
			######################################################
			i = int(binary_address[22:30], 2)
			tag_dada_bin = binary_address[0:22]
			dado = int(num_address)
			set_offset = binary_address[-2:]
			if self.table[i].livre == 0: #VAI PRO BLOCO 1
				self.table[i].bloco1.word1 = dado
				self.table[i].bloco1.tag_bin = tag_dada_bin
				self.table[i].bloco1.valid_bit = 1
				self.table[i].livre += 1
				self.table[i].fifo.append(1)
			elif self.table[i].livre == 1: #VAI PRO BLOCO 2
				self.table[i].bloco2.word1 = dado
				self.table[i].bloco2.tag_bin = tag_dada_bin
				self.table[i].bloco2.valid_bit = 1
				self.table[i].livre += 1
				self.table[i].fifo.append(2)
			elif self.table[i].livre == 2: #VAI PRO BLOCO 3
				self.table[i].bloco3.word1 = dado
				self.table[i].bloco3.tag_bin = tag_dada_bin
				self.table[i].bloco3.valid_bit = 1
				self.table[i].livre += 1
				self.table[i].fifo.append(3)
			elif self.table[i].livre == 3: #VAI PRO BLOCO 4
				self.table[i].bloco4.word1 = dado
				self.table[i].bloco4.tag_bin = tag_dada_bin
				self.table[i].bloco4.valid_bit = 1
				self.table[i].livre += 1
				self.table[i].fifo.append(4)
			elif self.table[i].livre >= 4: #TEM QUE CHECAR A FIFO PRA VER QUAL SERA SUBSTITUIDO.
				usado_ha_mais_tempo = self.table[i].fifo[0]
				self.table[i].fifo.pop(0)
				if usado_ha_mais_tempo == 1: #SOBRESCREVE BLOCO 1
					self.table[i].bloco1.word1 = dado
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif usado_ha_mais_tempo == 2: #SOBRESCREVE BLOCO 2
					self.table[i].bloco2.word1 = dado
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(2)
				elif usado_ha_mais_tempo == 3: #SOBRESCREVE BLOCO 3
					self.table[i].bloco3.word1 = dado
					self.table[i].bloco3.tag_bin = tag_dada_bin
					self.table[i].bloco3.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(3)
				elif usado_ha_mais_tempo == 4: #SOBRESCREVE BLOCO 4
					self.table[i].bloco4.word1 = dado
					self.table[i].bloco4.tag_bin = tag_dada_bin
					self.table[i].bloco4.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(4)
		elif tipo_cache == 'C2':
			#FOUR-WAY SET ASSOCIATIVE WITH 2 WORD/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                 SET           SET OFFSET  ##   
			##  22 BITS             O7 BITS          03 BITS    ##
			######################################################
			i = int(num_address[22:29], 2)
			tag_dada_bin = binary_address[0:22]
			dado = int(num_address)
			if self.table[i].livre == 0: #BLOCO 1
				if num_address % 2 == 0:############# word 1 ############
					self.table[i].bloco1.word1 = dado
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 2 == 1:############# word 2 ############
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = dado
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
				self.table[i].fifo.append(1)
			elif self.table[i].livre == 1: #BLOCO 2
				if num_address % 2 == 0:############# word 1 ############
					self.table[i].bloco2.word1 = dado
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 2 == 1:############# word 2 ############
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = dado
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
				self.table[i].fifo.append(2)
			elif self.table[i].livre == 2: #BLOCO 3
				if num_address % 2 == 0:############# word 1 ############
					self.table[i].bloco3.word1 = dado
					self.table[i].bloco3.word2 = None
					self.table[i].bloco3.tag_bin = tag_dada_bin
					self.table[i].bloco3.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 2 == 1:############# word 2 ############
					self.table[i].bloco3.word1 = None
					self.table[i].bloco3.word2 = dado
					self.table[i].bloco3.tag_bin = tag_dada_bin
					self.table[i].bloco3.valid_bit = 1
					self.table[i].livre += 1
				self.table[i].fifo.append(3)
			elif self.table[i].livre == 3: #BLOCO 4
				if num_address % 2 == 0:############# word 1 ############
					self.table[i].bloco4.word1 = dado
					self.table[i].bloco4.word2 = None
					self.table[i].bloco4.tag_bin = tag_dada_bin
					self.table[i].bloco4.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 2 == 1:############# word 2 ############
					self.table[i].bloco4.word1 = None
					self.table[i].bloco4.word2 = dado
					self.table[i].bloco4.tag_bin = tag_dada_bin
					self.table[i].bloco4.valid_bit = 1
					self.table[i].livre += 1
				self.table[i].fifo.append(4)
			elif self.table[i].livre >= 4: #CHECA O FIFO
				usado_ha_mais_tempo = self.table[i].fifo[0]
				self.table[i].fifo.pop(0)
				if usado_ha_mais_tempo == 1: #SOBRESCREVE O BLOCO 1
					if num_address % 2 == 0:############# word 1 ############
						self.table[i].bloco1.word1 = dado
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 2 == 1:############# word 2 ############
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = dado
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif usado_ha_mais_tempo == 2: #SOBRESCREVE O BLOCO 2
					if num_address % 2 == 0:############# word 1 ############
						self.table[i].bloco2.word1 = dado
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 2 == 1:############# word 2 ############
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = dado
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
					self.table[i].fifo.append(2)
				elif usado_ha_mais_tempo == 3: #SOBRESCREVE O BLOCO 3
					if num_address % 2 == 0:############# word 1 ############
						self.table[i].bloco3.word1 = dado
						self.table[i].bloco3.word2 = None
						self.table[i].bloco3.tag_bin = tag_dada_bin
						self.table[i].bloco3.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 2 == 1:############# word 2 ############
						self.table[i].bloco3.word1 = None
						self.table[i].bloco3.word2 = dado
						self.table[i].bloco3.tag_bin = tag_dada_bin
						self.table[i].bloco3.valid_bit = 1
						self.table[i].livre += 1
					self.table[i].fifo.append(3)
				elif usado_ha_mais_tempo == 4: #SOBRESCREVE O BLOCO 4
					if num_address % 2 == 0:############# word 1 ############
						self.table[i].bloco4.word1 = dado
						self.table[i].bloco4.word2 = None
						self.table[i].bloco4.tag_bin = tag_dada_bin
						self.table[i].bloco4.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 2 == 1:############# word 2 ############
						self.table[i].bloco4.word1 = None
						self.table[i].bloco4.word2 = dado
						self.table[i].bloco4.tag_bin = tag_dada_bin
						self.table[i].bloco4.valid_bit = 1
						self.table[i].livre += 1
					self.table[i].fifo.append(4)
		elif tipo_cache == 'C3':
			#FOUR-WAY SET ASSOCIATIVE WITH 4 WORD/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                 SET           SET OFFSET  ##   
			##  22 BITS             O6 BITS          04 BITS    ##
			######################################################
			i = num(binary_address[22:28], 2)
			tag_dada_bin = binary_address[0:22]
			dado = int(num_address)
			set_offset = binary_address[-4:]
			if self.table[i].livre == 0: #BLOCO 01
				if num_address % 4 == 0:############# word 1 ############
					self.table[i].bloco1.word1 = dado
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 4 == 1:############# word 2 ############
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = dado
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 4 == 2:############# word 3 ############
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = dado
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 4 == 3:############# word 4 ############
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = dado
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
				self.table[i].fifo.append(1)
			elif self.table[i].livre == 1: #BLOCO 02
				if num_address % 4 == 0:############# word 1 ############
					self.table[i].bloco2.word1 = dado
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 4 == 1:############# word 2 ############
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = dado
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 4 == 2:############# word 3 ############
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = dado
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 4 == 3:############# word 4 ############
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = dado
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
				self.table[i].fifo.append(2)
			elif self.table[i].livre == 2: #BLOCO 03
				if num_address % 4 == 0:############# word 1 ############
					self.table[i].bloco3.word1 = dado
					self.table[i].bloco3.word2 = None
					self.table[i].bloco3.word3 = None
					self.table[i].bloco3.word4 = None
					self.table[i].bloco3.tag_bin = tag_dada_bin
					self.table[i].bloco3.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 4 == 1:############# word 2 ############
					self.table[i].bloco3.word1 = None
					self.table[i].bloco3.word2 = dado
					self.table[i].bloco3.word3 = None
					self.table[i].bloco3.word4 = None
					self.table[i].bloco3.tag_bin = tag_dada_bin
					self.table[i].bloco3.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 4 == 2:############# word 3 ############
					self.table[i].bloco3.word1 = None
					self.table[i].bloco3.word2 = None
					self.table[i].bloco3.word3 = dado
					self.table[i].bloco3.word4 = None
					self.table[i].bloco3.tag_bin = tag_dada_bin
					self.table[i].bloco3.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 4 == 3:############# word 4 ############
					self.table[i].bloco3.word1 = None
					self.table[i].bloco3.word2 = None
					self.table[i].bloco3.word3 = None
					self.table[i].bloco3.word4 = dado
					self.table[i].bloco3.tag_bin = tag_dada_bin
					self.table[i].bloco3.valid_bit = 1
					self.table[i].livre += 1
				self.table[i].fifo.append(3)
			elif self.table[i].livre == 3: #BLOCO 04
				if num_address % 4 == 0:############# word 1 ############
					self.table[i].bloco4.word1 = dado
					self.table[i].bloco4.word2 = None
					self.table[i].bloco4.word3 = None
					self.table[i].bloco4.word4 = None
					self.table[i].bloco4.tag_bin = tag_dada_bin
					self.table[i].bloco4.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 4 == 1:############# word 2 ############
					self.table[i].bloco4.word1 = None
					self.table[i].bloco4.word2 = dado
					self.table[i].bloco4.word3 = None
					self.table[i].bloco4.word4 = None
					self.table[i].bloco4.tag_bin = tag_dada_bin
					self.table[i].bloco4.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 4 == 2:############# word 3 ############
					self.table[i].bloco4.word1 = None
					self.table[i].bloco4.word2 = None
					self.table[i].bloco4.word3 = dado
					self.table[i].bloco4.word4 = None
					self.table[i].bloco4.tag_bin = tag_dada_bin
					self.table[i].bloco4.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 4 == 3:############# word 4 ############
					self.table[i].bloco4.word1 = None
					self.table[i].bloco4.word2 = None
					self.table[i].bloco4.word3 = None
					self.table[i].bloco4.word4 = dado
					self.table[i].bloco4.tag_bin = tag_dada_bin
					self.table[i].bloco4.valid_bit = 1
					self.table[i].livre += 1
				self.table[i].fifo.append(4)
			elif self.table[i].livre >= 4: #TEM QUE ESCOLHER UM BLOCO PARA SUBSTITUIR...
				usado_ha_mais_tempo = self.table[i].fifo[0]
				self.table[i].fifo.pop(0)
				if usado_ha_mais_tempo == 1:
					if num_address % 4 == 0:############# word 1 ############
						self.table[i].bloco1.word1 = dado
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 4 == 1:############# word 2 ############
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = dado
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 4 == 2:############# word 3 ############
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = dado
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 4 == 3:############# word 4 ############
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = dado
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif usado_ha_mais_tempo == 2:
					if num_address % 4 == 0:############# word 1 ############
						self.table[i].bloco2.word1 = dado
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 4 == 1:############# word 2 ############
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = dado
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 4 == 2:############# word 3 ############
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = dado
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 4 == 3:############# word 4 ############
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = dado
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
					self.table[i].fifo.append(2)
				elif usado_ha_mais_tempo == 3:
					if num_address % 4 == 0:############# word 1 ############
						self.table[i].bloco3.word1 = dado
						self.table[i].bloco3.word2 = None
						self.table[i].bloco3.word3 = None
						self.table[i].bloco3.word4 = None
						self.table[i].bloco3.tag_bin = tag_dada_bin
						self.table[i].bloco3.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 4 == 1:############# word 2 ############
						self.table[i].bloco3.word1 = None
						self.table[i].bloco3.word2 = dado
						self.table[i].bloco3.word3 = None
						self.table[i].bloco3.word4 = None
						self.table[i].bloco3.tag_bin = tag_dada_bin
						self.table[i].bloco3.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 4 == 2:############# word 3 ############
						self.table[i].bloco3.word1 = None
						self.table[i].bloco3.word2 = None
						self.table[i].bloco3.word3 = dado
						self.table[i].bloco3.word4 = None
						self.table[i].bloco3.tag_bin = tag_dada_bin
						self.table[i].bloco3.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 4 == 3:############# word 4 ############
						self.table[i].bloco3.word1 = None
						self.table[i].bloco3.word2 = None
						self.table[i].bloco3.word3 = None
						self.table[i].bloco3.word4 = dado
						self.table[i].bloco3.tag_bin = tag_dada_bin
						self.table[i].bloco3.valid_bit = 1
						self.table[i].livre += 1
					self.table[i].fifo.append(3)
				elif usado_ha_mais_tempo == 4:
					if num_address % 4 == 0:############# word 1 ############
						self.table[i].bloco4.word1 = dado
						self.table[i].bloco4.word2 = None
						self.table[i].bloco4.word3 = None
						self.table[i].bloco4.word4 = None
						self.table[i].bloco4.tag_bin = tag_dada_bin
						self.table[i].bloco4.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 4 == 1:############# word 2 ############
						self.table[i].bloco4.word1 = None
						self.table[i].bloco4.word2 = dado
						self.table[i].bloco4.word3 = None
						self.table[i].bloco4.word4 = None
						self.table[i].bloco4.tag_bin = tag_dada_bin
						self.table[i].bloco4.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 4 == 2:############# word 3 ############
						self.table[i].bloco4.word1 = None
						self.table[i].bloco4.word2 = None
						self.table[i].bloco4.word3 = dado
						self.table[i].bloco4.word4 = None
						self.table[i].bloco4.tag_bin = tag_dada_bin
						self.table[i].bloco4.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 4 == 3:############# word 4 ############
						self.table[i].bloco4.word1 = None
						self.table[i].bloco4.word2 = None
						self.table[i].bloco4.word3 = None
						self.table[i].bloco4.word4 = dado
						self.table[i].bloco4.tag_bin = tag_dada_bin
						self.table[i].bloco4.valid_bit = 1
						self.table[i].livre += 1
					self.table[i].fifo.append(4)
		elif tipo_cache == 'C4':
			#FOUR-WAY SET ASSOCIATIVE WITH 8 WORD/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                 SET           SET OFFSET  ##   
			##  22 BITS             O5 BITS          05 BITS    ##
			######################################################
			i = int(binary_address[22:27], 2)
			tag_dada_bin = binary_address[0:22]
			dado = int(num_address)
			set_offset = binary_address[-5:]
			if self.table[i].livre == 0: #BLOCO 01
				if num_address % 8 == 0:############# word 1 ############
					self.table[i].bloco1.word1 = dado
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.word5 = None
					self.table[i].bloco1.word6 = None
					self.table[i].bloco1.word7 = None
					self.table[i].bloco1.word8 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 1:############# word 2 ############
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = dado
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.word5 = None
					self.table[i].bloco1.word6 = None
					self.table[i].bloco1.word7 = None
					self.table[i].bloco1.word8 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 2:############# word 3 ############
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = dado
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.word5 = None
					self.table[i].bloco1.word6 = None
					self.table[i].bloco1.word7 = None
					self.table[i].bloco1.word8 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 3:############# word 4 ############
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = dado
					self.table[i].bloco1.word5 = None
					self.table[i].bloco1.word6 = None
					self.table[i].bloco1.word7 = None
					self.table[i].bloco1.word8 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 4:############# word 5 ############
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.word5 = dado
					self.table[i].bloco1.word6 = None
					self.table[i].bloco1.word7 = None
					self.table[i].bloco1.word8 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 5:############# word 6 ############
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.word5 = None
					self.table[i].bloco1.word6 = dado
					self.table[i].bloco1.word7 = None
					self.table[i].bloco1.word8 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 6:############# word 7 ############
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.word5 = None
					self.table[i].bloco1.word6 = None
					self.table[i].bloco1.word7 = dado 
					self.table[i].bloco1.word8 = None
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 7:############# word 8 ############
					self.table[i].bloco1.word1 = None
					self.table[i].bloco1.word2 = None
					self.table[i].bloco1.word3 = None
					self.table[i].bloco1.word4 = None
					self.table[i].bloco1.word5 = None
					self.table[i].bloco1.word6 = None
					self.table[i].bloco1.word7 = None
					self.table[i].bloco1.word8 = dado
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
				self.table[i].fifo.append(1)
			elif self.table[i].livre == 1: #BLOCO 02
				if num_address % 8 == 0:############# word 1 ############
					self.table[i].bloco2.word1 = dado
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.word5 = None
					self.table[i].bloco2.word6 = None
					self.table[i].bloco2.word7 = None
					self.table[i].bloco2.word8 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 1:############# word 2 ############
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = dado
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.word5 = None
					self.table[i].bloco2.word6 = None
					self.table[i].bloco2.word7 = None
					self.table[i].bloco2.word8 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 2:############# word 3 ############
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = dado
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.word5 = None
					self.table[i].bloco2.word6 = None
					self.table[i].bloco2.word7 = None
					self.table[i].bloco2.word8 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 3:############# word 4 ############
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = dado
					self.table[i].bloco2.word5 = None
					self.table[i].bloco2.word6 = None
					self.table[i].bloco2.word7 = None
					self.table[i].bloco2.word8 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 4:############# word 5 ############
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.word5 = dado
					self.table[i].bloco2.word6 = None
					self.table[i].bloco2.word7 = None
					self.table[i].bloco2.word8 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 5:############# word 6 ############
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.word5 = None
					self.table[i].bloco2.word6 = dado
					self.table[i].bloco2.word7 = None
					self.table[i].bloco2.word8 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 6:############# word 7 ############
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.word5 = None
					self.table[i].bloco2.word6 = None
					self.table[i].bloco2.word7 = dado 
					self.table[i].bloco2.word8 = None
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 7:############# word 8 ############
					self.table[i].bloco2.word1 = None
					self.table[i].bloco2.word2 = None
					self.table[i].bloco2.word3 = None
					self.table[i].bloco2.word4 = None
					self.table[i].bloco2.word5 = None
					self.table[i].bloco2.word6 = None
					self.table[i].bloco2.word7 = None
					self.table[i].bloco2.word8 = dado
					self.table[i].bloco2.tag_bin = tag_dada_bin
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 1
				self.table[i].fifo.append(2)
			elif self.table[i].livre == 2: #BLOCO 03
				if num_address % 8 == 0:############# word 1 ############
					self.table[i].bloco3.word1 = dado
					self.table[i].bloco3.word2 = None
					self.table[i].bloco3.word3 = None
					self.table[i].bloco3.word4 = None
					self.table[i].bloco3.word5 = None
					self.table[i].bloco3.word6 = None
					self.table[i].bloco3.word7 = None
					self.table[i].bloco3.word8 = None
					self.table[i].bloco3.tag_bin = tag_dada_bin
					self.table[i].bloco3.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 1:############# word 2 ############
					self.table[i].bloco3.word1 = None
					self.table[i].bloco3.word2 = dado
					self.table[i].bloco3.word3 = None
					self.table[i].bloco3.word4 = None
					self.table[i].bloco3.word5 = None
					self.table[i].bloco3.word6 = None
					self.table[i].bloco3.word7 = None
					self.table[i].bloco3.word8 = None
					self.table[i].bloco3.tag_bin = tag_dada_bin
					self.table[i].bloco3.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 2:############# word 3 ############
					self.table[i].bloco3.word1 = None
					self.table[i].bloco3.word2 = None
					self.table[i].bloco3.word3 = dado
					self.table[i].bloco3.word4 = None
					self.table[i].bloco3.word5 = None
					self.table[i].bloco3.word6 = None
					self.table[i].bloco3.word7 = None
					self.table[i].bloco3.word8 = None
					self.table[i].bloco3.tag_bin = tag_dada_bin
					self.table[i].bloco3.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 3:############# word 4 ############
					self.table[i].bloco3.word1 = None
					self.table[i].bloco3.word2 = None
					self.table[i].bloco3.word3 = None
					self.table[i].bloco3.word4 = dado
					self.table[i].bloco3.word5 = None
					self.table[i].bloco3.word6 = None
					self.table[i].bloco3.word7 = None
					self.table[i].bloco3.word8 = None
					self.table[i].bloco3.tag_bin = tag_dada_bin
					self.table[i].bloco3.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 4:############# word 5 ############
					self.table[i].bloco3.word1 = None
					self.table[i].bloco3.word2 = None
					self.table[i].bloco3.word3 = None
					self.table[i].bloco3.word4 = None
					self.table[i].bloco3.word5 = dado
					self.table[i].bloco3.word6 = None
					self.table[i].bloco3.word7 = None
					self.table[i].bloco3.word8 = None
					self.table[i].bloco3.tag_bin = tag_dada_bin
					self.table[i].bloco3.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 5:############# word 6 ############
					self.table[i].bloco3.word1 = None
					self.table[i].bloco3.word2 = None
					self.table[i].bloco3.word3 = None
					self.table[i].bloco3.word4 = None
					self.table[i].bloco3.word5 = None
					self.table[i].bloco3.word6 = dado
					self.table[i].bloco3.word7 = None
					self.table[i].bloco3.word8 = None
					self.table[i].bloco3.tag_bin = tag_dada_bin
					self.table[i].bloco3.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 6:############# word 7 ############
					self.table[i].bloco3.word1 = None
					self.table[i].bloco3.word2 = None
					self.table[i].bloco3.word3 = None
					self.table[i].bloco3.word4 = None
					self.table[i].bloco3.word5 = None
					self.table[i].bloco3.word6 = None
					self.table[i].bloco3.word7 = dado 
					self.table[i].bloco3.word8 = None
					self.table[i].bloco3.tag_bin = tag_dada_bin
					self.table[i].bloco3.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 7:############# word 8 ############
					self.table[i].bloco3.word1 = None
					self.table[i].bloco3.word2 = None
					self.table[i].bloco3.word3 = None
					self.table[i].bloco3.word4 = None
					self.table[i].bloco3.word5 = None
					self.table[i].bloco3.word6 = None
					self.table[i].bloco3.word7 = None
					self.table[i].bloco3.word8 = dado
					self.table[i].bloco3.tag_bin = tag_dada_bin
					self.table[i].bloco3.valid_bit = 1
					self.table[i].livre += 1
				self.table[i].fifo.append(3)
			elif self.table[i].livre == 3: #BLOCO 04
				if num_address % 8 == 0:############# word 1 ############
					self.table[i].bloco4.word1 = dado
					self.table[i].bloco4.word2 = None
					self.table[i].bloco4.word3 = None
					self.table[i].bloco4.word4 = None
					self.table[i].bloco4.word5 = None
					self.table[i].bloco4.word6 = None
					self.table[i].bloco4.word7 = None
					self.table[i].bloco4.word8 = None
					self.table[i].bloco4.tag_bin = tag_dada_bin
					self.table[i].bloco4.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 1:############# word 2 ############
					self.table[i].bloco4.word1 = None
					self.table[i].bloco4.word2 = dado
					self.table[i].bloco4.word3 = None
					self.table[i].bloco4.word4 = None
					self.table[i].bloco4.word5 = None
					self.table[i].bloco4.word6 = None
					self.table[i].bloco4.word7 = None
					self.table[i].bloco4.word8 = None
					self.table[i].bloco4.tag_bin = tag_dada_bin
					self.table[i].bloco4.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 2:############# word 3 ############
					self.table[i].bloco4.word1 = None
					self.table[i].bloco4.word2 = None
					self.table[i].bloco4.word3 = dado
					self.table[i].bloco4.word4 = None
					self.table[i].bloco4.word5 = None
					self.table[i].bloco4.word6 = None
					self.table[i].bloco4.word7 = None
					self.table[i].bloco4.word8 = None
					self.table[i].bloco4.tag_bin = tag_dada_bin
					self.table[i].bloco4.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 3:############# word 4 ############
					self.table[i].bloco4.word1 = None
					self.table[i].bloco4.word2 = None
					self.table[i].bloco4.word3 = None
					self.table[i].bloco4.word4 = dado
					self.table[i].bloco4.word5 = None
					self.table[i].bloco4.word6 = None
					self.table[i].bloco4.word7 = None
					self.table[i].bloco4.word8 = None
					self.table[i].bloco4.tag_bin = tag_dada_bin
					self.table[i].bloco4.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 4:############# word 5 ############
					self.table[i].bloco4.word1 = None
					self.table[i].bloco4.word2 = None
					self.table[i].bloco4.word3 = None
					self.table[i].bloco4.word4 = None
					self.table[i].bloco4.word5 = dado
					self.table[i].bloco4.word6 = None
					self.table[i].bloco4.word7 = None
					self.table[i].bloco4.word8 = None
					self.table[i].bloco4.tag_bin = tag_dada_bin
					self.table[i].bloco4.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 5:############# word 6 ############
					self.table[i].bloco4.word1 = None
					self.table[i].bloco4.word2 = None
					self.table[i].bloco4.word3 = None
					self.table[i].bloco4.word4 = None
					self.table[i].bloco4.word5 = None
					self.table[i].bloco4.word6 = dado
					self.table[i].bloco4.word7 = None
					self.table[i].bloco4.word8 = None
					self.table[i].bloco4.tag_bin = tag_dada_bin
					self.table[i].bloco4.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 6:############# word 7 ############
					self.table[i].bloco4.word1 = None
					self.table[i].bloco4.word2 = None
					self.table[i].bloco4.word3 = None
					self.table[i].bloco4.word4 = None
					self.table[i].bloco4.word5 = None
					self.table[i].bloco4.word6 = None
					self.table[i].bloco4.word7 = dado 
					self.table[i].bloco4.word8 = None
					self.table[i].bloco4.tag_bin = tag_dada_bin
					self.table[i].bloco4.valid_bit = 1
					self.table[i].livre += 1
				elif num_address % 8 == 7:############# word 8 ############
					self.table[i].bloco4.word1 = None
					self.table[i].bloco4.word2 = None
					self.table[i].bloco4.word3 = None
					self.table[i].bloco4.word4 = None
					self.table[i].bloco4.word5 = None
					self.table[i].bloco4.word6 = None
					self.table[i].bloco4.word7 = None
					self.table[i].bloco4.word8 = dado
					self.table[i].bloco4.tag_bin = tag_dada_bin
					self.table[i].bloco4.valid_bit = 1
					self.table[i].livre += 1
				self.table[i].fifo.append(4)
			elif self.table[i].livre >= 4: #TEM QUE ESCOLHER UM BLOCO PARA SUBSTITUIR...
				usado_ha_mais_tempo = self.table[i].fifo[0]
				self.table[i].fifo.pop(0)
				if usado_ha_mais_tempo == 1:
					if num_address % 8 == 0:############# word 1 ############
						self.table[i].bloco1.word1 = dado
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.word5 = None
						self.table[i].bloco1.word6 = None
						self.table[i].bloco1.word7 = None
						self.table[i].bloco1.word8 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 1:############# word 2 ############
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = dado
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.word5 = None
						self.table[i].bloco1.word6 = None
						self.table[i].bloco1.word7 = None
						self.table[i].bloco1.word8 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 2:############# word 3 ############
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = dado
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.word5 = None
						self.table[i].bloco1.word6 = None
						self.table[i].bloco1.word7 = None
						self.table[i].bloco1.word8 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 3:############# word 4 ############
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = dado
						self.table[i].bloco1.word5 = None
						self.table[i].bloco1.word6 = None
						self.table[i].bloco1.word7 = None
						self.table[i].bloco1.word8 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 4:############# word 5 ############
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.word5 = dado
						self.table[i].bloco1.word6 = None
						self.table[i].bloco1.word7 = None
						self.table[i].bloco1.word8 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 5:############# word 6 ############
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.word5 = None
						self.table[i].bloco1.word6 = dado
						self.table[i].bloco1.word7 = None
						self.table[i].bloco1.word8 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 6:############# word 7 ############
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.word5 = None
						self.table[i].bloco1.word6 = None
						self.table[i].bloco1.word7 = dado 
						self.table[i].bloco1.word8 = None
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 7:############# word 8 ############
						self.table[i].bloco1.word1 = None
						self.table[i].bloco1.word2 = None
						self.table[i].bloco1.word3 = None
						self.table[i].bloco1.word4 = None
						self.table[i].bloco1.word5 = None
						self.table[i].bloco1.word6 = None
						self.table[i].bloco1.word7 = None
						self.table[i].bloco1.word8 = dado
						self.table[i].bloco1.tag_bin = tag_dada_bin
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif usado_ha_mais_tempo == 2:
					if num_address % 8 == 0:############# word 1 ############
						self.table[i].bloco2.word1 = dado
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.word5 = None
						self.table[i].bloco2.word6 = None
						self.table[i].bloco2.word7 = None
						self.table[i].bloco2.word8 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 1:############# word 2 ############
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = dado
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.word5 = None
						self.table[i].bloco2.word6 = None
						self.table[i].bloco2.word7 = None
						self.table[i].bloco2.word8 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 2:############# word 3 ############
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = dado
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.word5 = None
						self.table[i].bloco2.word6 = None
						self.table[i].bloco2.word7 = None
						self.table[i].bloco2.word8 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 3:############# word 4 ############
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = dado
						self.table[i].bloco2.word5 = None
						self.table[i].bloco2.word6 = None
						self.table[i].bloco2.word7 = None
						self.table[i].bloco2.word8 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 4:############# word 5 ############
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.word5 = dado
						self.table[i].bloco2.word6 = None
						self.table[i].bloco2.word7 = None
						self.table[i].bloco2.word8 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 5:############# word 6 ############
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.word5 = None
						self.table[i].bloco2.word6 = dado
						self.table[i].bloco2.word7 = None
						self.table[i].bloco2.word8 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 6:############# word 7 ############
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.word5 = None
						self.table[i].bloco2.word6 = None
						self.table[i].bloco2.word7 = dado 
						self.table[i].bloco2.word8 = None
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 7:############# word 8 ############
						self.table[i].bloco2.word1 = None
						self.table[i].bloco2.word2 = None
						self.table[i].bloco2.word3 = None
						self.table[i].bloco2.word4 = None
						self.table[i].bloco2.word5 = None
						self.table[i].bloco2.word6 = None
						self.table[i].bloco2.word7 = None
						self.table[i].bloco2.word8 = dado
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
					self.table[i].fifo.append(2)
				elif usado_ha_mais_tempo == 3:
					if num_address % 8 == 0:############# word 1 ############
						self.table[i].bloco3.word1 = dado
						self.table[i].bloco3.word2 = None
						self.table[i].bloco3.word3 = None
						self.table[i].bloco3.word4 = None
						self.table[i].bloco3.word5 = None
						self.table[i].bloco3.word6 = None
						self.table[i].bloco3.word7 = None
						self.table[i].bloco3.word8 = None
						self.table[i].bloco3.tag_bin = tag_dada_bin
						self.table[i].bloco3.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 1:############# word 2 ############
						self.table[i].bloco3.word1 = None
						self.table[i].bloco3.word2 = dado
						self.table[i].bloco3.word3 = None
						self.table[i].bloco3.word4 = None
						self.table[i].bloco3.word5 = None
						self.table[i].bloco3.word6 = None
						self.table[i].bloco3.word7 = None
						self.table[i].bloco3.word8 = None
						self.table[i].bloco3.tag_bin = tag_dada_bin
						self.table[i].bloco3.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 2:############# word 3 ############
						self.table[i].bloco3.word1 = None
						self.table[i].bloco3.word2 = None
						self.table[i].bloco3.word3 = dado
						self.table[i].bloco3.word4 = None
						self.table[i].bloco3.word5 = None
						self.table[i].bloco3.word6 = None
						self.table[i].bloco3.word7 = None
						self.table[i].bloco3.word8 = None
						self.table[i].bloco3.tag_bin = tag_dada_bin
						self.table[i].bloco3.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 3:############# word 4 ############
						self.table[i].bloco3.word1 = None
						self.table[i].bloco3.word2 = None
						self.table[i].bloco3.word3 = None
						self.table[i].bloco3.word4 = dado
						self.table[i].bloco3.word5 = None
						self.table[i].bloco3.word6 = None
						self.table[i].bloco3.word7 = None
						self.table[i].bloco3.word8 = None
						self.table[i].bloco3.tag_bin = tag_dada_bin
						self.table[i].bloco3.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 4:############# word 5 ############
						self.table[i].bloco3.word1 = None
						self.table[i].bloco3.word2 = None
						self.table[i].bloco3.word3 = None
						self.table[i].bloco3.word4 = None
						self.table[i].bloco3.word5 = dado
						self.table[i].bloco3.word6 = None
						self.table[i].bloco3.word7 = None
						self.table[i].bloco3.word8 = None
						self.table[i].bloco3.tag_bin = tag_dada_bin
						self.table[i].bloco3.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 5:############# word 6 ############
						self.table[i].bloco3.word1 = None
						self.table[i].bloco3.word2 = None
						self.table[i].bloco3.word3 = None
						self.table[i].bloco3.word4 = None
						self.table[i].bloco3.word5 = None
						self.table[i].bloco3.word6 = dado
						self.table[i].bloco3.word7 = None
						self.table[i].bloco3.word8 = None
						self.table[i].bloco3.tag_bin = tag_dada_bin
						self.table[i].bloco3.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 6:############# word 7 ############
						self.table[i].bloco3.word1 = None
						self.table[i].bloco3.word2 = None
						self.table[i].bloco3.word3 = None
						self.table[i].bloco3.word4 = None
						self.table[i].bloco3.word5 = None
						self.table[i].bloco3.word6 = None
						self.table[i].bloco3.word7 = dado 
						self.table[i].bloco3.word8 = None
						self.table[i].bloco3.tag_bin = tag_dada_bin
						self.table[i].bloco3.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 7:############# word 8 ############
						self.table[i].bloco3.word1 = None
						self.table[i].bloco3.word2 = None
						self.table[i].bloco3.word3 = None
						self.table[i].bloco3.word4 = None
						self.table[i].bloco3.word5 = None
						self.table[i].bloco3.word6 = None
						self.table[i].bloco3.word7 = None
						self.table[i].bloco3.word8 = dado
						self.table[i].bloco3.tag_bin = tag_dada_bin
						self.table[i].bloco3.valid_bit = 1
						self.table[i].livre += 1
					self.table[i].fifo.append(3)
				elif usado_ha_mais_tempo == 4:
					if num_address % 8 == 0:############# word 1 ############
						self.table[i].bloco4.word1 = dado
						self.table[i].bloco4.word2 = None
						self.table[i].bloco4.word3 = None
						self.table[i].bloco4.word4 = None
						self.table[i].bloco4.word5 = None
						self.table[i].bloco4.word6 = None
						self.table[i].bloco4.word7 = None
						self.table[i].bloco4.word8 = None
						self.table[i].bloco4.tag_bin = tag_dada_bin
						self.table[i].bloco4.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 1:############# word 2 ############
						self.table[i].bloco4.word1 = None
						self.table[i].bloco4.word2 = dado
						self.table[i].bloco4.word3 = None
						self.table[i].bloco4.word4 = None
						self.table[i].bloco4.word5 = None
						self.table[i].bloco4.word6 = None
						self.table[i].bloco4.word7 = None
						self.table[i].bloco4.word8 = None
						self.table[i].bloco4.tag_bin = tag_dada_bin
						self.table[i].bloco4.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 2:############# word 3 ############
						self.table[i].bloco4.word1 = None
						self.table[i].bloco4.word2 = None
						self.table[i].bloco4.word3 = dado
						self.table[i].bloco4.word4 = None
						self.table[i].bloco4.word5 = None
						self.table[i].bloco4.word6 = None
						self.table[i].bloco4.word7 = None
						self.table[i].bloco4.word8 = None
						self.table[i].bloco4.tag_bin = tag_dada_bin
						self.table[i].bloco4.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 3:############# word 4 ############
						self.table[i].bloco4.word1 = None
						self.table[i].bloco4.word2 = None
						self.table[i].bloco4.word3 = None
						self.table[i].bloco4.word4 = dado
						self.table[i].bloco4.word5 = None
						self.table[i].bloco4.word6 = None
						self.table[i].bloco4.word7 = None
						self.table[i].bloco4.word8 = None
						self.table[i].bloco4.tag_bin = tag_dada_bin
						self.table[i].bloco4.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 4:############# word 5 ############
						self.table[i].bloco4.word1 = None
						self.table[i].bloco4.word2 = None
						self.table[i].bloco4.word3 = None
						self.table[i].bloco4.word4 = None
						self.table[i].bloco4.word5 = dado
						self.table[i].bloco4.word6 = None
						self.table[i].bloco4.word7 = None
						self.table[i].bloco4.word8 = None
						self.table[i].bloco4.tag_bin = tag_dada_bin
						self.table[i].bloco4.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 5:############# word 6 ############
						self.table[i].bloco4.word1 = None
						self.table[i].bloco4.word2 = None
						self.table[i].bloco4.word3 = None
						self.table[i].bloco4.word4 = None
						self.table[i].bloco4.word5 = None
						self.table[i].bloco4.word6 = dado
						self.table[i].bloco4.word7 = None
						self.table[i].bloco4.word8 = None
						self.table[i].bloco4.tag_bin = tag_dada_bin
						self.table[i].bloco4.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 6:############# word 7 ############
						self.table[i].bloco4.word1 = None
						self.table[i].bloco4.word2 = None
						self.table[i].bloco4.word3 = None
						self.table[i].bloco4.word4 = None
						self.table[i].bloco4.word5 = None
						self.table[i].bloco4.word6 = None
						self.table[i].bloco4.word7 = dado 
						self.table[i].bloco4.word8 = None
						self.table[i].bloco4.tag_bin = tag_dada_bin
						self.table[i].bloco4.valid_bit = 1
						self.table[i].livre += 1
					elif num_address % 8 == 7:############# word 8 ############
						self.table[i].bloco4.word1 = None
						self.table[i].bloco4.word2 = None
						self.table[i].bloco4.word3 = None
						self.table[i].bloco4.word4 = None
						self.table[i].bloco4.word5 = None
						self.table[i].bloco4.word6 = None
						self.table[i].bloco4.word7 = None
						self.table[i].bloco4.word8 = dado
						self.table[i].bloco4.tag_bin = tag_dada_bin
						self.table[i].bloco4.valid_bit = 1
						self.table[i].livre += 1
					self.table[i].fifo.append(4)
		elif tipo_cache == 'D1':
			#FULLY ASSOCIATIVE WITH 1 WORD/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##                        TAG                       ##   
			##                      32 BITS                     ##
			######################################################
			i = self.free #comeco escrevendo no primeiro block do unico set
			tag_dada_bin = binary_address
			dado = int(num_address)
			self.table[i].tag_bin = tag_dada_bin
			self.table[i].word1 = dado 
			self.table[i].valid_bit = 1
			pseudoindex = bin(i)
			newindex = pseudoindex[2:]
			final = newindex.zfill(32)
			self.table[i].index_binary = final
			self.free += 1
			if self.free == 1024:
				self.free = 0
		elif tipo_cache == 'D2':
			#FULLY ASSOCIATIVE WITH 2 WORDS/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##                   TAG         OFFSET             ##   
			##                 31 BITS        1 BIT             ##
			######################################################
			i = self.free #comeco escrevendo no primeiro block do unico set
			tag_dada_bin = binary_address[0:31]
			dado = int(num_address)
			if dado % 2 == 0:
				self.table[i].tag_bin = tag_dada_bin
				self.table[i].word1 = dado
				self.table[i].word2 = None
				self.table[i].valid_bit = 1
				pseudoindex = bin(i)
				newindex = pseudoindex[2:]
				final = newindex.zfill(32)
				self.table[i].index_binary = final
			elif dado % 2 == 1:
				self.table[i].tag_bin = tag_dada_bin
				self.table[i].word1 = None
				self.table[i].word2 = dado
				self.table[i].valid_bit = 1
				pseudoindex = bin(i)
				newindex = pseudoindex[2:]
				final = newindex.zfill(32)
				self.table[i].index_binary = final
			self.free += 1
			if self.free == 512:
				self.free = 0
		elif tipo_cache == 'D3':
			#FULLY ASSOCIATIVE WITH 4 WORDS/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##                   TAG         OFFSET             ##   
			##                 30 BITS        2 BIT             ##
			######################################################
			i = self.free #comeco escrevendo no primeiro block do unico set
			tag_dada_bin = binary_address[0:30]
			dado = int(num_address)
			if dado % 4 == 0:
				self.table[i].tag_bin = tag_dada_bin
				self.table[i].word1 = dado
				self.table[i].word2 = None
				self.table[i].word3 = None 
				self.table[i].word4 = None
				self.table[i].valid_bit = 1
				pseudoindex = bin(i)
				newindex = pseudoindex[2:]
				final = newindex.zfill(32)
				self.table[i].index_binary = final
			elif dado % 4 == 1:
				self.table[i].tag_bin = tag_dada_bin
				self.table[i].word1 = None
				self.table[i].word2 = dado
				self.table[i].word3 = None 
				self.table[i].word4 = None
				self.table[i].valid_bit = 1
				pseudoindex = bin(i)
				newindex = pseudoindex[2:]
				final = newindex.zfill(32)
				self.table[i].index_binary = final
			elif dado % 4 == 2:
				self.table[i].tag_bin = tag_dada_bin
				self.table[i].word1 = None
				self.table[i].word2 = None
				self.table[i].word3 = dado  
				self.table[i].word4 = None
				self.table[i].valid_bit = 1
				pseudoindex = bin(i)
				newindex = pseudoindex[2:]
				final = newindex.zfill(32)
				self.table[i].index_binary = final
			elif dado % 4 == 3:
				self.table[i].tag_bin = tag_dada_bin
				self.table[i].word1 = None
				self.table[i].word2 = None
				self.table[i].word3 = None 
				self.table[i].word4 = dado
				self.table[i].valid_bit = 1
				pseudoindex = bin(i)
				newindex = pseudoindex[2:]
				final = newindex.zfill(32)
				self.table[i].index_binary = final
			self.free += 1
			if self.free == 256:
				self.free = 0
		elif tipo_cache == 'D4':
			#FULLY ASSOCIATIVE WITH 8 WORDS/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##                   TAG         OFFSET             ##   
			##                 29 BITS        3 BIT             ##
			######################################################
			i = self.free
			tag_dada_bin = binary_address[0:29]
			dado = int(num_address)
			if dado % 8 == 0:
				self.table[i].tag_bin = tag_dada_bin
				self.table[i].word1 = dado
				self.table[i].word2 = None
				self.table[i].word3 = None 
				self.table[i].word4 = None
				self.table[i].word5 = None
				self.table[i].word6 = None
				self.table[i].word7 = None
				self.table[i].word8 = None
				self.table[i].valid_bit = 1
				pseudoindex = bin(i)
				newindex = pseudoindex[2:]
				final = newindex.zfill(32)
				self.table[i].index_binary = final
			elif dado % 8 == 1:
				self.table[i].tag_bin = tag_dada_bin
				self.table[i].word1 = None
				self.table[i].word2 = dado 
				self.table[i].word3 = None 
				self.table[i].word4 = None
				self.table[i].word5 = None
				self.table[i].word6 = None
				self.table[i].word7 = None
				self.table[i].word8 = None
				self.table[i].valid_bit = 1
				pseudoindex = bin(i)
				newindex = pseudoindex[2:]
				final = newindex.zfill(32)
				self.table[i].index_binary = final
			elif dado % 8 == 2:
				self.table[i].tag_bin = tag_dada_bin
				self.table[i].word1 = None
				self.table[i].word2 = None
				self.table[i].word3 = dado 
				self.table[i].word4 = None
				self.table[i].word5 = None
				self.table[i].word6 = None
				self.table[i].word7 = None
				self.table[i].word8 = None
				self.table[i].valid_bit = 1
				pseudoindex = bin(i)
				newindex = pseudoindex[2:]
				final = newindex.zfill(32)
				self.table[i].index_binary = final
			elif dado % 8 == 3:
				self.table[i].tag_bin = tag_dada_bin
				self.table[i].word1 = None
				self.table[i].word2 = None
				self.table[i].word3 = None 
				self.table[i].word4 = dado
				self.table[i].word5 = None
				self.table[i].word6 = None
				self.table[i].word7 = None
				self.table[i].word8 = None
				self.table[i].valid_bit = 1
				pseudoindex = bin(i)
				newindex = pseudoindex[2:]
				final = newindex.zfill(32)
				self.table[i].index_binary = final
			elif dado % 8 == 4:
				self.table[i].tag_bin = tag_dada_bin
				self.table[i].word1 = None
				self.table[i].word2 = None
				self.table[i].word3 = None 
				self.table[i].word4 = None
				self.table[i].word5 = dado 
				self.table[i].word6 = None
				self.table[i].word7 = None
				self.table[i].word8 = None
				self.table[i].valid_bit = 1
				pseudoindex = bin(i)
				newindex = pseudoindex[2:]
				final = newindex.zfill(32)
				self.table[i].index_binary = final
			elif dado % 8 == 5:
				self.table[i].tag_bin = tag_dada_bin
				self.table[i].word1 = None
				self.table[i].word2 = None
				self.table[i].word3 = None 
				self.table[i].word4 = None
				self.table[i].word5 = None
				self.table[i].word6 = dado 
				self.table[i].word7 = None
				self.table[i].word8 = None
				self.table[i].valid_bit = 1
				pseudoindex = bin(i)
				newindex = pseudoindex[2:]
				final = newindex.zfill(32)
				self.table[i].index_binary = final
			elif dado % 8 == 6:
				self.table[i].tag_bin = tag_dada_bin
				self.table[i].word1 = None
				self.table[i].word2 = None
				self.table[i].word3 = None 
				self.table[i].word4 = None
				self.table[i].word5 = None
				self.table[i].word6 = None
				self.table[i].word7 = dado 
				self.table[i].word8 = None
				self.table[i].valid_bit = 1
				pseudoindex = bin(i)
				newindex = pseudoindex[2:]
				final = newindex.zfill(32)
				self.table[i].index_binary = final
			elif dado % 8 == 7:
				self.table[i].tag_bin = tag_dada_bin
				self.table[i].word1 = None
				self.table[i].word2 = None
				self.table[i].word3 = None 
				self.table[i].word4 = None
				self.table[i].word5 = None
				self.table[i].word6 = None
				self.table[i].word7 = None
				self.table[i].word8 = dado 
				self.table[i].valid_bit = 1
				pseudoindex = bin(i)
				newindex = pseudoindex[2:]
				final = newindex.zfill(32)
				self.table[i].index_binary = final
			self.free += 1
			if self.free == 128:
				self.free = 0

	def read_cache(self, num_address, binary_address, tipo_cache):
		if tipo_cache == 'A1':
			#######################################
			##  CONFIGURACAO DO ENDERECO 32 BITS ##
			##    TAG                    INDEX   ##   
			##  22 BITS                 1O BITS  ##
			#######################################
			i = int(binary_address[22:], 2)
			print(f"i: {i} ---- index_binary: {binary_address[22:]} --- full binary address: {binary_address}")
			#### CASO NAO TENHA NADA NAQUELE BLOCK -- MISS COMPULSORY ####
			if self.table[i].valid_bit == 0:
				self.table[i].index_binary = binary_address[22:]
				self.table[i].tag_bin = binary_address[0:22]
				self.table[i].word1 = int(num_address)
				self.table[i].valid_bit = 1;
				return 2
			elif self.table[i].valid_bit == 1:
				#E AGORA: TEM QUE CHECAR PRA VER SE TEMOS UM HIT OU SE TEMOS UM MISS POR CONFLITO:
				if binary_address[0:22] == self.table[i].tag_bin:
					#CASO DE UM HIT: TEMOS QUE A TAG PRESENTE NO ENDERECO EH IGUAL A TAG PRESENTE NAQUELE BLOCO ESPECIFICO DA CACHE
					return 1
				elif binary_address[0:22] != self.table[i].tag_bin:
					#CASO DE UM MISS POR CONFLITO: 
					self.table[i].index_binary = binary_address[22:]
					self.table[i].tag_bin = binary_address[0:22]
					self.table[i].word1 = int(num_address)
					self.table[i].valid_bit = 1;
					return 3
		elif tipo_cache == 'A2':
			#######################################
			##  CONFIGURACAO DO ENDERECO 32 BITS ##
			##    TAG       INDEX   BLOCK OFFSET ##   
			##  22 BITS    O9 BITS     01 BIT    ##
			#######################################
			i = int(binary_address[22:31],2) #INDEX
			print(f"i: {i} ---- index_binary: {binary_address[22:31]} --- full binary address: {binary_address}")
			#### CASO NAO TENHA NADA NAQUELE BLOCK -- MISS COMPULSORY ####
			if self.table[i].valid_bit == 0:
				if num_address % 2 == 0:
					self.table[i].index_binary = binary_address[22:31]
					self.table[i].tag_bin = binary_address[0:22]
					self.table[i].word1 = int(num_address)
					self.table[i].word2 = int(num_address) + 1
					self.table[i].valid_bit = 1
				elif num_address % 2 == 1:
					self.table[i].index_binary = binary_address[22:31]
					self.table[i].tag_bin = binary_address[0:22]
					self.table[i].word1 = int(num_address) - 1
					self.table[i].word2 = int(num_address)
					self.table[i].valid_bit = 1
				return 2
			elif self.table[i].valid_bit == 1:
				#E AGORA: TEM QUE CHECAR PRA VER SE TEMOS UM HIT OU SE TEMOS UM MISS POR CONFLITO:
				if binary_address[0:22] == self.table[i].tag_bin:
					#CASO DE UM HIT: TEMOS QUE A TAG PRESENTE NO ENDERECO EH IGUAL A TAG PRESENTE NAQUELE BLOCO ESPECIFICO DA CACHE
					if num_address % 2 == 0:
						if self.table[i].word1 == num_address:
							return 1
						elif self.table[i].word1 == None:
							self.table[i].index_binary = binary_address[22:31]
							self.table[i].tag_bin = binary_address[0:22]
							self.table[i].word1 = int(num_address)
							self.table[i].word2 = int(num_address) + 1
							self.table[i].valid_bit = 1
							return 2
					elif num_address % 2 == 1:
						if self.table[i].word2 == num_address:
							return 1
						elif self.table[i].word2 == None:
							self.table[i].index_binary = binary_address[22:31]
							self.table[i].tag_bin = binary_address[0:22]
							self.table[i].word1 = int(num_address) - 1
							self.table[i].word2 = int(num_address)
							self.table[i].valid_bit = 1
							return 2
				elif binary_address[0:22] != self.table[i].tag_bin:
					#CASO DE UM MISS POR CONFLITO: 
					if num_address % 2 == 0:
						self.table[i].index_binary = binary_address[22:31]
						self.table[i].tag_bin = binary_address[0:22]
						self.table[i].word1 = int(num_address)
						self.table[i].word2 = int(num_address) + 1
						self.table[i].valid_bit = 1
					elif num_address % 2 == 1:
						self.table[i].index_binary = binary_address[22:31]
						self.table[i].tag_bin = binary_address[0:22]
						self.table[i].word1 = int(num_address) - 1
						self.table[i].word2 = int(num_address)
						self.table[i].valid_bit = 1
					return 3
		elif tipo_cache == 'A3':
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                INDEX         BLOCK OFFSET ##   
			##  22 BITS             O8 BITS           02 BIT    ##
			######################################################
			i = int(binary_address[22:30],2) #INDEX
			print(f"i: {i} ---- index_binary: {binary_address[22:30]} --- full binary address: {binary_address}")
			#### CASO NAO TENHA NADA NAQUELE BLOCK -- MISS COMPULSORY ####
			if self.table[i].valid_bit == 0:
				if num_address % 4 == 0:
					self.table[i].index_binary = binary_address[22:30]
					self.table[i].tag_bin = binary_address[0:22]
					self.table[i].word1 = int(num_address)
					self.table[i].word2 = int(num_address) + 1
					self.table[i].word3 = int(num_address) + 2
					self.table[i].word4 = int(num_address) + 3
					self.table[i].valid_bit = 1
				elif num_address % 4 == 1:
					self.table[i].index_binary = binary_address[22:30]
					self.table[i].tag_bin = binary_address[0:22]
					self.table[i].word1 = int(num_address) - 1
					self.table[i].word2 = int(num_address)
					self.table[i].word3 = int(num_address) + 1
					self.table[i].word4 = int(num_address) + 2
					self.table[i].valid_bit = 1
				elif num_address % 4 == 2:
					self.table[i].index_binary = binary_address[22:30]
					self.table[i].tag_bin = binary_address[0:22]
					self.table[i].word1 = int(num_address) - 2
					self.table[i].word2 = int(num_address) - 1
					self.table[i].word3 = int(num_address)
					self.table[i].word4 = int(num_address) + 1
					self.table[i].valid_bit = 1
				elif num_address % 4 == 3:
					self.table[i].index_binary = binary_address[22:30]
					self.table[i].tag_bin = binary_address[0:22]
					self.table[i].word1 = int(num_address) - 3
					self.table[i].word2 = int(num_address) - 2
					self.table[i].word3 = int(num_address) - 1
					self.table[i].word4 = int(num_address)
					self.table[i].valid_bit = 1
				return 2
			elif self.table[i].valid_bit == 1:
				#E AGORA: TEM QUE CHECAR PRA VER SE TEMOS UM HIT OU SE TEMOS UM MISS POR CONFLITO:
				if binary_address[0:22] == self.table[i].tag_bin:
					#CASO DE UM HIT: TEMOS QUE A TAG PRESENTE NO ENDERECO EH IGUAL A TAG PRESENTE NAQUELE BLOCO ESPECIFICO DA CACHE
					if num_address % 4 == 0:
						if self.table[i].word1 == num_address:
							return 1
						elif self.table[i].word1 == None:
							self.table[i].index_binary = binary_address[22:30]
							self.table[i].tag_bin = binary_address[0:22]
							self.table[i].word1 = int(num_address)
							self.table[i].word2 = int(num_address) + 1
							self.table[i].word3 = int(num_address) + 2
							self.table[i].word4 = int(num_address) + 3
							self.table[i].valid_bit = 1
							return 2
					elif num_address % 4 == 1:
						if self.table[i].word2 == num_address:
							return 1
						elif self.table[i].word2 == None:
							self.table[i].index_binary = binary_address[22:30]
							self.table[i].tag_bin = binary_address[0:22]
							self.table[i].word1 = int(num_address) - 1
							self.table[i].word2 = int(num_address)
							self.table[i].word3 = int(num_address) + 1
							self.table[i].word4 = int(num_address) + 2
							self.table[i].valid_bit = 1
							return 2
					elif num_address % 4 == 2:
						if self.table[i].word3 == num_address:
							return 1
						elif self.table[i].word3 == None:
							self.table[i].index_binary = binary_address[22:30]
							self.table[i].tag_bin = binary_address[0:22]
							self.table[i].word1 = int(num_address) - 2
							self.table[i].word2 = int(num_address) - 1
							self.table[i].word3 = int(num_address)
							self.table[i].word4 = int(num_address) + 1
							self.table[i].valid_bit = 1
							return 2 
					elif num_address % 4 == 3:
						if self.table[i].word4 == num_address:
							return 1
						elif self.table[i].word4 == None:
							self.table[i].index_binary = binary_address[22:30]
							self.table[i].tag_bin = binary_address[0:22]
							self.table[i].word1 = int(num_address) - 3
							self.table[i].word2 = int(num_address) - 2
							self.table[i].word3 = int(num_address) - 1
							self.table[i].word4 = int(num_address)
							self.table[i].valid_bit = 1
							return 2
				elif binary_address[0:22] != self.table[i].tag_bin:
					#CASO DE UM MISS POR CONFLITO: 
					if num_address % 4 == 0:
						self.table[i].index_binary = binary_address[22:30]
						self.table[i].tag_bin = binary_address[0:22]
						self.table[i].word1 = int(num_address)
						self.table[i].word2 = int(num_address) + 1
						self.table[i].word3 = int(num_address) + 2
						self.table[i].word4 = int(num_address) + 3
						self.table[i].valid_bit = 1
					elif num_address % 4 == 1:
						self.table[i].index_binary = binary_address[22:30]
						self.table[i].tag_bin = binary_address[0:22]
						self.table[i].word1 = int(num_address) - 1
						self.table[i].word2 = int(num_address)
						self.table[i].word3 = int(num_address) + 1
						self.table[i].word4 = int(num_address) + 2
						self.table[i].valid_bit = 1
					elif num_address % 4 == 2:
						self.table[i].index_binary = binary_address[22:30]
						self.table[i].tag_bin = binary_address[0:22]
						self.table[i].word1 = int(num_address) - 2
						self.table[i].word2 = int(num_address) - 1
						self.table[i].word3 = int(num_address)
						self.table[i].word4 = int(num_address) + 1
						self.table[i].valid_bit = 1
					elif num_address % 4 == 3:
						self.table[i].index_binary = binary_address[22:30]
						self.table[i].tag_bin = binary_address[0:22]
						self.table[i].word1 = int(num_address) - 3
						self.table[i].word2 = int(num_address) - 2
						self.table[i].word3 = int(num_address) - 1
						self.table[i].word4 = int(num_address)
						self.table[i].valid_bit = 1
					return 3
		elif tipo_cache == 'A4':
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                INDEX         BLOCK OFFSET ##   
			##  22 BITS             O7 BITS           03 BIT    ##
			######################################################
			i = int(binary_address[22:29],2) #INDEX
			print(f"i: {i} ---- index_binary: {binary_address[22:29]} --- full binary address: {binary_address}")
			#### CASO NAO TENHA NADA NAQUELE BLOCK -- MISS COMPULSORY ####
			if self.table[i].valid_bit == 0:
				if num_address % 8 == 0:
					self.table[i].index_binary = binary_address[22:29]
					self.table[i].tag_bin = binary_address[0:22]
					self.table[i].word1 = int(num_address)
					self.table[i].word2 = int(num_address) + 1
					self.table[i].word3 = int(num_address) + 2
					self.table[i].word4 = int(num_address) + 3
					self.table[i].word5 = int(num_address) + 4
					self.table[i].word6 = int(num_address) + 5
					self.table[i].word7 = int(num_address) + 6
					self.table[i].word8 = int(num_address) + 7
					self.table[i].valid_bit = 1
				elif num_address % 8 == 1:
					self.table[i].index_binary = binary_address[22:29]
					self.table[i].tag_bin = binary_address[0:22]
					self.table[i].word1 = int(num_address) - 1
					self.table[i].word2 = int(num_address)
					self.table[i].word3 = int(num_address) + 1
					self.table[i].word4 = int(num_address) + 2
					self.table[i].word5 = int(num_address) + 3
					self.table[i].word6 = int(num_address) + 4
					self.table[i].word7 = int(num_address) + 5
					self.table[i].word8 = int(num_address) + 6
					self.table[i].valid_bit = 1
				elif num_address % 8 == 2:
					self.table[i].index_binary = binary_address[22:29]
					self.table[i].tag_bin = binary_address[0:22]
					self.table[i].word1 = int(num_address) - 2
					self.table[i].word2 = int(num_address) - 1
					self.table[i].word3 = int(num_address)
					self.table[i].word4 = int(num_address) + 1
					self.table[i].word5 = int(num_address) + 2
					self.table[i].word6 = int(num_address) + 3
					self.table[i].word7 = int(num_address) + 4
					self.table[i].word8 = int(num_address) + 5
					self.table[i].valid_bit = 1
				elif num_address % 8 == 3:
					self.table[i].index_binary = binary_address[22:29]
					self.table[i].tag_bin = binary_address[0:22]
					self.table[i].word1 = int(num_address) - 3
					self.table[i].word2 = int(num_address) - 2
					self.table[i].word3 = int(num_address) - 1
					self.table[i].word4 = int(num_address)
					self.table[i].word5 = int(num_address) + 1
					self.table[i].word6 = int(num_address) + 2
					self.table[i].word7 = int(num_address) + 3
					self.table[i].word8 = int(num_address) + 4
					self.table[i].valid_bit = 1
				elif num_address % 8 == 4:
					self.table[i].index_binary = binary_address[22:29]
					self.table[i].tag_bin = binary_address[0:22]
					self.table[i].word1 = int(num_address) - 4
					self.table[i].word2 = int(num_address) - 3
					self.table[i].word3 = int(num_address) - 2
					self.table[i].word4 = int(num_address) - 1
					self.table[i].word5 = int(num_address) 
					self.table[i].word6 = int(num_address) + 1
					self.table[i].word7 = int(num_address) + 2
					self.table[i].word8 = int(num_address) + 3
					self.table[i].valid_bit = 1
				elif num_address % 8 == 5:
					self.table[i].index_binary = binary_address[22:29]
					self.table[i].tag_bin = binary_address[0:22]
					self.table[i].word1 = int(num_address) - 5
					self.table[i].word2 = int(num_address) - 4
					self.table[i].word3 = int(num_address) - 3
					self.table[i].word4 = int(num_address) - 2
					self.table[i].word5 = int(num_address) - 1
					self.table[i].word6 = int(num_address) 
					self.table[i].word7 = int(num_address) + 1
					self.table[i].word8 = int(num_address) + 2
					self.table[i].valid_bit = 1
				elif num_address % 8 == 6:
					self.table[i].index_binary = binary_address[22:29]
					self.table[i].tag_bin = binary_address[0:22]
					self.table[i].word1 = int(num_address) - 6
					self.table[i].word2 = int(num_address) - 5
					self.table[i].word3 = int(num_address) - 4
					self.table[i].word4 = int(num_address) - 3
					self.table[i].word5 = int(num_address) - 2
					self.table[i].word6 = int(num_address) - 1
					self.table[i].word7 = int(num_address) 
					self.table[i].word8 = int(num_address) + 1
					self.table[i].valid_bit = 1
				elif num_address % 8 == 7:
					self.table[i].index_binary = binary_address[22:29]
					self.table[i].tag_bin = binary_address[0:22]
					self.table[i].word1 = int(num_address) - 7
					self.table[i].word2 = int(num_address) - 6
					self.table[i].word3 = int(num_address) - 5
					self.table[i].word4 = int(num_address) - 4
					self.table[i].word5 = int(num_address) - 3
					self.table[i].word6 = int(num_address) - 2
					self.table[i].word7 = int(num_address) - 1
					self.table[i].word8 = int(num_address) 
					self.table[i].valid_bit = 1
				return 2
			elif self.table[i].valid_bit == 1:
				#E AGORA: TEM QUE CHECAR PRA VER SE TEMOS UM HIT OU SE TEMOS UM MISS POR CONFLITO:
				if binary_address[0:22] == self.table[i].tag_bin:
					#CASO DE UM HIT: TEMOS QUE A TAG PRESENTE NO ENDERECO EH IGUAL A TAG PRESENTE NAQUELE BLOCO ESPECIFICO DA CACHE
					if num_address % 8 == 0:
						if self.table[i].word1 == num_address:
							return 1
						elif self.table[i].word1 == None:
							self.table[i].index_binary = binary_address[22:29]
							self.table[i].tag_bin = binary_address[0:22]
							self.table[i].word1 = int(num_address)
							self.table[i].word2 = int(num_address) + 1
							self.table[i].word3 = int(num_address) + 2
							self.table[i].word4 = int(num_address) + 3
							self.table[i].word5 = int(num_address) + 4
							self.table[i].word6 = int(num_address) + 5
							self.table[i].word7 = int(num_address) + 6
							self.table[i].word8 = int(num_address) + 7
							self.table[i].valid_bit = 1
							return 2
					elif num_address % 8 == 1:
						if self.table[i].word2 == num_address:
							return 1
						elif self.table[i].word2 == None:
							self.table[i].index_binary = binary_address[22:29]
							self.table[i].tag_bin = binary_address[0:22]
							self.table[i].word1 = int(num_address) - 1
							self.table[i].word2 = int(num_address)
							self.table[i].word3 = int(num_address) + 1
							self.table[i].word4 = int(num_address) + 2
							self.table[i].word5 = int(num_address) + 3
							self.table[i].word6 = int(num_address) + 4
							self.table[i].word7 = int(num_address) + 5
							self.table[i].word8 = int(num_address) + 6
							self.table[i].valid_bit = 1
							return 2
					elif num_address % 8 == 2:
						if self.table[i].word3 == num_address:
							return 1
						elif self.table[i].word3 == None:
							self.table[i].index_binary = binary_address[22:29]
							self.table[i].tag_bin = binary_address[0:22]
							self.table[i].word1 = int(num_address) - 2
							self.table[i].word2 = int(num_address) - 1
							self.table[i].word3 = int(num_address)
							self.table[i].word4 = int(num_address) + 1
							self.table[i].word5 = int(num_address) + 2
							self.table[i].word6 = int(num_address) + 3
							self.table[i].word7 = int(num_address) + 4
							self.table[i].word8 = int(num_address) + 5
							self.table[i].valid_bit = 1
							return 2
					elif num_address % 8 == 3:
						if self.table[i].word4 == num_address:
							return 1
						elif self.table[i].word4 == None:
							self.table[i].index_binary = binary_address[22:29]
							self.table[i].tag_bin = binary_address[0:22]
							self.table[i].word1 = int(num_address) - 3
							self.table[i].word2 = int(num_address) - 2
							self.table[i].word3 = int(num_address) - 1
							self.table[i].word4 = int(num_address)
							self.table[i].word5 = int(num_address) + 1
							self.table[i].word6 = int(num_address) + 2
							self.table[i].word7 = int(num_address) + 3
							self.table[i].word8 = int(num_address) + 4
							self.table[i].valid_bit = 1
							return 2
					elif num_address % 8 == 4:
						if self.table[i].word5 == num_address:
							return 1
						elif self.table[i].word5 == None:
							self.table[i].index_binary = binary_address[22:29]
							self.table[i].tag_bin = binary_address[0:22]
							self.table[i].word1 = int(num_address) - 4
							self.table[i].word2 = int(num_address) - 3
							self.table[i].word3 = int(num_address) - 2
							self.table[i].word4 = int(num_address) - 1
							self.table[i].word5 = int(num_address) 
							self.table[i].word6 = int(num_address) + 1
							self.table[i].word7 = int(num_address) + 2
							self.table[i].word8 = int(num_address) + 3
							self.table[i].valid_bit = 1
							return 2
					elif num_address % 8 == 5:
						if self.table[i].word6 == num_address:
							return 1
						elif self.table[i].word6 == None:
							self.table[i].index_binary = binary_address[22:29]
							self.table[i].tag_bin = binary_address[0:22]
							self.table[i].word1 = int(num_address) - 5
							self.table[i].word2 = int(num_address) - 4
							self.table[i].word3 = int(num_address) - 3
							self.table[i].word4 = int(num_address) - 2
							self.table[i].word5 = int(num_address) - 1
							self.table[i].word6 = int(num_address) 
							self.table[i].word7 = int(num_address) + 1
							self.table[i].word8 = int(num_address) + 2
							self.table[i].valid_bit = 1
							return 2
					elif num_address % 8 == 6:
						if self.table[i].word7 == num_address:
							return 1
						elif self.table[i].word7 == None:
							self.table[i].index_binary = binary_address[22:29]
							self.table[i].tag_bin = binary_address[0:22]
							self.table[i].word1 = int(num_address) - 6
							self.table[i].word2 = int(num_address) - 5
							self.table[i].word3 = int(num_address) - 4
							self.table[i].word4 = int(num_address) - 3
							self.table[i].word5 = int(num_address) - 2
							self.table[i].word6 = int(num_address) - 1
							self.table[i].word7 = int(num_address) 
							self.table[i].word8 = int(num_address) + 1
							self.table[i].valid_bit = 1
							return 2
					elif num_address % 8 == 7:
						if self.table[i].word8 == num_address:
							return 1
						elif self.table[i].word8 == None:
							self.table[i].index_binary = binary_address[22:29]
							self.table[i].tag_bin = binary_address[0:22]
							self.table[i].word1 = int(num_address) - 7
							self.table[i].word2 = int(num_address) - 6
							self.table[i].word3 = int(num_address) - 5
							self.table[i].word4 = int(num_address) - 4
							self.table[i].word5 = int(num_address) - 3
							self.table[i].word6 = int(num_address) - 2
							self.table[i].word7 = int(num_address) - 1
							self.table[i].word8 = int(num_address) 
							self.table[i].valid_bit = 1
							return 2
				elif binary_address[0:22] != self.table[i].tag_bin:
					#CASO DE UM MISS POR CONFLITO
					if num_address % 8 == 0:
						self.table[i].index_binary = binary_address[22:29]
						self.table[i].tag_bin = binary_address[0:22]
						self.table[i].word1 = int(num_address)
						self.table[i].word2 = int(num_address) + 1
						self.table[i].word3 = int(num_address) + 2
						self.table[i].word4 = int(num_address) + 3
						self.table[i].word5 = int(num_address) + 4
						self.table[i].word6 = int(num_address) + 5
						self.table[i].word7 = int(num_address) + 6
						self.table[i].word8 = int(num_address) + 7
						self.table[i].valid_bit = 1
					elif num_address % 8 == 1:
						self.table[i].index_binary = binary_address[22:29]
						self.table[i].tag_bin = binary_address[0:22]
						self.table[i].word1 = int(num_address) - 1
						self.table[i].word2 = int(num_address)
						self.table[i].word3 = int(num_address) + 1
						self.table[i].word4 = int(num_address) + 2
						self.table[i].word5 = int(num_address) + 3
						self.table[i].word6 = int(num_address) + 4
						self.table[i].word7 = int(num_address) + 5
						self.table[i].word8 = int(num_address) + 6
						self.table[i].valid_bit = 1
					elif num_address % 8 == 2:
						self.table[i].index_binary = binary_address[22:29]
						self.table[i].tag_bin = binary_address[0:22]
						self.table[i].word1 = int(num_address) - 2
						self.table[i].word2 = int(num_address) - 1
						self.table[i].word3 = int(num_address)
						self.table[i].word4 = int(num_address) + 1
						self.table[i].word5 = int(num_address) + 2
						self.table[i].word6 = int(num_address) + 3
						self.table[i].word7 = int(num_address) + 4
						self.table[i].word8 = int(num_address) + 5
						self.table[i].valid_bit = 1
					elif num_address % 8 == 3:
						self.table[i].index_binary = binary_address[22:29]
						self.table[i].tag_bin = binary_address[0:22]
						self.table[i].word1 = int(num_address) - 3
						self.table[i].word2 = int(num_address) - 2
						self.table[i].word3 = int(num_address) - 1
						self.table[i].word4 = int(num_address)
						self.table[i].word5 = int(num_address) + 1
						self.table[i].word6 = int(num_address) + 2
						self.table[i].word7 = int(num_address) + 3
						self.table[i].word8 = int(num_address) + 4
						self.table[i].valid_bit = 1
					elif num_address % 8 == 4:
						self.table[i].index_binary = binary_address[22:29]
						self.table[i].tag_bin = binary_address[0:22]
						self.table[i].word1 = int(num_address) - 4
						self.table[i].word2 = int(num_address) - 3
						self.table[i].word3 = int(num_address) - 2
						self.table[i].word4 = int(num_address) - 1
						self.table[i].word5 = int(num_address) 
						self.table[i].word6 = int(num_address) + 1
						self.table[i].word7 = int(num_address) + 2
						self.table[i].word8 = int(num_address) + 3
						self.table[i].valid_bit = 1
					elif num_address % 8 == 5:
						self.table[i].index_binary = binary_address[22:29]
						self.table[i].tag_bin = binary_address[0:22]
						self.table[i].word1 = int(num_address) - 5
						self.table[i].word2 = int(num_address) - 4
						self.table[i].word3 = int(num_address) - 3
						self.table[i].word4 = int(num_address) - 2
						self.table[i].word5 = int(num_address) - 1
						self.table[i].word6 = int(num_address) 
						self.table[i].word7 = int(num_address) + 1
						self.table[i].word8 = int(num_address) + 2
						self.table[i].valid_bit = 1
					elif num_address % 8 == 6:
						self.table[i].index_binary = binary_address[22:29]
						self.table[i].tag_bin = binary_address[0:22]
						self.table[i].word1 = int(num_address) - 6
						self.table[i].word2 = int(num_address) - 5
						self.table[i].word3 = int(num_address) - 4
						self.table[i].word4 = int(num_address) - 3
						self.table[i].word5 = int(num_address) - 2
						self.table[i].word6 = int(num_address) - 1
						self.table[i].word7 = int(num_address) 
						self.table[i].word8 = int(num_address) + 1
						self.table[i].valid_bit = 1
					elif num_address % 8 == 7:
						self.table[i].index_binary = binary_address[22:29]
						self.table[i].tag_bin = binary_address[0:22]
						self.table[i].word1 = int(num_address) - 7
						self.table[i].word2 = int(num_address) - 6
						self.table[i].word3 = int(num_address) - 5
						self.table[i].word4 = int(num_address) - 4
						self.table[i].word5 = int(num_address) - 3
						self.table[i].word6 = int(num_address) - 2
						self.table[i].word7 = int(num_address) - 1
						self.table[i].word8 = int(num_address) 
						self.table[i].valid_bit = 1
					return 3
		elif tipo_cache == 'B1':
			#TWO-WAY SET ASSOCIATIVE: 1 WORD/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                 SET           SET OFFSET  ##   
			##  22 BITS             O9 BITS           01 BIT    ##
			######################################################
			##TEM QUE CHECAR SE VAI DAR MISS COMPULSORY OU ALGO DO TIPO
			i = int(binary_address[22:31], 2) #SET NO FORMATO DECIMAL
			tag_dada_bin = binary_address[0:22] #pegando a tag que foi dada
			dado = int(num_address) #dado a ser escrito na forma decimal
			### CHECANDO PRA VER SE EH MISS COMPULSORIO #####
			if self.table[i].bloco1.valid_bit == 0 and self.table[i].bloco2.valid_bit == 0:
				#MISS COMPULSORY NA LATA. AZEDOU...
				self.table[i].bloco1.word1 = dado
				self.table[i].bloco1.tag_bin = tag_dada_bin 
				self.table[i].bloco1.valid_bit = 1
				self.table[i].livre += 1
				self.table[i].fifo.append(1)
				return 2
			elif self.table[i].bloco1.valid_bit == 1 and self.table[i].bloco2.valid_bit == 0:
				#BLOCO 1 DESSE SET JA TA OCUPADO... PODE SER QUE O DADO ESTEJA NO BLOCO 1 DESSE SET... CASO CONTRARIO TEM QUE DAR MISS COMPULSORY
				if self.table[i].bloco1.tag_bin == tag_dada_bin and self.table[i].bloco1.word1 == dado :
					self.table[i].fifo.append(1)
					return 1
				else:
					self.table[i].bloco2.word1 = dado
					self.table[i].bloco2.tag_bin = tag_dada_bin 
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 2
					self.table[i].fifo.append(2)
					return 2
			elif self.table[i].bloco1.valid_bit == 1 and self.table[i].bloco2.valid_bit == 1:
				if self.table[i].bloco1.tag_bin == tag_dada_bin and self.table[i].bloco1.word1 == dado:
					self.table[i].fifo.append(1)
					return 1
				elif self.table[i].bloco2.tag_bin == tag_dada_bin and self.table[i].bloco2.word1 == dado:
					self.table[i].fifo.append(2)
					return 1
				usado_ha_mais_tempo = self.table[i].fifo[0]
				self.table[i].fifo.pop(0)
				if usado_ha_mais_tempo == 1: #substitui o bloco 1 do set
					self.table[i].bloco1.word1 = dado
					self.table[i].bloco1.tag_bin = tag_dada_bin 
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif usado_ha_mais_tempo == 2: #substitui o bloco 2 do set
					self.table[i].bloco2.word1 = dado
					self.table[i].bloco2.tag_bin = tag_dada_bin 
					self.table[i].bloco2.valid_bit = 1
					self.table[i].livre += 2
					self.table[i].fifo.append(2)
				return 3
		elif tipo_cache == 'B2':
			#TWO-WAY SET ASSOCIATIVE: 2 WORDs/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                 SET           SET OFFSET  ##   
			##  22 BITS             O8 BITS          02 BITS    ##
			######################################################
			'''def write_cache(self, num_address, binary_address, tipo_cache):'''
			i = int(binary_address[22:30], 2) #SET NO FORMATO DECIMAL
			tag_dada_bin = binary_address[0:22]
			dado = int(num_address)
			### CHECANDO PRA VER SE EH MISS COMPULSORIO ###
			if self.table[i].bloco1.valid_bit == 0 and self.table[i].bloco2.valid_bit == 0:
				#COMPULSORY NA LATA... AZEDOU... JOGA PRO BLOCO 1
				if dado % 2 == 0:
					self.table[i].bloco1.word1 = dado
					self.table[i].bloco1.word2 = dado + 1
					self.table[i].bloco1.tag_bin = tag_dada_bin 
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif dado % 2 == 1:
					self.table[i].bloco1.word1 = dado - 1
					self.table[i].bloco1.word2 = dado 
					self.table[i].bloco1.tag_bin = tag_dada_bin 
					self.table[i].bloco1.valid_bit = 1
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				return 2
			elif self.table[i].bloco1.valid_bit == 1 and self.table[i].bloco2.valid_bit == 0:
				#TEM ALGO NO PRIMEIRO BLOCO... PODE SER QUE NAO SEJA O DADO. DAI CARREGA NO BLOCO 2
				if self.table[i].bloco1.tag_bin == tag_dada_bin:
					if dado % 2 == 0:
						if self.table[i].bloco1.word1 == dado:
							return 1
						elif self.table[i].bloco1.word1 == None:
							self.table[i].bloco2.word1 = dado
							self.table[i].bloco2.word2 = dado + 1
							self.table[i].bloco2.tag_bin = tag_dada_bin
							self.table[i].bloco2.valid_bit = 1
							self.table[i].livre += 1
							self.table[i].fifo.append(2)
							return 3
					elif dado % 2 == 1:
						if self.table[i].bloco1.word2 == dado:
							return 1
						elif self.table[i].bloco1.word2 == None:
							self.table[i].bloco2.word1 = dado - 1
							self.table[i].bloco2.word2 = dado
							self.table[i].bloco2.tag_bin = tag_dada_bin
							self.table[i].bloco2.valid_bit = 1
							self.table[i].livre += 1
							self.table[i].fifo.append(2)
							return 3
				if self.table[i].bloco1.tag_bin != tag_dada_bin:
					if dado % 2 == 0:
						self.table[i].bloco2.word1 = dado
						self.table[i].bloco2.word2 = dado + 1
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
						return 2
					elif dado % 2 == 1:
						self.table[i].bloco2.word1 = dado - 1
						self.table[i].bloco2.word2 = dado
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
						return 2
			elif self.table[i].bloco1.valid_bit == 1 and self.table[i].bloco2.valid_bit == 1:
				#TESTANDO PRA VER SE O DADO TA NO PRIMEIRO BLOCO DO SET
				if self.table[i].bloco1.tag_bin == tag_dada_bin:
					if dado % 2 == 0:
						if self.table[i].bloco1.word1 == dado:
							self.table[i].fifo.append(1)
							return 1
					elif dado % 2 == 1:
						if self.table[i].bloco1.word2 == dado:
							self.table[i].fifo.append(1)
							return 1
				#TESTANDO PRA VER SE O DADO TA NO SEGUNDO BLOCO DO SET
				elif self.table[i].bloco2.tag_bin == tag_dada_bin:
					if dado % 2 == 0:
						if self.table[i].bloco2.word1 == dado:
							self.table[i].fifo.append(2)
							return 1
					elif dado % 2 == 1:
						if self.table[i].bloco2.word2 == dado:
							self.table[i].fifo.append(2)
							return 1
				#NAO TA EM NENHUM DOS DOIS BLOCOS... PEGA O PRIMEIRO DA FILA E SOBRESCREVE... MISS POR CONFLITO...
				usado_ha_mais_tempo = self.table[i].fifo[0]
				self.table[i].fifo.pop(0)
				if usado_ha_mais_tempo == 1: #SOBRESCREVE NO BLOCO 1
					if dado % 2 == 0:
						self.table[i].bloco1.word1 = dado
						self.table[i].bloco1.word2 = dado + 1
						self.table[i].bloco1.tag_bin = tag_dada_bin 
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif dado % 2 == 1:
						self.table[i].bloco1.word1 = dado - 1
						self.table[i].bloco1.word2 = dado
						self.table[i].bloco1.tag_bin = tag_dada_bin 
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
				elif usado_ha_mais_tempo == 2: #SOBRESCREVE NO BLOCO 2
					if dado % 2 == 0:
						self.table[i].bloco2.word1 = dado
						self.table[i].bloco2.word2 = dado + 1
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 2 == 1:
						self.table[i].bloco2.word1 = dado - 1
						self.table[i].bloco2.word2 = dado
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
				return 3
		elif tipo_cache == 'B3':
			#TWO-WAY SET ASSOCIATIVE: 4 WORDs/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                 SET           SET OFFSET  ##   
			##  22 BITS             O7 BITS          03 BITS    ##
			######################################################
			'''def write_cache(self, num_address, binary_address, tipo_cache):'''
			i = int(binary_address[22:29], 2)
			tag_dada_bin = binary_address[0:22]
			dado = int(num_address)	
			if self.table[i].bloco1.valid_bit == 0 and self.table[i].bloco2.valid_bit == 0: #MISS COMPULSORY... JOGA PRO BLOCO 1
				if dado % 4 == 0:
					self.table[i].bloco1.word1 = dado
					self.table[i].bloco1.word2 = dado + 1
					self.table[i].bloco1.word3 = dado + 2
					self.table[i].bloco1.word4 = dado + 3
					self.table[i].bloco1.valid_bit = 1
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif dado % 4 == 1:
					self.table[i].bloco1.word1 = dado - 1
					self.table[i].bloco1.word2 = dado 
					self.table[i].bloco1.word3 = dado + 1
					self.table[i].bloco1.word4 = dado + 2
					self.table[i].bloco1.valid_bit = 1
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif dado % 4 == 2:
					self.table[i].bloco1.word1 = dado - 2
					self.table[i].bloco1.word2 = dado - 1
					self.table[i].bloco1.word3 = dado 
					self.table[i].bloco1.word4 = dado + 1
					self.table[i].bloco1.valid_bit = 1
					self.table[i].tag_bin = tag_dada_bin
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif dado % 4 == 3:
					self.table[i].bloco1.word1 = dado - 3
					self.table[i].bloco1.word2 = dado - 2
					self.table[i].bloco1.word3 = dado - 1
					self.table[i].bloco1.word4 = dado 
					self.table[i].bloco1.valid_bit = 1
					self.table[i].tag_bin = tag_dada_bin
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				return 2 #MISS COMPULSORY
			elif self.table[i].bloco1.valid_bit == 1 and self.table[i].bloco2.valid_bit == 0:
				if self.table[i].bloco1.tag_bin == tag_dada_bin:
					if dado % 4 == 0:
						if self.table[i].bloco1.word1 == dado:
							self.table[i].fifo.append(1)
							return 1
						elif self.table[i].bloco1.word1 == None:
							self.table[i].bloco2.word1 = dado
							self.table[i].bloco2.word2 = dado + 1
							self.table[i].bloco2.word3 = dado + 2
							self.table[i].bloco2.word4 = dado + 3
							self.table[i].bloco2.valid_bit = 1
							self.table[i].bloco2.tag_bin = tag_dada_bin
							self.table[i].livre += 1
							self.table[i].fifo.append(2)
							return 3
					elif dado % 4 == 1:
						if self.table[i].bloco1.word2 == dado:
							self.table[i].fifo.append(1)
							return 1
						elif self.table[i].bloco1.word2 == None:
							self.table[i].bloco2.word1 = dado - 1
							self.table[i].bloco2.word2 = dado 
							self.table[i].bloco2.word3 = dado + 1
							self.table[i].bloco2.word4 = dado + 2
							self.table[i].bloco2.valid_bit = 1
							self.table[i].bloco2.tag_bin = tag_dada_bin
							self.table[i].livre += 1
							self.table[i].fifo.append(2)
							return 3
					elif dado % 4 == 2:
						if self.table[i].bloco1.word3 == dado:
							self.table[i].fifo.append(1)
							return 1
						elif self.table[i].bloco1.word3 == None:
							self.table[i].bloco2.word1 = dado - 2
							self.table[i].bloco2.word2 = dado - 1
							self.table[i].bloco2.word3 = dado 
							self.table[i].bloco2.word4 = dado + 1
							self.table[i].bloco2.valid_bit = 1
							self.table[i].bloco2.tag_bin = tag_dada_bin
							self.table[i].livre += 1
							self.table[i].fifo.append(2)
							return 3
					elif dado % 4 == 3:
						if self.table[i].bloco1.word4 == dado:
							self.table[i].fifo.append(1)
							return 1
						elif self.table[i].bloco1.word4 == None:
							self.table[i].bloco2.word1 = dado - 3
							self.table[i].bloco2.word2 = dado - 2
							self.table[i].bloco2.word3 = dado - 1
							self.table[i].bloco2.word4 = dado
							self.table[i].bloco2.valid_bit = 1
							self.table[i].bloco2.tag_bin = tag_dada_bin
							self.table[i].livre += 1
							self.table[i].fifo.append(2)
							return 3
				elif self.table[i].bloco1.tag_bin != tag_dada_bin: #JOGA PRO BLOCO 2
					if dado % 4 == 0:
						self.table[i].bloco2.word1 = dado
						self.table[i].bloco2.word2 = dado + 1
						self.table[i].bloco2.word3 = dado + 2
						self.table[i].bloco2.word4 = dado + 3
						self.table[i].bloco2.valid_bit = 1
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 4 == 1:
						self.table[i].bloco2.word1 = dado - 1
						self.table[i].bloco2.word2 = dado 
						self.table[i].bloco2.word3 = dado + 1
						self.table[i].bloco2.word4 = dado + 2
						self.table[i].bloco2.valid_bit = 1
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 4 == 2:
						self.table[i].bloco2.word1 = dado - 2
						self.table[i].bloco2.word2 = dado - 1
						self.table[i].bloco2.word3 = dado 
						self.table[i].bloco2.word4 = dado + 1
						self.table[i].bloco2.valid_bit = 1
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 4 == 3:
						self.table[i].bloco2.word1 = dado - 3
						self.table[i].bloco2.word2 = dado - 2
						self.table[i].bloco2.word3 = dado - 1
						self.table[i].bloco2.word4 = dado
						self.table[i].bloco2.valid_bit = 1
						self.table[i].bloco2.tag_bin = tag_dada_bin
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					return 2
			elif self.table[i].bloco1.valid_bit == 1 and self.table[i].bloco2.valid_bit == 1:
				#TESTANDO PRA VER SE O DADO TA NO PRIMEIRO BLOCO DO SET
				if self.table[i].bloco1.tag_bin == tag_dada_bin:
					if dado % 4 == 0:
						if self.table[i].bloco1.word1 == dado:
							self.table[i].fifo.append(1)
							return 1
					elif dado % 4 == 1:
						if self.table[i].bloco1.word2 == dado:
							self.table[i].fifo.append(1)
							return 1
					elif dado % 4 == 2:
						if self.table[i].bloco1.word3 == dado:
							self.table[i].fifo.append(1)
							return 1
					elif dado % 4 == 3:
						if self.table[i].bloco1.word4 == dado:
							self.table[i].fifo.append(1)
							return 1
				#TESTANDO PRA VER SE O DADO TA NO SEGUNDO BLOCO DO SET
				elif self.table[i].bloco2.tag_bin == tag_dada_bin:
					if dado % 4 == 0:
						if self.table[i].bloco2.word1 == dado:
							self.table[i].fifo.append(2)
							return 1
					elif dado % 4 == 1:
						if self.table[i].bloco2.word2 == dado:
							self.table[i].fifo.append(2)
							return 1
					elif dado % 4 == 2:
						if self.table[i].bloco2.word3 == dado:
							self.table[i].fifo.append(2)
							return 1
					elif dado % 4 == 3:
						if self.table[i].bloco2.word4 == dado:
							self.table[i].fifo.append(2)
							return 1
				#NAO TA EM NENHUM DOS DOIS BLOCOS... PEGA O PRIMEIRO DA FILA E SOBRESCREVE... MISS POR CONFLITO...
				usado_ha_mais_tempo = self.table[i].fifo[0]
				self.table[i].fifo.pop(0)
				if usado_ha_mais_tempo == 1:
					if dado % 4 == 0:
						self.table[i].bloco1.word1 = dado
						self.table[i].bloco1.word2 = dado + 1
						self.table[i].bloco1.word3 = dado + 2
						self.table[i].bloco1.word4 = dado + 3
						self.table[i].bloco1.tag_bin = tag_dada_bin 
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif dado % 4 == 1:
						self.table[i].bloco1.word1 = dado - 1
						self.table[i].bloco1.word2 = dado 
						self.table[i].bloco1.word3 = dado + 1
						self.table[i].bloco1.word4 = dado + 2
						self.table[i].bloco1.tag_bin = tag_dada_bin 
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif dado % 4 == 2:
						self.table[i].bloco1.word1 = dado - 2
						self.table[i].bloco1.word2 = dado - 1
						self.table[i].bloco1.word3 = dado 
						self.table[i].bloco1.word4 = dado + 1
						self.table[i].bloco1.tag_bin = tag_dada_bin 
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif dado % 4 == 3:
						self.table[i].bloco1.word1 = dado - 3
						self.table[i].bloco1.word2 = dado - 2
						self.table[i].bloco1.word3 = dado - 1
						self.table[i].bloco1.word4 = dado 
						self.table[i].bloco1.tag_bin = tag_dada_bin 
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
				elif usado_ha_mais_tempo == 2:
					if dado % 4 == 0:
						self.table[i].bloco2.word1 = dado
						self.table[i].bloco2.word2 = dado + 1
						self.table[i].bloco2.word3 = dado + 2
						self.table[i].bloco2.word4 = dado + 3
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 4 == 1:
						self.table[i].bloco2.word1 = dado - 1
						self.table[i].bloco2.word2 = dado 
						self.table[i].bloco2.word3 = dado + 1
						self.table[i].bloco2.word4 = dado + 2
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 4 == 2:
						self.table[i].bloco2.word1 = dado - 2
						self.table[i].bloco2.word2 = dado - 1
						self.table[i].bloco2.word3 = dado 
						self.table[i].bloco2.word4 = dado + 1
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 4 == 3:
						self.table[i].bloco2.word1 = dado - 3
						self.table[i].bloco2.word2 = dado - 2
						self.table[i].bloco2.word3 = dado - 1
						self.table[i].bloco2.word4 = dado
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
				return 3
		elif tipo_cache == 'B4':
			#TWO-WAY SET ASSOCIATIVE: 8 WORDs/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                 SET           SET OFFSET  ##   
			##  22 BITS             O6 BITS          04 BITS    ##
			######################################################
			'''def write_cache(self, num_address, binary_address, tipo_cache):'''
			i = int(binary_address[22:28], 2)
			tag_dada_bin = binary_address[0:22]
			dado = int(num_address)
			if self.table[i].bloco1.valid_bit == 0 and self.table[i].bloco2.valid_bit == 0: #MISS COMPULSORY... JOGA PRO BLOCO 1
				if dado % 8 == 0:
					self.table[i].bloco1.word1 = dado
					self.table[i].bloco1.word2 = dado + 1
					self.table[i].bloco1.word3 = dado + 2
					self.table[i].bloco1.word4 = dado + 3
					self.table[i].bloco1.word5 = dado + 4
					self.table[i].bloco1.word6 = dado + 5
					self.table[i].bloco1.word7 = dado + 6
					self.table[i].bloco1.word8 = dado + 7
					self.table[i].bloco1.valid_bit = 1
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif dado % 8 == 1:
					self.table[i].bloco1.word1 = dado - 1
					self.table[i].bloco1.word2 = dado 
					self.table[i].bloco1.word3 = dado + 1
					self.table[i].bloco1.word4 = dado + 2
					self.table[i].bloco1.word5 = dado + 3
					self.table[i].bloco1.word6 = dado + 4
					self.table[i].bloco1.word7 = dado + 5
					self.table[i].bloco1.word8 = dado + 6
					self.table[i].bloco1.valid_bit = 1
					self.table[i].bloco1.tag_bin = tag_dada_bin
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif dado % 8 == 2:
					self.table[i].bloco1.word1 = dado - 2
					self.table[i].bloco1.word2 = dado - 1
					self.table[i].bloco1.word3 = dado 
					self.table[i].bloco1.word4 = dado + 1
					self.table[i].bloco1.word5 = dado + 2
					self.table[i].bloco1.word6 = dado + 3
					self.table[i].bloco1.word7 = dado + 4
					self.table[i].bloco1.word8 = dado + 5
					self.table[i].bloco1.valid_bit = 1
					self.table[i].tag_bin = tag_dada_bin
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif dado % 8 == 3:
					self.table[i].bloco1.word1 = dado - 3
					self.table[i].bloco1.word2 = dado - 2
					self.table[i].bloco1.word3 = dado - 1
					self.table[i].bloco1.word4 = dado 
					self.table[i].bloco1.word5 = dado + 1
					self.table[i].bloco1.word6 = dado + 2
					self.table[i].bloco1.word7 = dado + 3
					self.table[i].bloco1.word8 = dado + 4
					self.table[i].bloco1.valid_bit = 1
					self.table[i].tag_bin = tag_dada_bin
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif dado % 8 == 4:
					self.table[i].bloco1.word1 = dado - 4
					self.table[i].bloco1.word2 = dado - 3
					self.table[i].bloco1.word3 = dado - 2
					self.table[i].bloco1.word4 = dado - 1
					self.table[i].bloco1.word5 = dado 
					self.table[i].bloco1.word6 = dado + 1
					self.table[i].bloco1.word7 = dado + 2
					self.table[i].bloco1.word8 = dado + 3
					self.table[i].bloco1.valid_bit = 1
					self.table[i].tag_bin = tag_dada_bin
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif dado % 8 == 5:
					self.table[i].bloco1.word1 = dado - 5
					self.table[i].bloco1.word2 = dado - 4
					self.table[i].bloco1.word3 = dado - 3
					self.table[i].bloco1.word4 = dado - 2
					self.table[i].bloco1.word5 = dado - 1
					self.table[i].bloco1.word6 = dado 
					self.table[i].bloco1.word7 = dado + 1
					self.table[i].bloco1.word8 = dado + 2
					self.table[i].bloco1.valid_bit = 1
					self.table[i].tag_bin = tag_dada_bin
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif dado % 8 == 6:
					self.table[i].bloco1.word1 = dado - 6
					self.table[i].bloco1.word2 = dado - 5
					self.table[i].bloco1.word3 = dado - 4
					self.table[i].bloco1.word4 = dado - 3
					self.table[i].bloco1.word5 = dado - 2
					self.table[i].bloco1.word6 = dado - 1
					self.table[i].bloco1.word7 = dado 
					self.table[i].bloco1.word8 = dado + 1
					self.table[i].bloco1.valid_bit = 1
					self.table[i].tag_bin = tag_dada_bin
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				elif dado % 8 == 7:
					self.table[i].bloco1.word1 = dado - 7
					self.table[i].bloco1.word2 = dado - 6
					self.table[i].bloco1.word3 = dado - 5
					self.table[i].bloco1.word4 = dado - 4
					self.table[i].bloco1.word5 = dado - 3
					self.table[i].bloco1.word6 = dado - 2
					self.table[i].bloco1.word7 = dado - 1
					self.table[i].bloco1.word8 = dado 
					self.table[i].bloco1.valid_bit = 1
					self.table[i].tag_bin = tag_dada_bin
					self.table[i].livre += 1
					self.table[i].fifo.append(1)
				return 2 #MISS COMPULSORY
			elif self.table[i].bloco1.valid_bit == 1 and self.table[i].bloco2.valid_bit == 0:
				if self.table[i].bloco1.tag_bin == tag_dada_bin:
					if dado % 8 == 0:
						if self.table[i].bloco1.word1 == dado:
							self.table[i].fifo.append(1)
							return 1
						elif self.table[i].bloco1.word1 == None:
							self.table[i].bloco2.word1 = dado
							self.table[i].bloco2.word2 = dado + 1
							self.table[i].bloco2.word3 = dado + 2
							self.table[i].bloco2.word4 = dado + 3
							self.table[i].bloco2.word5 = dado + 4
							self.table[i].bloco2.word6 = dado + 5
							self.table[i].bloco2.word7 = dado + 6
							self.table[i].bloco2.word8 = dado + 7
							self.table[i].bloco2.valid_bit = 1
							self.table[i].bloco2.tag_bin = tag_dada_bin
							self.table[i].livre += 1
							self.table[i].fifo.append(2)
							return 3
					elif dado % 8 == 1:
						if self.table[i].bloco1.word2 == dado:
							self.table[i].fifo.append(1)
							return 1
						elif self.table[i].bloco1.word2 == None:
							self.table[i].bloco2.word1 = dado - 1
							self.table[i].bloco2.word2 = dado 
							self.table[i].bloco2.word3 = dado + 1
							self.table[i].bloco2.word4 = dado + 2
							self.table[i].bloco2.word5 = dado + 3
							self.table[i].bloco2.word6 = dado + 4
							self.table[i].bloco2.word7 = dado + 5
							self.table[i].bloco2.word8 = dado + 6
							self.table[i].bloco2.valid_bit = 1
							self.table[i].bloco2.tag_bin = tag_dada_bin
							self.table[i].livre += 1
							self.table[i].fifo.append(2)
							return 3
					elif dado % 8 == 2:
						if self.table[i].bloco1.word3 == dado:
							self.table[i].fifo.append(1)
							return 1
						elif self.table[i].bloco1.word3 == None:
							self.table[i].bloco2.word1 = dado - 2
							self.table[i].bloco2.word2 = dado - 1
							self.table[i].bloco2.word3 = dado 
							self.table[i].bloco2.word4 = dado + 1
							self.table[i].bloco2.word5 = dado + 2
							self.table[i].bloco2.word6 = dado + 3
							self.table[i].bloco2.word7 = dado + 4
							self.table[i].bloco2.word8 = dado + 5
							self.table[i].bloco2.valid_bit = 1
							self.table[i].bloco2.tag_bin = tag_dada_bin
							self.table[i].livre += 1
							self.table[i].fifo.append(2)
							return 3
					elif dado % 8 == 3:
						if self.table[i].bloco1.word4 == dado:
							self.table[i].fifo.append(1)
							return 1
						elif self.table[i].bloco1.word4 == None:
							self.table[i].bloco2.word1 = dado - 3
							self.table[i].bloco2.word2 = dado - 2
							self.table[i].bloco2.word3 = dado - 1
							self.table[i].bloco2.word4 = dado
							self.table[i].bloco2.word5 = dado + 1
							self.table[i].bloco2.word6 = dado + 2
							self.table[i].bloco2.word7 = dado + 3
							self.table[i].bloco2.word8 = dado + 4
							self.table[i].bloco2.valid_bit = 1
							self.table[i].bloco2.tag_bin = tag_dada_bin
							self.table[i].livre += 1
							self.table[i].fifo.append(2)
							return 3
					elif dado % 8 == 4:
						if self.table[i].bloco1.word5 == dado:
							self.table[i].fifo.append(1)
							return 1
						elif self.table[i].bloco1.word5 == None:
							self.table[i].bloco2.word1 = dado - 4
							self.table[i].bloco2.word2 = dado - 3
							self.table[i].bloco2.word3 = dado - 2
							self.table[i].bloco2.word4 = dado - 1
							self.table[i].bloco2.word5 = dado 
							self.table[i].bloco2.word6 = dado + 1
							self.table[i].bloco2.word7 = dado + 2
							self.table[i].bloco2.word8 = dado + 3
							self.table[i].bloco2.valid_bit = 1
							self.table[i].bloco2.tag_bin = tag_dada_bin
							self.table[i].livre += 1
							self.table[i].fifo.append(2)
							return 3
					elif dado % 8 == 5:
						if self.table[i].bloco1.word6 == dado:
							self.table[i].fifo.append(1)
							return 1
						elif self.table[i].bloco1.word6 == None:
							self.table[i].bloco2.word1 = dado - 5
							self.table[i].bloco2.word2 = dado - 4
							self.table[i].bloco2.word3 = dado - 3
							self.table[i].bloco2.word4 = dado - 2
							self.table[i].bloco2.word5 = dado - 1
							self.table[i].bloco2.word6 = dado 
							self.table[i].bloco2.word7 = dado + 1
							self.table[i].bloco2.word8 = dado + 2
							self.table[i].bloco2.valid_bit = 1
							self.table[i].bloco2.tag_bin = tag_dada_bin
							self.table[i].livre += 1
							self.table[i].fifo.append(2)
							return 3
					elif dado % 8 == 6:
						if self.table[i].bloco1.word7 == dado:
							self.table[i].fifo.append(1)
							return 1
						elif self.table[i].bloco1.word7 == None:
							self.table[i].bloco2.word1 = dado - 6
							self.table[i].bloco2.word2 = dado - 5
							self.table[i].bloco2.word3 = dado - 4
							self.table[i].bloco2.word4 = dado - 3
							self.table[i].bloco2.word5 = dado - 2
							self.table[i].bloco2.word6 = dado - 1
							self.table[i].bloco2.word7 = dado 
							self.table[i].bloco2.word8 = dado + 1
							self.table[i].bloco2.valid_bit = 1
							self.table[i].bloco2.tag_bin = tag_dada_bin
							self.table[i].livre += 1
							self.table[i].fifo.append(2)
							return 3
					elif dado % 8 == 7:
						if self.table[i].bloco1.word8 == dado:
							self.table[i].fifo.append(1)
							return 1
						elif self.table[i].bloco1.word8 == None:
							self.table[i].bloco2.word1 = dado - 7
							self.table[i].bloco2.word2 = dado - 6
							self.table[i].bloco2.word3 = dado - 5
							self.table[i].bloco2.word4 = dado - 4
							self.table[i].bloco2.word5 = dado - 3
							self.table[i].bloco2.word6 = dado - 2
							self.table[i].bloco2.word7 = dado - 1
							self.table[i].bloco2.word8 = dado 
							self.table[i].bloco2.valid_bit = 1
							self.table[i].bloco2.tag_bin = tag_dada_bin
							self.table[i].livre += 1
							self.table[i].fifo.append(2)
							return 3
				elif self.table[i].bloco1.tag_bin != tag_dada_bin: #JOGA PRO BLOCO 2
					if dado % 8 == 0:
						self.table[i].bloco2.word1 = dado
						self.table[i].bloco2.word2 = dado + 1
						self.table[i].bloco2.word3 = dado + 2
						self.table[i].bloco2.word4 = dado + 3
						self.table[i].bloco2.word5 = dado + 4
						self.table[i].bloco2.word6 = dado + 5
						self.table[i].bloco2.word7 = dado + 6
						self.table[i].bloco2.word8 = dado + 7
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 8 == 1:
						self.table[i].bloco2.word1 = dado - 1
						self.table[i].bloco2.word2 = dado 
						self.table[i].bloco2.word3 = dado + 1
						self.table[i].bloco2.word4 = dado + 2
						self.table[i].bloco2.word5 = dado + 3
						self.table[i].bloco2.word6 = dado + 4
						self.table[i].bloco2.word7 = dado + 5
						self.table[i].bloco2.word8 = dado + 6
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 8 == 2:
						self.table[i].bloco2.word1 = dado - 2
						self.table[i].bloco2.word2 = dado - 1
						self.table[i].bloco2.word3 = dado 
						self.table[i].bloco2.word4 = dado + 1
						self.table[i].bloco2.word5 = dado + 2
						self.table[i].bloco2.word6 = dado + 3
						self.table[i].bloco2.word7 = dado + 4
						self.table[i].bloco2.word8 = dado + 5
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 8 == 3:
						self.table[i].bloco2.word1 = dado - 3
						self.table[i].bloco2.word2 = dado - 2
						self.table[i].bloco2.word3 = dado - 1
						self.table[i].bloco2.word4 = dado 
						self.table[i].bloco2.word5 = dado + 1
						self.table[i].bloco2.word6 = dado + 2
						self.table[i].bloco2.word7 = dado + 3
						self.table[i].bloco2.word8 = dado + 4
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 8 == 4:
						self.table[i].bloco2.word1 = dado - 4
						self.table[i].bloco2.word2 = dado - 3
						self.table[i].bloco2.word3 = dado - 2
						self.table[i].bloco2.word4 = dado - 1
						self.table[i].bloco2.word5 = dado 
						self.table[i].bloco2.word6 = dado + 1
						self.table[i].bloco2.word7 = dado + 2
						self.table[i].bloco2.word8 = dado + 3
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 8 == 5:
						self.table[i].bloco2.word1 = dado - 5
						self.table[i].bloco2.word2 = dado - 4
						self.table[i].bloco2.word3 = dado - 3
						self.table[i].bloco2.word4 = dado - 2
						self.table[i].bloco2.word5 = dado - 1
						self.table[i].bloco2.word6 = dado 
						self.table[i].bloco2.word7 = dado + 1
						self.table[i].bloco2.word8 = dado + 2
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 8 == 6:
						self.table[i].bloco2.word1 = dado - 6
						self.table[i].bloco2.word2 = dado - 5
						self.table[i].bloco2.word3 = dado - 4
						self.table[i].bloco2.word4 = dado - 3
						self.table[i].bloco2.word5 = dado - 2
						self.table[i].bloco2.word6 = dado - 1
						self.table[i].bloco2.word7 = dado 
						self.table[i].bloco2.word8 = dado + 1
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 8 == 7:
						self.table[i].bloco2.word1 = dado - 7
						self.table[i].bloco2.word2 = dado - 6
						self.table[i].bloco2.word3 = dado - 5
						self.table[i].bloco2.word4 = dado - 4
						self.table[i].bloco2.word5 = dado - 3
						self.table[i].bloco2.word6 = dado - 2
						self.table[i].bloco2.word7 = dado - 1
						self.table[i].bloco2.word8 = dado
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					return 2
			elif self.table[i].bloco1.valid_bit == 1 and self.table[i].bloco2.valid_bit == 1:
				#TESTANDO PRA VER SE O DADO TA NO PRIMEIRO BLOCO DO SET
				if self.table[i].bloco1.tag_bin == tag_dada_bin:
					if dado % 8 == 0:
						if self.table[i].bloco1.word1 == dado:
							self.table[i].fifo.append(1)
							return 1
					elif dado % 8 == 1:
						if self.table[i].bloco1.word2 == dado:
							self.table[i].fifo.append(1)
							return 1
					elif dado % 8 == 2:
						if self.table[i].bloco1.word3 == dado:
							self.table[i].fifo.append(1)
							return 1
					elif dado % 8 == 3:
						if self.table[i].bloco1.word4 == dado:
							self.table[i].fifo.append(1)
							return 1
					elif dado % 8 == 4:
						if self.table[i].bloco1.word5 == dado:
							self.table[i].fifo.append(1)
							return 1
					elif dado % 8 == 5:
						if self.table[i].bloco1.word6 == dado:
							self.table[i].fifo.append(1)
							return 1
					elif dado % 8 == 6:
						if self.table[i].bloco1.word7 == dado:
							self.table[i].fifo.append(1)
							return 1
					elif dado % 8 == 7:
						if self.table[i].bloco1.word8 == dado:
							self.table[i].fifo.append(1)
							return 1
				#TESTANDO PRA VER SE O DADO TA NO SEGUNDO BLOCO DO SET
				elif self.table[i].bloco2.tag_bin == tag_dada_bin:
					if dado % 8 == 0:
						if self.table[i].bloco2.word1 == dado:
							self.table[i].fifo.append(2)
							return 1
					elif dado % 8 == 1:
						if self.table[i].bloco2.word2 == dado:
							self.table[i].fifo.append(2)
							return 1
					elif dado % 8 == 2:
						if self.table[i].bloco2.word3 == dado:
							self.table[i].fifo.append(2)
							return 1
					elif dado % 8 == 3:
						if self.table[i].bloco2.word4 == dado:
							self.table[i].fifo.append(2)
							return 1
					elif dado % 8 == 4:
						if self.table[i].bloco2.word5 == dado:
							self.table[i].fifo.append(2)
							return 1
					elif dado % 8 == 5:
						if self.table[i].bloco2.word6 == dado:
							self.table[i].fifo.append(2)
							return 1
					elif dado % 8 == 6:
						if self.table[i].bloco2.word7 == dado:
							self.table[i].fifo.append(2)
							return 1
					elif dado % 8 == 7:
						if self.table[i].bloco2.word8 == dado:
							self.table[i].fifo.append(2)
							return 1
				#NAO TA EM NENHUM DOS DOIS BLOCOS... PEGA O PRIMEIRO DA FILA E SOBRESCREVE... MISS POR CONFLITO...
				usado_ha_mais_tempo = self.table[i].fifo[0]
				self.table[i].fifo.pop(0)
				if usado_ha_mais_tempo == 1:
					if dado % 8 == 0:
						self.table[i].bloco1.word1 = dado
						self.table[i].bloco1.word2 = dado + 1
						self.table[i].bloco1.word3 = dado + 2
						self.table[i].bloco1.word4 = dado + 3
						self.table[i].bloco1.word5 = dado + 4
						self.table[i].bloco1.word6 = dado + 5
						self.table[i].bloco1.word7 = dado + 6
						self.table[i].bloco1.word8 = dado + 7
						self.table[i].bloco1.tag_bin = tag_dada_bin 
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif dado % 8 == 1:
						self.table[i].bloco1.word1 = dado - 1
						self.table[i].bloco1.word2 = dado 
						self.table[i].bloco1.word3 = dado + 1
						self.table[i].bloco1.word4 = dado + 2
						self.table[i].bloco1.word5 = dado + 3
						self.table[i].bloco1.word6 = dado + 4
						self.table[i].bloco1.word7 = dado + 5
						self.table[i].bloco1.word8 = dado + 6
						self.table[i].bloco1.tag_bin = tag_dada_bin 
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif dado % 8 == 2:
						self.table[i].bloco1.word1 = dado - 2
						self.table[i].bloco1.word2 = dado - 1
						self.table[i].bloco1.word3 = dado 
						self.table[i].bloco1.word4 = dado + 1
						self.table[i].bloco1.word5 = dado + 2
						self.table[i].bloco1.word6 = dado + 3
						self.table[i].bloco1.word7 = dado + 4
						self.table[i].bloco1.word8 = dado + 5
						self.table[i].bloco1.tag_bin = tag_dada_bin 
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif dado % 8 == 3:
						self.table[i].bloco1.word1 = dado - 3
						self.table[i].bloco1.word2 = dado - 2
						self.table[i].bloco1.word3 = dado - 1
						self.table[i].bloco1.word4 = dado 
						self.table[i].bloco1.word5 = dado + 1
						self.table[i].bloco1.word6 = dado + 2
						self.table[i].bloco1.word7 = dado + 3
						self.table[i].bloco1.word8 = dado + 4
						self.table[i].bloco1.tag_bin = tag_dada_bin 
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif dado % 8 == 4:
						self.table[i].bloco1.word1 = dado - 4
						self.table[i].bloco1.word2 = dado - 3
						self.table[i].bloco1.word3 = dado - 2
						self.table[i].bloco1.word4 = dado - 1
						self.table[i].bloco1.word5 = dado 
						self.table[i].bloco1.word6 = dado + 1
						self.table[i].bloco1.word7 = dado + 2
						self.table[i].bloco1.word8 = dado + 3
						self.table[i].bloco1.tag_bin = tag_dada_bin 
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif dado % 8 == 5:
						self.table[i].bloco1.word1 = dado - 5
						self.table[i].bloco1.word2 = dado - 4
						self.table[i].bloco1.word3 = dado - 3
						self.table[i].bloco1.word4 = dado - 2
						self.table[i].bloco1.word5 = dado - 1
						self.table[i].bloco1.word6 = dado 
						self.table[i].bloco1.word7 = dado + 1
						self.table[i].bloco1.word8 = dado + 2
						self.table[i].bloco1.tag_bin = tag_dada_bin 
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif dado % 8 == 6:
						self.table[i].bloco1.word1 = dado - 6
						self.table[i].bloco1.word2 = dado - 5
						self.table[i].bloco1.word3 = dado - 4
						self.table[i].bloco1.word4 = dado - 3
						self.table[i].bloco1.word5 = dado - 2
						self.table[i].bloco1.word6 = dado - 1
						self.table[i].bloco1.word7 = dado 
						self.table[i].bloco1.word8 = dado + 1
						self.table[i].bloco1.tag_bin = tag_dada_bin 
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
					elif dado % 8 == 7:
						self.table[i].bloco1.word1 = dado - 7
						self.table[i].bloco1.word2 = dado - 6
						self.table[i].bloco1.word3 = dado - 5
						self.table[i].bloco1.word4 = dado - 4
						self.table[i].bloco1.word5 = dado - 3
						self.table[i].bloco1.word6 = dado - 2
						self.table[i].bloco1.word7 = dado - 1
						self.table[i].bloco1.word8 = dado
						self.table[i].bloco1.tag_bin = tag_dada_bin 
						self.table[i].bloco1.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(1)
				elif usado_ha_mais_tempo == 2:
					if dado % 8 == 0:
						self.table[i].bloco2.word1 = dado
						self.table[i].bloco2.word2 = dado + 1
						self.table[i].bloco2.word3 = dado + 2
						self.table[i].bloco2.word4 = dado + 3
						self.table[i].bloco2.word5 = dado + 4
						self.table[i].bloco2.word6 = dado + 5
						self.table[i].bloco2.word7 = dado + 6
						self.table[i].bloco2.word8 = dado + 7
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 8 == 1:
						self.table[i].bloco2.word1 = dado - 1
						self.table[i].bloco2.word2 = dado 
						self.table[i].bloco2.word3 = dado + 1
						self.table[i].bloco2.word4 = dado + 2
						self.table[i].bloco2.word5 = dado + 3
						self.table[i].bloco2.word6 = dado + 4
						self.table[i].bloco2.word7 = dado + 5
						self.table[i].bloco2.word8 = dado + 6
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 8 == 2:
						self.table[i].bloco2.word1 = dado - 2
						self.table[i].bloco2.word2 = dado - 1
						self.table[i].bloco2.word3 = dado 
						self.table[i].bloco2.word4 = dado + 1
						self.table[i].bloco2.word5 = dado + 2
						self.table[i].bloco2.word6 = dado + 3
						self.table[i].bloco2.word7 = dado + 4
						self.table[i].bloco2.word8 = dado + 5
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 8 == 3:
						self.table[i].bloco2.word1 = dado - 3
						self.table[i].bloco2.word2 = dado - 2
						self.table[i].bloco2.word3 = dado - 1
						self.table[i].bloco2.word4 = dado 
						self.table[i].bloco2.word5 = dado + 1
						self.table[i].bloco2.word6 = dado + 2
						self.table[i].bloco2.word7 = dado + 3
						self.table[i].bloco2.word8 = dado + 4
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 8 == 4:
						self.table[i].bloco2.word1 = dado - 4
						self.table[i].bloco2.word2 = dado - 3
						self.table[i].bloco2.word3 = dado - 2
						self.table[i].bloco2.word4 = dado - 1
						self.table[i].bloco2.word5 = dado 
						self.table[i].bloco2.word6 = dado + 1
						self.table[i].bloco2.word7 = dado + 2
						self.table[i].bloco2.word8 = dado + 3
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 8 == 5:
						self.table[i].bloco2.word1 = dado - 5
						self.table[i].bloco2.word2 = dado - 4
						self.table[i].bloco2.word3 = dado - 3
						self.table[i].bloco2.word4 = dado - 2
						self.table[i].bloco2.word5 = dado - 1
						self.table[i].bloco2.word6 = dado 
						self.table[i].bloco2.word7 = dado + 1
						self.table[i].bloco2.word8 = dado + 2
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 8 == 6:
						self.table[i].bloco2.word1 = dado - 6
						self.table[i].bloco2.word2 = dado - 5
						self.table[i].bloco2.word3 = dado - 4
						self.table[i].bloco2.word4 = dado - 3
						self.table[i].bloco2.word5 = dado - 2
						self.table[i].bloco2.word6 = dado - 1
						self.table[i].bloco2.word7 = dado 
						self.table[i].bloco2.word8 = dado + 1
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
					elif dado % 8 == 7:
						self.table[i].bloco2.word1 = dado - 7
						self.table[i].bloco2.word2 = dado - 6
						self.table[i].bloco2.word3 = dado - 5
						self.table[i].bloco2.word4 = dado - 4
						self.table[i].bloco2.word5 = dado - 3
						self.table[i].bloco2.word6 = dado - 2
						self.table[i].bloco2.word7 = dado - 1
						self.table[i].bloco2.word8 = dado
						self.table[i].bloco2.tag_bin = tag_dada_bin 
						self.table[i].bloco2.valid_bit = 1
						self.table[i].livre += 1
						self.table[i].fifo.append(2)
				return 3
		elif tipo_cache == 'C1':
			#FOUR-WAY SET ASSOCIATIVE WITH 1 WORD/BLOCK
			######################################################
			##          CONFIGURACAO DO ENDERECO 32 BITS        ##
			##    TAG                 SET           SET OFFSET  ##   
			##  22 BITS             O8 BITS          02 BITS    ##
			######################################################
			i = int(binary_address[22:30], 2)
			tag_dada_bin = binary_address[0:22]
			dado = int(num_address)
			if self.table[i].bloco1.valid_bit == 0 and self.table[i].bloco2.valid_bit == 0 and self.table[i].bloco3.valid_bit == 0 and self.table[i].bloco4.valid_bit == 0: #MISS COMPULSORY... JOGA PRO BLOCO 1


		elif tipo_cache == 'C2':
			pass
		elif tipo_cache == 'C3':
			pass
		elif tipo_cache == 'C4':
			pass
		elif tipo_cache == 'D1':
			pass
		elif tipo_cache == 'D2':
			pass
		elif tipo_cache == 'D3':
			pass
		elif tipo_cache == 'D4':
			pass
		
		

