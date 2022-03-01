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

	 
visitados = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,]

def busca(origem, destino):
	pilha = []
	#pdb.set_trace()
	pilha.append(origem) # equivale ao push
	while len(pilha) > 0:
		noAtual = pilha.pop()
		if visitados[noAtual] == -1:
			visitados[noAtual] = 1
			print(mapa[noAtual])
			if noAtual == destino:
				print("Destino Encontrado!")
				break
			else:
				for noh in grafo[noAtual]:
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



