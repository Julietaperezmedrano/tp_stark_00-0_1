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

def calcular_mayor(lista:list)->float:
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

def menu_opciones():
    print("----SUPERHEROES OPCIONES----")
    print("1. Mostrar nombres personajes")
    print("2. Mostrar nombres de personajes junto con su altura")
    print("3. Cual es el heroe más alto")
    print("4. Cual es el heroe más bajo")
    print("5. El promedio de todas las alturas")
    print("6. El nombre del heroe más alto")
    print("7. El nombre del superheroe más bajo")
    print("8. El heroe más pesado")
    print("9. El heroe menos pesado")
    print("10. salir")
    print("11. MENÚ TP ---> 2")
    return input("Ingrese la opción: ")


def filtrar_genero(lista:list, campo)->list:
    """Filtra genero según el campo que le indiquemos (F o M) y me devuelve una lista nueva con esos valores

    Args:
        lista (list): lista a filtrar
        campo (_type_): campo que queremos que nos retorne la nueva lista

    Returns:
        list: una lista nueva con los valores pedidos
    """
    lista_retorno = []
    for superheroe in lista:
        if superheroe["genero"] == campo:
            lista_retorno.append(superheroe)
    return lista_retorno


def filtrar_inteligencia(lista:list, campo)->list:
    """Filtra según el campo de inteligencia y me devuelve una lista nueva con esos valores

    Args:
        lista (list): lista a filtrar
        campo (_type_): campo que queremos que nos retorne la nueva lista

    Returns:
        list: una lista nueva con los valores pedidos
    """
    lista_retorno = []
    for superheroe in lista:
        if superheroe["inteligencia"] == campo:
            lista_retorno.append(superheroe)
    return lista_retorno

def filtrar_color_ojos(lista:list, campo)->list:
    """Filtra según el campo que le indiquemos y me devuelve una lista nueva con esos valores

    Args:
        lista (list): lista a filtrar
        campo (_type_): campo que queremos que nos retorne la nueva lista

    Returns:
        list: una lista nueva con los valores pedidos
    """
    lista_retorno = []
    for superheroe in lista:
        if superheroe["color_ojos"] == campo:
            lista_retorno.append(superheroe)
    return lista_retorno

def filtrar_color_pelo(lista:list, campo)->list:
    lista_retorno = []
    for superheroe in lista:
        if superheroe["color_pelo"] == campo:
            lista_retorno.append(superheroe)
    return lista_retorno

def nombres_superheroes_masculinos():
    masculinos = filtrar_genero(lista_personajes, "M")
    for masculino in masculinos:
        print(masculino["nombre"])

def nombres_superheroes_femeninos():
    femeninos = filtrar_genero(lista_personajes,"F")
    for femenino in femeninos:
        print(femenino["nombre"])

def superheroe_alto_masculino():
    masculinos = filtrar_genero(lista_personajes, "M")
    masculinos_altura = mapear_campo(masculinos, "altura")
    return altura_maxima(masculinos_altura)

def superheroe_alto_femenino():
    femeninos = filtrar_genero(lista_personajes, "F")
    femeninos_altura = mapear_campo(femeninos, "altura")
    return altura_maxima(femeninos_altura)

def superheroe_bajo_masculino():
    masculinos = filtrar_genero(lista_personajes, "M")
    masculinos_altura = mapear_campo(masculinos, "altura")
    return altura_minima(masculinos_altura)

def superheroe_bajo_femenino():
    femeninos = filtrar_genero(lista_personajes, "F")
    femeninos_altura = mapear_campo(femeninos, "altura")
    return altura_minima(femeninos_altura)

def altura_promedio_masculino():
    masculinos = filtrar_genero(lista_personajes, "M")
    masculinos_altura = mapear_campo(masculinos, "altura")
    return calcular_promedio_lista(masculinos_altura)

def altura_promedio_femenino():
    femeninos = filtrar_genero(lista_personajes, "F")
    femeninos_altura = mapear_campo(femeninos, "altura")
    return calcular_promedio_lista(femeninos_altura)

def nombre_alto_masculino():
    nombre_mayor = None
    masculinos = filtrar_genero(lista_personajes, "M")
    for masculino in masculinos:
        if float(masculino["altura"]) == superheroe_alto_masculino():
            nombre_mayor = masculino["nombre"]
    return nombre_mayor

def nombre_alto_femenino():
    nombre_mayor = None
    femeninos = filtrar_genero(lista_personajes, "F")
    for femenino in femeninos:
        if float(femenino["altura"]) == superheroe_alto_femenino():
            nombre_mayor = femenino["nombre"]
    return nombre_mayor

def nombre_bajo_masculino():
    nombre_menor = None
    masculinos = filtrar_genero(lista_personajes, "M")
    for masculino in masculinos:
        if float(masculino["altura"]) == superheroe_bajo_masculino():
            nombre_menor = masculino["nombre"]
    return nombre_menor

