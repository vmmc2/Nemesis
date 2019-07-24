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
		#BLOCK WITH 3 WORDS PER BLOCK
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
		#BLOCK WITH 4 WORDS PER BLOCK
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




class Cache:
	def __init__(self, tipo): #Esse metodo inicial eh responsavel por realizar a inicializacao da cache.
		#Cache Direct-Mapping: 1 word/block
		if tipo == 'A1':
			self.tipo = 'A1'
			self.numero_indices = 1024 #range (0 ate 1023)
			self.table = []
			for element in range(0, 1024):
				bloco = Block("A1")
				self.table.append(bloco)
		#Cache Direct-Mapping: 2 words/block
		elif tipo == 'A2':
			self.tipo = 'A2'
			self.numero_indices = 512  #range(0 a 511)
			self.table = []
			for element in range(0, 512):
				bloco = Block("A2")
				self.table.append(bloco)
		#Cache Direct-Mapping: 4 words/block
		elif tipo == 'A3':
			self.tipo = 'A3'
			self.numero_indices = 256  #range(0 a 255)
			self.table = []
			for element in range(0, 256):
				bloco = Block("A3")
				self.table.append(bloco)
		#Cache Direct-Mapping: 8 words/block
		elif tipo == 'A4':
			self.tipo = 'A4'
			self.numero_indices = 128  #range(0 a 127)
			self.table = []
			for element in range(0, 128):
				bloco = Block("A4")
				self.table.append(bloco)
		else:
			print("Ai ja eh set-associative. Nao ta implementado ainda")

	def print_cache(self):
		if self.tipo == 'A1':
			for i in range (0, 1024):
				sentence = f"Index: {i:04} ---- Valid Bit: {self.table[i].valid_bit} ---- Tag: {self.table[i].tag_bin} ---- Data: {self.table[i].word1}"
				print(sentence)
		elif self.tipo == 'A2':
			for i in range(0, 512):
				sentence = f"Index: {i:03} ---- Valid Bit: {self.table[i].valid_bit} ---- Tag: {self.table[i].tag_dec} ---- Word1: {self.table[i].word1} ---- Word2: {self.table[i].word2}"
				print(sentence)
		elif self.tipo == 'A3':
			for i in range(0, 256):
				sentence = f"Index: {i:03} ---- Valid Bit: {self.table[i].valid_bit} ---- Tag: {self.table[i].tag_dec} ---- Word1: {self.table[i].word1} ---- Word2: {self.table[i].word2}"
				print(sentence)
				sentence2 = f"                                                 Word3: {self.table[i].word3} ---- Word4: {self.table[i].word4}"
				print(sentence2)
				print(" ")
		elif self.tipo == 'A4':
			for i in range(0, 128):
				sentence = f"Index: {i:03} ---- Valid Bit: {self.table[i].valid_bit} ---- Tag: {self.table[i].tag_dec} ---- Word1: {self.table[i].word1} ---- Word2: {self.table[i].word2}"
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

	def write_cache(self, num_address, data, binary_address, tipo_cache):
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
			self.table[i].word1 = data
			self.table[i].valid_bit = 1;
		elif tipo_cache == 'A2':
			pass
		elif tipo_cache == 'A3':
			pass
		elif tipo_cache == 'A4':
			pass
		elif tipo_cache == 'B1':
			pass
		elif tipo_cache == 'B2':
			pass
		elif tipo_cache == 'B3':
			pass
		elif tipo_cache == 'B4':
			pass
		elif tipo_cache == 'C1':
			pass
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
		elif tipo_cache == 'E1':
			pass
		elif tipo_cache == 'E2':
			pass
		elif tipo_cache == 'E3':
			pass
		elif tipo_cache == 'E4':
			pass

	def read_cache(self, num_address, data, binary_address, tipo_cache):
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
				return 2
			elif self.table[i].valid_bit == 1:
				#E AGORA?
			pass
		elif tipo_cache == 'A2':
			pass
		elif tipo_cache == 'A3':
			pass
		elif tipo_cache == 'A4':
			pass
		elif tipo_cache == 'B1':
			pass
		elif tipo_cache == 'B2':
			pass
		elif tipo_cache == 'B3':
			pass
		elif tipo_cache == 'B4':
			pass
		elif tipo_cache == 'C1':
			pass
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
		elif tipo_cache == 'E1':
			pass
		elif tipo_cache == 'E2':
			pass
		elif tipo_cache == 'E3':
			pass
		elif tipo_cache == 'E4':
			pass


