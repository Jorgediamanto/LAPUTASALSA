import pizzeria.personalizadas.patron_builder as patron_builder
import pizzeria.personalizadas.pedido_pizzas as guardar_pedido
import pizzeria.cliente as cliente
from pizzeria.menus.menu import Menu
import pandas as pd

def main_pizzeria():
    print('Bienvenido a la Pizzeria Delizioso')
    precio_pizza = 0
    precio_menu = 0

    # Crea un cliente
    mi_cliente = cliente.Cliente()
    # Llama a la funcion iniciar e inicia sesion
    mi_cliente.iniciar()

    # Pregunta si desea crear una pizza personalizada
    while True:
        pedir_pizza = input("Desea crear una pizza (S/N): ")
        if pedir_pizza.lower() == "s":
            print("Precio estandar pizza personalizada 15€")
            
            # Crea el director y el builder
            director = patron_builder.Director()
            builder = patron_builder.ConcreteBuilder()
            director.builder = builder
            
            # Construye una pizza con todos los atributos
            director.build_full_featured_product(mi_cliente, guardar_pedido.Pedido(builder))

            # Guarda el pedido y lo muestra
            pedido = guardar_pedido.Pedido(builder)
            pedido.guardar()
            pedido.mostrar()
            # Guarda el numero de pedido en el archivo CSV clientes.csv
            mi_cliente.pedido_pizzas(pedido, 'Pizzas')

            # Lee el archivo CSV pedidos.csv y lo guarda en una variable
            pedidos_df = pd.read_csv('pizzeria/personalizadas/pizzas.csv')
            # Obtiene el ultimo pedido
            ultimo_pedido = pedidos_df.iloc[-1]
            # Obtiene la parte de extras del pedido
            extras = ultimo_pedido['Extras Gourmet']
            # Cuenta el numero de extras
            n_extras = len(extras.split("/"))
            
            # Calcula el precio total del pedido
            precio_pizza = 15 + n_extras * 2
            break

        elif pedir_pizza.lower() == "n":
            break

        else:
            print("Opción no válida. Intenta de nuevo.")
    
    # Pregunta si quiere pedir un menú
    while True:
        pedir_menu = input("\nDesea pedir un menú (S/N): ")
        if pedir_menu.lower() == "s":
            menus = Menu()
            menu = menus.pedir_menu()
            precio_menu = menu.obtener_precio()
            menus.guardar_menu(menu)
            # Guarda el numero de pedido en el archivo CSV clientes.csv
            individual = menus.simple
            if individual:
                mi_cliente.pedido_pizzas(menus, 'Menus Simples')
            else:
                mi_cliente.pedido_pizzas(menus, 'Menus Compuestos')
            print(f"El precio total de su pedido es de {precio_pizza + precio_menu} €")
            break
        elif pedir_menu.lower() == "n":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
    
    # ver si la variable menus existe
    try:
        menus
    except NameError:
        menus = Menu()
    # Pregunta si desea ver los elementos de los menus simples anteriores:
    elementos_simples = mi_cliente.acceder_menu_simple(menus)
    if elementos_simples != []:
        while True:
            ver_elementos = input("\nDesea ver sus menus simples anteriores (S/N): ")
            if ver_elementos.lower() == "s":
                for menu in elementos_simples:
                    for elemento in menu:
                        print(elemento)
                    print()
                break
            elif ver_elementos.lower() == "n":
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
    
    # Pregunta si desea ver los elementos de los menus compuestos anteriores:
    elementos_compuestos = mi_cliente.acceder_menu_compuesto(menus)
    if elementos_compuestos != []:
        while True:
            ver_elementos = input("\nDesea ver sus menus compuestos anteriores (S/N): ")
            if ver_elementos.lower() == "s":
                for menu in elementos_compuestos:
                    print(menu[0], ":")
                    for i in range(1, len(menu), 2):
                        print(menu[i], "con", menu[i + 1])
                    print()
                break
            elif ver_elementos.lower() == "n":
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

    print("Gracias por su visita. Hasta pronto!")