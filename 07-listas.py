#lista con secuencia de elementos se crea con []
lista1=["Dario", 33, 9.5, True, "German", 20.8]

print(lista1)
print(lista1[:])
print(lista1[2])
print(lista1[0:3])
print(lista1[3:])

lista1.append("Vargas")
print(lista1)

lista1.insert(2, "Nadia")
print(lista1)

lista1.extend(["uno",1.1,False])
print(lista1)