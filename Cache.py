class Block():
	def __init__(self, tipo): #Mesmo esquema: A1. A2. A3. A4. B1,...., E4
		#BLOCK WITH 1 WORD PER BLOCK
		if tipo == 'A1':
			self.valid_bit = 0
			self.tag_dec = None
			self.tag_bin = None
			self.tag_hex = None
			self.word1 = None
		#BLOCK WITH 2 WORDS PER BLOCK
		elif tipo == 'A2':
			self.valid_bit = 0
			self.tag_dec = None
			self.tag_bin = None
			self.tag_hex = None
			self.word1 = None
			self.word2 = None
		#BLOCK WITH 3 WORDS PER BLOCK
		elif tipo == 'A3':
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
				sentence = f"Index: {i:04} ---- Valid Bit: {self.table[i].valid_bit} ---- Tag: {self.table[i].tag_dec} ---- Data: {self.table[i].word1}"
				print(sentence)
		else:
			pass
