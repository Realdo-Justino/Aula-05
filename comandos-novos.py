#Como fazer um arrray
minhalista=["Realdo","Eduardo","Vitor",10]

print(minhalista)

#Acesso por posição
print(minhalista[1])

#Acesso indexado por posição
print(minhalista[-1])

#Intervalo dentro da array
print(minhalista[1:3])

#Intervalo dentro da array sem o primeiro item
print(minhalista[:3])

#Intervalo dentro da array sem o ultimo item
print(minhalista[1:])


#Intervalo dentro da array com numeros negativos
print(minhalista[1:-1])

#Alterando o valor
minhalista[3]="Novo"
print(minhalista)

#Trabalhando com o "for" em array
for i in minhalista:
    print(i)

#Trabalhando com o "for" em array usando intervalo
for i in minhalista[1:3]:
    print(i)

#Procurando
nome=(input("Procure um nome: "))
if nome in minhalista:
    print("nome encontrado")
else:
    print("Nome não encontrado")

#Contar itens
print(len(minhalista))

#Adiciona item ao array
minhalista.append("Henrique")
print(minhalista)

#Adiciona item na posição escolhida
minhalista.insert(2, "Sei la")
print(minhalista)

#Remover item específico
minhalista.remove("Realdo")
print(minhalista)

#Remove o índice especificado
minhalista.pop(4)
print(minhalista)

#Se usar o pop sem passar o parâmetro, vai remover o último da lixta
minhalista.pop()
print(minhalista)

#Deleta item na posição específica
del minhaLista[1]
print(minhaLista)

#deleta a lista toda
#del minhaLista

#Limpa a lista mas não deleta ela.
minhalista.clear()
print(minhalista)

#Inserindo valores novamente
minhalista.insert(0, "what")
minhalista.insert(1, "hey")
print(minhalista)

#Copia dados de uma lista para outra lista
minhasegundalista = minhalista.copy()
print(minhasegundalista)

#Copia dados de uma lista para outra lista
minhaterceiralista = list(minhasegundalista)
print(minhaterceiralista)

#Adicionando novos valores nas listas a seguir: 
minhasegundalista.append("eae")
minhaterceiralista.insert(0, "hey")
print(minhasegundalista)
print(minhaterceiralista)

#função count serve para contar a quantidade de vezes que o item se repete na lista
print(minhaterceiralista.count("what"))

#Juntando listas
minhaquartalista = minhasegundalista + minhaterceiralista
print(minhaquartaLista)

#Encontrando a posição de um item na lista
print(minhaquartaLista.index("hey"))