from data_stark import lista_personajes
from funciones_stark_001 import *

while True:
    limpiar_pantalla()
    tp_02 = menu_tp_2()
    match tp_02:
            case "a":
                print("--- Nombres superheroes M ---")
                nombres_superheroes_masculinos()
            case "b":
                print("--- Nombres superheroes F ---")
                nombres_superheroes_femeninos()
            case "c":
                print(f"La altura del superheroe M más alto es de: {superheroe_alto_masculino()}")
            case "d":
                print(f"La altura del superheroe F más alta es de: {superheroe_alto_femenino()}")
            case "e":
                print(f"La altura del superheroe M más bajo es de: {superheroe_bajo_masculino()}")
            case "f":
                print(f"La altura del superheroe F más baja es de: {superheroe_bajo_femenino()}")
            case "g":
                print(f"El promedio de las alturas de genero M es de: {altura_promedio_masculino()}")
            case "h":
                print(f"El promedio de las alturas de genero F es de: {altura_promedio_femenino()}")
            case "i":
                nombres_indicadores_anteriores()   
            case "j":
                tipos_ojos()
            case "k":
                color_pelo()
            case "l":
                inteligencia() 
            case "m":
                lista_nombres_color_ojos()
            case "n":
                lista_nombres_color_pelo()
            case "o":
                lista_nombres_inteligencia()
            case _:
                print("Valor incorrecto")
    pausar()


print("fin del programa :)")


