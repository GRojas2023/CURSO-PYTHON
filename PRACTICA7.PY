# 1) Diseña una función que tome como parámetro 2 números, y que devuelva una lista que contenga todos los números enteros entre estos 2 incluyendo ambos parámetros.


"""lista = []

def PRIMER_PUNTO(num1,num2):
    for i in range (num1,num2+1):
        lista.append(i)
    print(lista)

PRIMER_PUNTO(1,10)"""

#2) Escribir una función que tome como parámetro 2 números, y retorne una lista con todos los números pares entre estos, excluyendo a los parámetros.
"""
def par(num):
    if num % 2==0:
        return True
    return False

pares = []
def LOS_PARES( UNO,DOS ):
    for i in range(UNO, DOS):
        if par(i):
            pares.append(i)
    print(pares)

LOS_PARES(1,10)
"""
# 3) Escribir una función que tome 2 parámetros, el primero que reciba una cadena, y el segundo que reciba un carácter. La función tendrá que retornar la cantidad de veces que aparece ese carácter en esa cadena. 

"""def TRES(cadena,caracter):
    cantidad = 0
    for i in range(len(cadena)):
        if cadena[i] == caracter:
            cantidad+=1
    print (cantidad)

TRES("jajajajajjajjaja","j")"""

# 4) Elaborar una función que tome como parámetro 2 números, y retorne una lista con todos los números primos entre ese rango de números.

"""def Funcion_primos(INICIO , FIN):   
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

Funcion_primos(0 , 10)
"""
# 5) Elaborar una función que tome como parámetro una lista, y devuelva un bool que diga si en esa lista todos sus números son pares.

"""def pares_impares(*numeros):
    for i in numeros: # ciclo para recorrer la lista 
        if i % 2 != 0: #pregunta si un integrante es par o inpar y abajo estan los retornos
            return False
    return True

print(pares_impares(5, 6, 7, 8, 9, 10))
print(pares_impares())
print(pares_impares(5, 3))  
print(pares_impares(2, 4, 6, 8, 10, 12))"""

# 6) Elaborar una función que tome como parámetro una lista y devuelva un bool que diga si en esa lista todos sus números son primos.

"""
def este_es_primo(c):
    lista_auxiliar = [1]
    p = 1
    #creo una lista desde el uno al numero ungresado en la funcion
    while p < c:
        p +=1
        lista_auxiliar.append(p)
    
    # acumulo los resultados de las divisiones  
    resultados = []
    # divido al numero ingresado por la funcion desde el 1 hasta si mismo y los mando a la lista resultados 
    for i in lista_auxiliar:
        divisiones = c/i
        resultados.append(divisiones)
    #cuento cuantos enteros hay en lista resultados     
    cantidad_enteros = sum(float(elemento).is_integer() for elemento in resultados) # ACA CONTAMOS CUANTOS VECES OBTENEMOS UN NUMERO ENTERO CUANDO DIVIDIMOS
    # condicionamos para dar una respuesta verdadero o falso    
    if cantidad_enteros == 2:
        return True
    else:
        return False
    
def funcion6(*lista_de_numero):
    
    primos_verdadero = []
    for i in lista_de_numero:
        r = este_es_primo(i)
        if r == True:
            primos_verdadero.append(r)
    if len(primos_verdadero) == len(lista_de_numero):
        return True
    else:
        return False

    
print(funcion6(3,4,5,6,7,))
print(funcion6(3,3,3,3,3,3))
"""