def nombre_bajo_femenino():
    nombre_baja = None
    femeninos = filtrar_genero(lista_personajes, "F")
    for femenino in femeninos:
        if float(femenino["altura"]) == superheroe_bajo_femenino():
            nombre_baja = femenino["nombre"]
    return nombre_baja  

def nombres_indicadores_anteriores():
    print(f"El masculino más alto es {nombre_alto_masculino()}")
    print(f"El femenino más alto es {nombre_alto_femenino()}")
    print(f"El masculino más bajo es {nombre_bajo_masculino()}")
    print(f"El femenino más bajo es {nombre_bajo_femenino()}")

def tipos_ojos():
    ojos = mapear_campo(lista_personajes, "color_ojos")
    contador_blue = 0
    contador_brown = 0
    contador_green = 0
    contador_red = 0
    contador_yellow = 0
    contador_silver = 0
    contador_hazel = 0
    for ojo in ojos:
        match ojo:
            case "Blue":
                contador_blue += 1
            case "Brown":
                contador_brown += 1
            case "Green":
                contador_green += 1
            case "Red":
                contador_red += 1
            case "Yellow":
                contador_yellow += 1
            case "Silver":
                contador_silver += 1
            case "Hazel":
                contador_hazel += 1
            case _:
                contador_yellow += 1
    print(f"La cantidad de heroes con ojos azules es: {contador_blue}")
    print(f"La cantidad de heroes con ojos marrones es: {contador_brown}")
    print(f"La cantidad de heroes con ojos verdes es: {contador_green}")
    print(f"La cantidad de heroes con ojos rojos es: {contador_red}")
    print(f"La cantidad de heroes con ojos amarillos es: {contador_yellow}")
    print(f"La cantidad de heroes con ojos plateados es: {contador_silver}")
    print(f"La cantidad de heroes con ojos hazel es: {contador_hazel}")


def color_pelo():
    pelos = mapear_campo(lista_personajes, "color_pelo")
    contador_brown = 0
    contador_yellow = 0
    contador_auburn = 0
    contador_blond = 0
    contador_white = 0
    contador_green = 0
    contador_red = 0
    contador_black = 0
    contador_dos_colores = 0
    no_tienen_pelo = 0
    for pelo in pelos:
        match pelo:
            case "Brown":
                contador_brown += 1
            case "Yellow":
                contador_yellow += 1
            case "Auburn":
                contador_auburn += 1
            case "Blond":
                contador_blond += 1
            case "White":
                contador_white += 1
            case "Green":
                contador_green += 1
            case "Red":
                contador_red += 1
            case "Black":
                contador_black += 1
            case "" | "No Hair":
                no_tienen_pelo += 1
            case _:
                contador_dos_colores += 1
    print(f"La cantidad de heroes con pelo marron es: {contador_brown}")
    print(f"La cantidad de heroes con pelo amarillo es: {contador_yellow}")
    print(f"La cantidad de heroes con pelo Auburn es: {contador_auburn}")
    print(f"La cantidad de heroes con pelo rubio es: {contador_blond}")
    print(f"La cantidad de heroes con pelo blanco es: {contador_white}")
    print(f"La cantidad de heroes con pelo verde es: {contador_green}")
    print(f"La cantidad de heroes con pelo rojo es: {contador_red}")
    print(f"La cantidad de heroes con pelo negro es: {contador_black}")
    print(f"La cantidad de heroes sin pelo es: {no_tienen_pelo}")
    print(f"La cantidad de heroes con pelo de dos colores es: {contador_dos_colores}")

def inteligencia():
    inteligencias = mapear_campo(lista_personajes, "inteligencia")
    contador_average = 0
    contador_good = 0
    contador_high = 0
    sin_int = 0
    for int in inteligencias:
        match int:
            case "average":
                contador_average += 1
            case "good":
                contador_good += 1
            case "high":
                contador_high += 1
            case _:
                sin_int += 1
    print(f"La cantidad de heroes con inteligencia average es: {contador_average}")
    print(f"La cantidad de heroes con inteligencia good es: {contador_good}")
    print(f"La cantidad de heroes con inteligencia high es: {contador_high}")
    print(f"La cantidad de heroes sin inteligencia es: {sin_int}")


