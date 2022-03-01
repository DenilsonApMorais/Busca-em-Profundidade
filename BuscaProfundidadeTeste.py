mapa = {
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


grafo = [ [1, 2], # vizinhos do noh 0
	 [0, 4, 5],  # vizinhos do no 1
	 [0, 3], #vizinhos do noh 2
	 [2, 5, 7], #vizinhos do noh 3
	 [1, 6], #vizinhos do noh 4
	 [1, 3, 6, 8], #vizinhos do noh 5
	 [4, 5, 9], #vizinhos do noh 6
	 [3, 10], #vizinhos do noh 7
	 [5, 9, 10], #vizinhos do noh 8
	 [6, 8, 10], #vizinhos do noh 9
	 [7, 8, 9]] #vizinhos do noh 10

	 
visitados = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

def busca(origem, destino):
	pilha = [] 
	pilha.append(origem) # Adciona a origem na pilha
	while len(pilha) > 0: # Enquanto tiver elementos na pilha 
		noAtual = pilha.pop()  # Desempilha no no atual
		if visitados[noAtual] == -1: # Se o nó atual ainda não foi visitado
			visitados[noAtual] = 1   # Marque-o como visitado
			print(mapa[noAtual])   # mostra o caminho que estamos percorrendo 
			if noAtual == destino:  #se encontramos o alvo paramos
				print("Destino Encontrado!")
				break
			else:
				for noh in grafo[noAtual]: # se não encontrou adcione o proximo nó a pilha
					pilha.append(noh)



print("""As cidade disponíveis são:
0: Montes Claros
1: Diamantina
2: Uberlândia
3: Uberaba
4: Governador Valadares
5: Belo Horizonte
6: Ipatinga
7: Poços de Caldas
8: São João Del Dey
9: juiz de Fora
10: São Lourenço
""")

origem = int(input('Digite a origem: '))
destino = int(input('Digite o destino: '))

busca(origem, destino)
