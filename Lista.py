amigos = ["Leo", "Cadu", "Gabriel", "Lucas", "Cauã", "Luiz"]
amigas = ["Julia", "Luana", "Julia", "Gabi", "Clara"]

#print(amigos[0]) #Printa a primeira opção da lista
#print(amigos[-1]) #Printa a última opção da lista
#print(amigas[0]) #Printa a primeira opção da lista
#print(amigas[-1]) #Printa a última opção da lista

print(amigos)
print(amigas)
amigos.extend(amigas) #Junta as duas listas
amigos.append("Lipe") #Adiciona no final da lista
amigos.insert(0, "João") #Adiciona na posição indicada da lista
amigos.remove("João") #Remove um item da lista
print(amigos)
amigos.pop() #Remove o último item da lista
print(amigos.index("Luiz")) #Diz a posição do item na lista, se não existir, diz que não existe
print(amigos.count("Julia")) #Conta a quantidade de vezes que o item aparece na lista
amigos.clear() #Limpa a lista por completo
print(amigos)