def lista_nombres_color_ojos():
    brown = filtrar_color_ojos(lista_personajes, "Brown")
    print("*** Superheroes ojos marrones ***")
    for heroe in brown:
        print(heroe["nombre"])
    blue = filtrar_color_ojos(lista_personajes, "Blue")
    print("*** Superheroes ojos azules ***")
    for heroe in blue:
        print(heroe["nombre"])
    green = filtrar_color_ojos(lista_personajes, "Green")
    print("*** Superheroes ojos verdes ***")
    for heroe in green:
        print(heroe["nombre"])
    red = filtrar_color_ojos(lista_personajes, "Red")
    print("*** Superheroes ojos rojos ***")
    for heroe in red:
        print(heroe["nombre"])
    hazel = filtrar_color_ojos(lista_personajes, "Hazel")
    print("*** Superheroes ojos hazel ***")
    for heroe in hazel:
        print(heroe["nombre"])
    silver = filtrar_color_ojos(lista_personajes, "Silver")
    print("*** Superheroes ojos plateados ***")
    for heroe in silver:
        print(heroe["nombre"])
    yellow = filtrar_color_ojos(lista_personajes, "Yellow")
    print("*** Superheroes ojos amarillos ***")
    for heroe in yellow:
        print(heroe["nombre"])

def lista_nombres_color_pelo():
    pelo_yellow = filtrar_color_pelo(lista_personajes, "Yellow")
    print("*** Superheroes pelo amarillo ***")
    for heroe in pelo_yellow:
        print(heroe["nombre"])

    brown = filtrar_color_pelo(lista_personajes, "Brown")
    print("*** Superheroes pelo marron ***")
    for heroe in brown:
        print(heroe["nombre"])

    black = filtrar_color_pelo(lista_personajes, "Black")
    print("*** Superheroes pelo negro ***")
    for heroe in black:
        print(heroe["nombre"])

    auburn = filtrar_color_pelo(lista_personajes, "Auburn")
    print("*** Superheroes pelo auburn ***")
    for heroe in auburn:
        print(heroe["nombre"])

    red_orange = filtrar_color_pelo(lista_personajes, "Red / Orange")
    print("*** Superheroes pelo red orange ***")
    for heroe in red_orange:
        print(heroe["nombre"])

    white = filtrar_color_pelo(lista_personajes, "White")
    print("*** Superheroes pelo blanco ***")
    for heroe in white:
        print(heroe["nombre"])

    no_hair = filtrar_color_pelo(lista_personajes, "No Hair")
    print("*** Superheroes sin pelo ***")
    for heroe in no_hair:
        print(heroe["nombre"])

    no_hair_2 = filtrar_color_pelo(lista_personajes, "")
    print("*** Superheroes sin pelo ***")
    for heroe in no_hair_2:
        print(heroe["nombre"])

    blond = filtrar_color_pelo(lista_personajes, "Blond")
    print("*** Superheroes pelo rubio ***")
    for heroe in blond:
        print(heroe["nombre"])

    green = filtrar_color_pelo(lista_personajes, "Green")
    print("*** Superheroes pelo verde ***")
    for heroe in green:
        print(heroe["nombre"])

    red = filtrar_color_pelo(lista_personajes, "Red")
    print("*** Superheroes pelo rojo ***")
    for heroe in red:
        print(heroe["nombre"])


    brown_white = filtrar_color_pelo(lista_personajes, "Brown / White")
    print("*** Superheroes pelo marron / blanco ***")
    for heroe in brown_white:
        print(heroe["nombre"])

def lista_nombres_inteligencia():
    sin_int = filtrar_inteligencia(lista_personajes, "")
    print("*** Superheroes sin inteligencia ***")
    for heroe in sin_int:
        print(heroe["nombre"])
    print()

    average = filtrar_inteligencia(lista_personajes, "average")
    print("*** Superheroes inteligencia average ***")
    for heroe in average:
        print(heroe["nombre"])
    print()

    good = filtrar_inteligencia(lista_personajes, "good")
    print("*** Superheroes inteligencia good ***")
    for heroe in good:
        print(heroe["nombre"])
    print()

    high = filtrar_inteligencia(lista_personajes, "high")
    print("*** Superheroes inteligencia good ***")
    for heroe in high:
        print(heroe["nombre"])
    print()

def menu_tp_2():
    print("---OPCIONES TP 2---")
    print("A. Nombres de superheroes genero Masculino")
    print("B. Nombres de superheroes genero Femenino")
    print("C. Superheroe más alto género Masculino")
    print("D. Superheroe más alto género Femenino")
    print("E. Superheroe más bajo género Masculino")
    print("F. Superheroe más bajo género Femenino")
    print("G. Altura promedio de los superheroes genero Masculino")
    print("H. Altura promedio de los superheroes genero Femenino")
    print("I. Nombre de cada uno de los indicadores anteriores (DEL C AL F)")
    print("J. Cantidad de superheroes con cada tipo de color de ojos")
    print("K. Cantidad de superheroes con cada tipo de color de pelo")
    print("L. Cantidad de superheroes por cada tipo de inteligencia")
    print("M. Lista de superheroes agrupados por cada color de ojos")
    print("N. Lista de superheroes agrupados por cada color de pelo")
    print("O. Lista de superheroes agrupados por tipo de Inteligencia")
    print()
    return input("Ingrese una de las siguientes opciones: ")
