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
			self.block_offset = None
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
					return 1
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
					return 1
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
				elif num_address % 8 == 3:
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
					return 1
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
					elif num_address % 8 == 3:
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
			pass '''
		

