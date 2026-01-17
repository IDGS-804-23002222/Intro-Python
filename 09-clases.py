class OperasBas: #def nombre clase
    
    #DECLARACION DE PROPIEDADES
    num1=0
    num2=0
    res=0
    
    #declaracion de constructor this
    def __init__(self): # self es como el this en java, aunque sea un constructor vacío debe contener el self, si no marca error
        self.num1=0
        self.num2=0
        
    #declaracion de metodos de clase
    def suma(self, a):
        self.num1=a
        self.res=self.num1+self.num2
        print("La suma es: {}".format(self.res))
        
    def resta(self):
        self.res=self.num1-self.num2
        print("La resta es: {}".format(self.res))

#declaracion de main para declarar orden de las funciones al llamarlas
def main():
    obj=OperasBas()
    
    #si se le esta pasando un parámetro
    obj.suma(5)
    
    #si no se oasa parametro
    obj.resta()
    
if __name__=='__main__':
    main()
    