""" 
Este módulo contiene 3 funciones de lógica para hacer
lo siguiente:

* Sumar 3 números
* Sumar n números
* Sumar 2 listas, elemento a elemento
"""
def sumar3Numeros(num1, num2, num3): #Entrada de la función
    resultado= num1+num2+num3
    return resultado #Salida de la función

def sumarNumeros(*numeros): #Se interpreta como lista
    resultadosuma= sum(numeros)    
    return resultadosuma

def sumarListas(lista1, lista2):
    listaResultado= []
    for i in range(0,len(lista1)):
        suma = lista1[i] + lista2[i]
        listaResultado.append(suma)
    return listaResultado