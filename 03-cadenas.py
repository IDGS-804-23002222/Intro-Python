texto="Hola mundo :D"

# gato para comentarios de una linea
'''
para comentarios
de varias
lineas
'''
print(texto)
print(texto.lower)
print(texto.upper)
print(texto.title)
print(texto.find("al"))
print(texto.count("e"))
print(texto.replace("e","a"))

cadenaSeparada=texto.split(" ")
print(cadenaSeparada)