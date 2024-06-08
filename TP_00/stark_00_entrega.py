from data_stark import lista_personajes
from funciones_stark import * 

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
    return input("Ingrese la opción: ")

while True:
    limpiar_pantalla()
    seleccion = menu_opciones()
    match seleccion:
        case "1":
            print(imprimir_nombres_superheroes())
        case "2": 
            imprimir_nombres_alturas()
        case "3":
            print(f"La altura maxima es {altura_maxima(alturas)}")
        case "4": 
            print(f"La altura minima es {altura_minima(alturas)}")
        case "5":
            promedio_alturas(alturas)
        case "6":
            print(nombre_mayor_altura(lista_personajes))
        case "7":
            print(nombre_menor_altura(lista_personajes))
        case "8":
            mas_pesado(pesos)
        case "9":
            menos_pesado(pesos)
        case "10":
            print("Saliendo...")
            break
        case _:
            print("Valor incorrecto")
    pausar()


print("fin del programa :)")


