# Lista: sempre a mesma ordem e é mutável

name_list = ["Ingrid","Livia",15]
name_list.append("Denis")
#print(name_list)


#Tupla é imúltavel, aloca uma pedaço da memória e a tupla não pode ser alterada

#Sets é uma conjunto de itens que não pode ser removido, apenas add. Não matém a ordem dos dados.

name_list_set = set(name_list)
name_list_set.remove(15)
print(name_list_set)
