class BuscaProf:

	def __init__(self):
		self.visitados = [-1]*11
		self.mapa = {
		0: 'Montes Claros',
		1: 'Diamantina',
		2: 'Uberlândia',
		3: 'Uberaba',
		4: 'Governador Valadares',
		5: 'Belo Horizonte',
		6: 'Ipatinga',
		7: 'Poços de Caldas',
		8: 'São João Del Dey',
		9: 'juiz de Fora',
		10: 'São Lourenço'}

		self.grafo = [ [1, 2], # vizinhos do no 0
		[0, 4, 5],  # vizinhos do no 1
		[0, 3], #vizinhos do no 2
		[2, 5, 7], #vizinhos do no 3
		[1, 6], #vizinhos do no 4
		[1, 3, 6, 8], #vizinhos do no 5
		[4, 5, 9], #vizinhos do no 6
		[3, 10], #vizinhos do no 7
		[5, 9, 10], #vizinhos do no 8
		[6, 8, 10], #vizinhos do no 9
		[7, 8, 9]] #vizinhos do no 10
	

	def busca(self,origem, destino):
		
		pilha = [] 
		pilha.append(origem) # Adciona a origem na pilha
		while len(pilha) > 0: # Enquanto tiver elementos na pilha 
			noAtual = pilha.pop()  # Desempilha no no atual	

			if self.visitados[noAtual] == -1: # Se o nó atual ainda não foi visitado
				self.visitados[noAtual] = 1   # Marque-o como visitado

				try:
					if destino == self.grafo[noAtual][0] or destino == self.grafo[noAtual][1] or destino == self.grafo[noAtual][2]:
						print (self.mapa[noAtual])
						print(self.mapa[destino])
						print("\nDestino Encontrado!")

						break
				except:
					print(end ='')	

				print(self.mapa[noAtual])  # mostra o caminho que estamos percorrendo


				if noAtual == destino:  #se encontramos o alvo paramos
					print("\nDestino Encontrado!")
					break
				else:

					for no in self.grafo[noAtual]: 			
						pilha.append(no)# se não encontrou adcione o proximo nó a pilha


