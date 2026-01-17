#operacion de multiplicacion de a x b utilizando sumas 
# salida=3+3+3+3=12

a=3
b=4

resultado=0
contador=0
cadena=''

while contador<b:
    cadena=cadena+str(a)+'+'
    resultado=resultado+a
    contador=contador+1
print(cadena)
print("El resultado de la operación es: ", resultado)