from BuscaProfundidadeTeste import BuscaProf


if __name__ == '__main__':
    
	
	obj = BuscaProf()

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

	while True:

		origem = int(input('Digite a origem: '))
		destino = int(input('Digite o destino: '))

		if origem < 0 or origem > 10 or destino < 0 or destino > 10:
			print("O valor desejado está fora do esperado!!")	
			print('Digite um valor entre 0 e 10 \n')

		else:
			obj.busca(origem, destino)
			break


