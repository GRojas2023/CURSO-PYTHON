# 1)Escriba una función que muestre todos los números primos entre 1 y un número n que es ingresado por parámetro.

"""def Funcion_primos( FIN):   
    INICIO = 1
    PRIMOS = []
    lista1 =[]
    lista2 =[]
    x=0
    for i in range (1, FIN+1): #CREO UNA LISTA DEL 1 HASTA EL SEGUNDO NUMERO INGRESADO EN LA FUNCION 
        lista1.append(i)
    
    
    for i in range (INICIO, FIN+1): #CREO OTRA LISTA CON RANGO DE LOS NUMERO INGRESADO EN LA FUNCION
        lista2.append(i)
    

    while INICIO < FIN:
            primo = lista2[x] # CADA NUMERO DE LISTA 2 GUARDADO ES ESTA VARIABLE 
            resultado = [primo / elemento for elemento in lista1] #CADA NUMERO DE LISTA 2 ES DIVIDIDO POR TODOS LOS NUEROS DE LA LISTA 1
            cantidad_enteros = sum(float(elemento).is_integer() for elemento in resultado) # ACA CONTAMOS CUANTOS VECES OBTENEMOS UN NUMERO ENTERO CUANDO DIVIDIMOS
            
            if cantidad_enteros == 2:# SI CONTAMOS 2 ENTEROS EN LA DIVISION DE UN NUMERO CON TODOS LOS NUMEROS DE LA LISTA 1 ES PRIMO
                PRIMOS.append(primo) # SI ES PRIMO SE AGREGA A LA LISTA DE PRIMOS
            x+=1
            INICIO+=1
    print(PRIMOS)

Funcion_primos(40)"""

#2) Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del programa de acuerdo a estos criterios:
#• Use un test condicional en el ciclo while para detener la ejecución.
#• Use un test condicional dentro del ciclo para decidir si continuar la ejecución.

"""def sandwhich():
    sandwhich_completo = [] 
    while True:
        if len(sandwhich_completo) == 0:
            saludo = input("hola un gusto poder ayudarte a la preparacion de tu sandwich PRESIONA ENTER PARA CONTINUAR: ")
            ingrediente =  input("Por favor selecciona un ingrediente de tu preferencia: ").upper()
            sandwhich_completo.append(ingrediente)
        if len(sandwhich_completo) > 0 and ingrediente != "SALIR":
            ingrediente = input("Por favor selecciona otro ingrediente de tu preferencia para tu sandwich o, escribe SALIR si deseas terminar: ").upper()
            sandwhich_completo.append(ingrediente)
        else:
            sandwhich_completo.remove("SALIR")
            print(f"Tu sandwich tiene lo siguiente, {sandwhich_completo}")
            break

sandwhich()"""
"""
#3) A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez usando argumentos por posición. Llámela una segunda vez usando argumentos por clave.
def hacer_remera(tamaño, mensaje):
    print(f"Se ha creado una remera de tamaño {tamaño} con el mensaje: '{mensaje}'.")

hacer_remera("L", "Hola, mundo!") # Llamada usando argumentos por posición

hacer_remera(tamaño="M", mensaje="Python es lo mejor que hay!") # Llamada usando argumentos por clave

#3B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los valores por defecto, y la segunda con valores diferentes.

def hacer_remera(tamaño='L', mensaje='Me gusta Python'):
    print(f"Se ha creado una remera de tamaño {tamaño} con el mensaje: '{mensaje}'.")

hacer_remera() # Primera remera con valores por defecto

hacer_remera(tamaño='M', mensaje='Me gusta Python') # Segunda remera con valores diferentes
"""
# 4) Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …).
"""
def fibonacci(n):
    lista_fibo = [0,1]
    while True:
        nuevo = lista_fibo[-1] + lista_fibo[-2]
        if nuevo < n:
            lista_fibo.append(nuevo)
        else:
            print(lista_fibo)
            break

fibonacci(19)"""


# 5) (Opcional) Calculadora más inteligente: Modifique el ejercicio 9 del primer practico para que la calculadora sea capaz de devolver el resultado solamente de una operación especificada por el usuario. Por ejemplo, si el usuario ingresa dos numeros x, y, y luego ingresa ‘1’, la calculadora devuelve la suma entre los numeros x,y; si ingresa ‘2’, devuelve la resta, etc.
"""
def operacion (x,y,a):
    operaciones = { 1: x+y , 2: x-y , 3 : x*y , 4: x/y}
    calculo = operaciones[a]
    print(calculo) 

operacion(2,3,4)
"""
#6) (Opcional) Conversión imperial: Desarrollar un programa en Python que pueda convertir gramos a libras, centímetros a pulgadas y kilómetros a millas. El programa debe permitir la conversión en ambos sentidos. 1.60934 Km = 1 milla 0.393701 pulgadas = 1 cm 0.00220462 libras = 1 gramo


def gramos_a_libras(x):
    gramos_o_libra = int(input("Si quieres convertir gramos a libra elige 1, o viceversa elige 2: "))
    if gramos_o_libra == 1:
        libra = (x / 453.592)
        print(f"Los {x} gramos, son {libra} libras")
    else:
        gramos = (x * 453.592)
        print(f"Los {x} libras, son {gramos} gramos")

def centímetros_a_pulgadas(x):
    centímetros_o_pulgadas = int(input("Si quieres convertir a pulgadas elige 1, o viceversa elige 2: "))
    if centímetros_o_pulgadas == 1:
        pulgada = (x / 2.54)
        print(f"Los {x} centimetros, son {pulgada} pulgadas")
    else:
        centimetros = (x * 2.54)
        print(f"Los {x} pulgadas, son {centimetros} centimetros")

def kilómetros_a_millas(x):
    kilómetros_o_millas = int(input("Si quieres convertir Kilometros a millas elige 1, o viceversa elige 2: "))
    if kilómetros_o_millas == 1:
        millas = (x * 0.621371)
        print(f"Los {x} kilometros, son {millas} millas")
    else:
        kilometro = (x * 1.60934)
        print(f"Los {x} millas, son {kilometro} kilometros")

def converciones():
    x = int(input("ingresa el monto a convertir: "))
    metodos = {1: gramos_a_libras, 2 : centímetros_a_pulgadas , 3 : kilómetros_a_millas}
    seleccion = int(input("""Por favor seleciona el numero de una opcion para convertir:
    1 De gramos a libras o viceversa,
    2 De centimetros a pulgadas o viceversa,
    3 De Kilometros a millas o viceversa o,
    4 para SALIR
    :"""))
    while True:
        if seleccion == 4:
            print("GRACIAS hasta la proxima")
            break
        else:
            if seleccion in metodos:
                metodos[seleccion](x)
                break

converciones()        






