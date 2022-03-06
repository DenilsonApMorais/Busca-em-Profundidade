from BuscaProfundidade import BuscaProf


if __name__ == '__main__':
    
	cond = 's'

	print("""As cidade disponíveis são:
	0: Montes Claros
	1: Diamantina
	2: Uberlândia
	3: Uberaba
	4: Governador Valadares
	5: Belo Horizonte
	6: Ipatinga
	7: Poços de Caldas
	8: São João Del Rey
	9: Juiz de Fora
	10: São Lourenço
	""")
 	

	while cond == 's':
		obj = BuscaProf()
		origem = int(input('Digite a origem: '))
		destino = int(input('Digite o destino: '))

		if origem < 0 or origem > 10 or destino < 0 or destino > 10 or destino == origem :
			print("O valor desejado está fora do esperado!!")	
			print('Digite um valor entre 0 e 10 \n')

		else:
			obj.busca(origem, destino)
			
			cond = input('\nDeseja continuar? (s/n): ')
			


