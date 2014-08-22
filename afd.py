# -*- coding: UTF-8 -*-

done = 's'
newMachine = 's'

while done.lower() == 's':
####################Efetua a leitura de uma nova maquina####################.
	if newMachine.lower() == 's':
		valid = False
		#Repete a leitura enquanto a maquina nao for valida.
		while not valid:
			machineName = str(raw_input("Informe o nome da maquina: "))
			try:
				machineFile = open(machineName)
			except:
				print "Arquivo não encontrado."
			else:
				states = machineFile.readline().replace('\n', '').replace(' ', '')#Le os estados do arquivo e retira os espaços e a quebra de linha.
				states = states.split(",")#Separa os estados em uma lista.

				alphabet = machineFile.readline().replace('\n', '').replace(' ', '')#Le o alfabeto do arquivo e retira os espaços e a quebra de linha.
				alphabet = alphabet.split(",")#Separa o alfabeto em uma lista.

				matrixSize = len(states) * len(alphabet)#Calcula o tamanho da matriz de transição.

				matrixLinear = machineFile.readline().replace('\n', '').replace(' ', '')#Le a matriz e retira os espaços e a quebra de linha.
				#Verifica se a matriz contem a quantidade de elementos estimados. Ela deve conter states X alphabet elementos mais os separadores.
				if len(matrixLinear) != matrixSize * 2 - 1:
					print "Matriz esta incorreta."
					continue
				matrixLinear = matrixLinear.split(";")#Separa aslinhasda matriz.

				#Separa os elementos das linhas em uma lista.
				i = 0
				while i < len(matrixLinear):
					matrixLinear[i] = matrixLinear[i].split(",")
					i += 1

				#Monta uma matriz de dicionario com as transições.
				matrix = {}
				i = 0
				j = 0
				for state in states:
					matrix[state] = {}
					for letter in alphabet:
						matrix[state][letter] = matrixLinear[i][j]
						j += 1
					i += 1
					j = 0

				#Le o estado inicial e verifica se o mesmo é valido.
				initial = machineFile.readline().replace('\n', '').replace(' ', '')
				if initial == '' or initial not in states:
					print "Estado inicial invalido ou nao informado(", initial, ")."
					validinue

				#Le o(s) estado(s) de aceitação e verifica se foi .
				final = machineFile.readline().replace('\n', '').replace(' ', '')
				if final == '':
					print "Estado final nao informado.(", final,")."
					continue
				valid = True
		print "Maquina carregada com sucesso."

####################Le a palavra.####################
	entry = str(raw_input("Informe palavra: "))

####################Inicia o estado da maquina.####################
	end = initial

####################Executa a maquina.####################
	print '\n'
	valid = True
	for i in entry:
		if i in alphabet:
			print end, '->',
			end = matrix[end][i]
		else:
			print "\nA palavra contem letras invalidas."
			valid = False
			break

####################Verifica se a palavra foi aceita.####################
	if valid:
		print end
		if end in final:
			print "A entrada foi aceita."
		else:
			print "A entrada nao foi aceita."

####################Le as opções do usuario.####################
	done = str(raw_input("\n\nDeseja continuar(S/n): "))
	if done == '':
		done = 's'

	if done.lower() == 's':
		newMachine = str(raw_input("Deseja carregar uma nova maquina(s/N): "))
		if newMachine == '':
			newMachine = 'n'