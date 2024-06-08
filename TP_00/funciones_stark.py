from data_stark import *
from os import system

def mapear_campo(lista:list, campo)->list:
    """Mapea un campo de una lista origen y me devuelve su contenido en una nueva lista.

    Args:
        lista (list): Una lista origen
        campo (_type_): Campo de la lista de origen

    Returns:
        list: Una nueva lista con los datos del campo elegido
    """
    nueva_lista = []
    for dato in lista:
        nueva_lista.append(dato[campo])
    return nueva_lista


alturas = mapear_campo(lista_personajes, "altura")
pesos = mapear_campo(lista_personajes, "peso")

def mapear_dos_items(lista:list, item_1, item_2)->list:
    """Mapea dos campos de una lista y me devuelve su contenido en una nueva lista.

    Args:
        lista (list): Lista origen
        item_1 (_type_): Primer campo
        item_2 (_type_): Segundo campo

    Returns:
        list: Retorna la lista nueva con los datos de los campos seleccionados.
    """
    nueva_lista = []
    for el in lista:
        nueva_lista.append((el[item_1], el[item_2]))#solamente para ser leido y no ser modificado, me conviene usar una tupla
    return nueva_lista

def calcular_mayor(lista:list)->int:
    """Calcula el numero mayor de la lista
    Args:
        lista (list): lista para buscar el mayor

    Returns:
        int: retorna el mayor elemento de la lista
    """
    flag_mayor = True
    for el in lista:
        flotante = float(el)
        if flag_mayor == True or flotante > mayor:
            mayor = flotante
            flag_mayor = False
    return mayor

def calcular_menor(lista:list)->float:
    """Calcula el numero menor de la lista
    Args:
        lista (list): lista para buscar el menor

    Returns:
        int: retorna el menor elemento de la lista
    """
    flag_menor = True
    for el in lista:
        flotante = float(el)
        if flag_menor == True or flotante < menor:
            menor = flotante
            flag_menor = False
    return menor

def totalizar_lista(lista:list)->float:
    """Suma todos los elementos de la lista
    Args:
        lista (list): La lista a sumar

    Returns:
        int: Retorna el resultado de sumar todos los elementos de la lista
    """
    sumatoria = 0
    for el in lista:
        float_el = float(el)
        sumatoria += float_el
    return sumatoria

def calcular_promedio_lista(lista:list)->float:
    """Calcula el promedio de los elementos de una lista.

    Args:
        lista (list): Lista a promediar sus valores

    Raises:
        ValueError: Si la cantidad de elementos de la lista es 0

    Returns:
        float: El promedio de la lista
    """
    cant = len(lista)
    if cant == 0:
        raise ValueError("No esta definido el promedio de una lista vacia")
    return totalizar_lista(lista) / cant

def imprimir_nombres_superheroes():
    """Muestra los nombres de los superheroes por consola
    """
    mostrar_nombres = mapear_campo(lista_personajes, "nombre")
    for nombre in mostrar_nombres:
        print(f"nombres superheroes: {nombre}")

def imprimir_nombres_alturas():
    """Imprime los nombres y las alturas de los superheroes por consola
    """
    nombre_altura_superheroe = mapear_dos_items(lista_personajes, "nombre", "altura")
    for cada_elm in nombre_altura_superheroe:
        print(f"Nombre: {cada_elm[0]}")
        print(f"Altura: {cada_elm[1]}")
        print()

def altura_maxima(lista_alturas:list)->float:
    """Devuelve la altura maxima de una lista (En este caso pensado para la lista de alturas)

    Args:
        lista_alturas (_type_): lista a calcular el maximo

    Returns:
        _type_: la altura maxima
    """
    return calcular_mayor(lista_alturas)


def altura_minima(lista_alturas:list)->float:
    """Devuelve la altura minima de una lista (En este caso pensado para la lista de alturas)

    Args:
        lista_alturas (_type_): lista a calcular el minimo

    Returns:
        _type_: la altura minima
    """
    return calcular_menor(lista_alturas)

def promedio_alturas(lista_alturas:list)->float:
    """Calcula el promedio de las alturas de los superheroes y lo imprime por consola

    Args:
        lista_alturas: La lista de alturas de los superheroes
    """
    promedio_alturas = calcular_promedio_lista(lista_alturas)
    print(f"El promedio de todas las alturas es: {promedio_alturas}")

#G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
def nombre_mayor_altura(lista:list)->str:
    """Retorna el nombre del superheroe con mayor altura

    Args:
        lista: lista de personajes

    Returns:
        El nombre del superheroe
    """
    nombre_mayor = None
    for personaje in lista:
        if float(personaje["altura"]) == altura_maxima(alturas):
            nombre_mayor = personaje["nombre"]
    return f"El nombre del personaje con mayor altura es: {nombre_mayor}"

def nombre_menor_altura(lista:list)->str:
    """Retorna el nombre del superheroe con menor altura

    Args:
        lista: lista de personajes

    Returns:
        El nombre del superheroe
    """
    nombre_menor = None
    for personaje in lista:
        if float(personaje["altura"]) == altura_minima(alturas):
            nombre_menor = personaje["nombre"]
    return f"El nombre del personaje con menor altura es: {nombre_menor}"

def mas_pesado(lista_pesos:list)->str:
    """Calcula el peso del superheroe más pesado y lo retorna junto a su nombre

    Args:
        lista_pesos: lista de pesos de los superheroes

    Returns:
        El más pesado junto con su nombre
    """
    mayor_peso = calcular_mayor(lista_pesos)
    nombre_mayor_peso = None
    for personaje in lista_personajes:
        if float(personaje["peso"]) == mayor_peso:
            nombre_mayor_peso = personaje["nombre"]
    return print(f"El personaje con mayor peso es {nombre_mayor_peso} con {mayor_peso}kg")

def menos_pesado(lista_pesos:list)->str:
    """Calcula el peso del superheroe menos pesado y lo retorna junto a su nombre

    Args:
        lista_pesos: lista de pesos de los superheroes

    Returns:
        El menos pesado junto con su nombre
    """
    menor_peso = calcular_menor(lista_pesos)
    nombre_menor_peso = None
    for personaje in lista_personajes:
        if float(personaje["peso"]) == menor_peso:
            nombre_menor_peso = personaje["nombre"]
    return print(f"El personaje con menor peso es {nombre_menor_peso} con {menor_peso}kg")

def limpiar_pantalla():
    system("cls")

def pausar():
    system("pause")