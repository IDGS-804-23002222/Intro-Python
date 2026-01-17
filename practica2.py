'''
crear un programa que permita realizar las operaciones basicas +,-,*,/
utilizando funciones para cada operacion y un menu principal para desplegar y elegir que operacion 
realizaremos
'''
def suma():
    num1=float(input("Ingresa el primer número: "))
    num2=float(input("Ingresa el segundo número: "))
    print("Resultado: ", num1 + num2)
    
def resta():
    num1=float(input("Ingresa el primer número: "))
    num2=float(input("Ingresa el segundo número: "))
    print("Resultado: ", num1 - num2)
    
def multiplicacion():
    num1=float(input("Ingresa el primer número: "))
    num2=float(input("Ingresa el segundo número: "))
    print("Resultado: ", num1 * num2)
    
def division():
    num1=float(input("Ingresa el primer número: "))
    num2=float(input("Ingresa el segundo número: "))
    if num2!=0:
        print("Resultado: ", num1/num2)
    else:
        print("Error: no se puede dividir entre cero")
        
def main():
    print('Selecciona una opcion para hacer la operacion')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicacion')
    print('4. Division')
    
    op=int(input("Opción: "))
    
    if op==1:
        suma()
    elif op==2:
        resta()
    elif op==3:
        multiplicacion()
    elif op==4:
        division()
    else:
        print("Opción no válida, selecciona una opción válida")

if __name__ == "__main__":
    main()