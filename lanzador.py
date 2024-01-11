from pizzeria.lanzador_pizzeria import main_pizzeria
from samur.lanzador_samur import main_samur

def main():
    print("¿Qué ejercicio quieres ejecutar?")
    print("1. Pizzeria")
    print("2. Samur")
    while True:
        opcion = input("Opción: ")
        if opcion == "1":
            main_pizzeria()
            break
        elif opcion == "2":
            main_samur()
            break
        else:
            print("Opción no válida.")