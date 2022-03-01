mD = {
0: 'F',
1: 'MO',
2: 'JU',
3: 'P',
4: 'N',
5: 'CG',
6: 'JP',
7: 'A',
8: 'CA',
9: 'JP',
10: 'R',
11: 'MA'}

grafo = [ [1, 2], # vizinhos do noh 0
	 [0, 4, 5],  # vizinhos do no 1
	 [0, 3], #vizinhos do noh 2
	 [2, 5, 7], #vizinhos do noh 3
	 [1, 6], #vizinhos do noh 4
	 [1, 3, 6, 8], #vizinhos do noh 5
	 [4, 5, 10], #vizinhos do noh 6
	 [3, 11], #vizinhos do noh 7
	 [5, 10, 11], #vizinhos do noh 8
	 [4, 5, 10], #vizinhos do noh 9
	 [6, 8, 11], #vizinhos do noh 10
	 [7, 8, 10]] #vizinhos do noh 11
	 
nohsVisitados = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
nohPartida = 0
nohChegada = 4

def busca_em_profundidade(nohPartida, nohChegada):
	pilha = []
	#pdb.set_trace()
	pilha.append(nohPartida) # equivale ao push
	while len(pilha) > 0:
		nohDaVez = pilha.pop()
		if nohsVisitados[nohDaVez] == 0:
			nohsVisitados[nohDaVez] = 1
			print(mD[nohDaVez])
			if nohDaVez == nohChegada:
				print("Chegou ao destino")
				break
			else:
				for noh in grafo[nohDaVez]:
					pilha.append(noh)



busca_em_profundidade(nohPartida, nohChegada)



