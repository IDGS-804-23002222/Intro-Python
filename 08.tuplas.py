# tupla son inmutables se declara con ()

tupla=("uno", "dos","tres")
print(tupla)

tuplaVariosDatos=(12, True, 23.5, "El gato",12+4)
print(tuplaVariosDatos)

tuplasConTuplas=(1, 2, 3, 4(1, 2, 3))
print(tuplasConTuplas)

print(tuplaVariosDatos[3])
print(tuplaVariosDatos[-2])
print(tuplaVariosDatos[0:2])

#destructuracion de tupla
a,b,c=tupla
print(a,b,c)