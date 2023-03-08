from tkinter import * #importar libreria tkinter
from tkinter import ttk

class entrada:
    def __init__(self, raiz):
        #init sirve como constructor de la clase(), self que hace referencia a los elementos de la misma clase.
        raiz.title("Inicio de Sesion")
        #la raiz es nuestra ventana base #self da a conocer los atributos.
        self.usuario = StringVar()
        self.contraseña = StringVar()
        
        mainFrame=ttk.Frame(raiz, padding="10 10 10 10") #Widgets transparentes #Instancia de raiz
        mainFrame.grid(column=0, row=0)
        
        
        usuarioEntry = ttk.Entry(mainFrame, width=25, textvariable=self.usuario)
        usuarioEntry.grid()
        usuarioEntry.grid(column=2,row=1)
        
        contraseñaEntry = ttk.Entry(mainFrame, width=25, textvariable=self.contraseña)
        contraseñaEntry.grid()
        contraseñaEntry.grid(column=2,row=3, pady=12)
        
        ttk.Label(mainFrame, text="Contraseña").grid(column=0, row=3) #sticky=(N,W,E,S)) #Objeto
##        ttk.Label(mainFrame, textvariable=self.usuario).grid(column=1, row=0)
        ttk.Label(mainFrame, text="Usuario").grid(column=0, row=1)
        
        
       
        ttk.Button(mainFrame, text="Ingresar", command=self.calcular).grid(column=2, row=10, sticky=(E))
        
    
        
        raiz.bind("<Return>", self.calcular)   #Buscar tablas de estandares de las letras.
        
        
        
    def calcular(self, *args): #Agregar en evento calcular el args arreglo de parametros
        print("Boton presionado: ")
        piesUsuario=self.pies.get() #Get Siempre devuelve una cadena
        print("Usuario ingresado: ", piesUsuario) 
            
if __name__=="__main__":
    print("Nada mas se mostrara si es el principal.")     
    print("Nada mas se mostrara esto si es el principal.")
    
 