import pandas as pd
from pizzeria.menus.patron_composite import MenuComposite, MenuCompuesto, Elemento

class Menu:
    def __init__(self):
        self.simple = False

    # funcion para elegir bebida
    def elegir_bebida(self):
        print("\nBebidas disponibles:")
        print("1. Coca Cola")
        print("2. Zumo")
        print("3. Agua")
        while True:
            eleccion_bebida = input("Elige un número de bebida: ")
            if eleccion_bebida == "1":
                bebida = "Coca Cola"
                break
            elif eleccion_bebida == "2":
                bebida = "Zumo"
                break
            elif eleccion_bebida == "3":
                bebida = "Agua"
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        return bebida
        
    def pedir_menu(self):
        # Crear menús simples
        menu_bbq = MenuComposite("Menu Simple BBQ")
        menu_bbq.agregar(Elemento("Patatas", 5))
        menu_bbq.agregar(Elemento("Pizza Barbacoa", 12))
        menu_bbq.agregar(Elemento("Helado", 4))

        menu_basico = MenuComposite("Menu Simple Básico")
        menu_basico.agregar(Elemento("Croquetas", 5))
        menu_basico.agregar(Elemento("Pizza Margarita", 10))
        menu_basico.agregar(Elemento("Sorbete", 4))

        menu_queso = MenuComposite("Menu Simple Queso")
        menu_queso.agregar(Elemento("Ensalada", 3))
        menu_queso.agregar(Elemento("Pizza 4 Quesos", 12))
        menu_queso.agregar(Elemento("Tarta de Queso", 4))

        menu_carbonara = MenuComposite("Menu Simple Carbonara")
        menu_carbonara.agregar(Elemento("Alitas de Pollo", 5))
        menu_carbonara.agregar(Elemento("Pizza Carbonara", 13))
        menu_carbonara.agregar(Elemento("Tiramisú", 4))

        # Preguntar al usuario si desea un menú simple o uno compuesto
        while True:
            print("\nTipos de Menús Simples disponibles:")
            print(f"\nMenu Simple BBQ: {menu_bbq.obtener_precio() + 1} €")
            for elemento in menu_bbq.elementos:
                    print(f"- {elemento.nombre}")
            print(f"\nMenu Simple Básico: {menu_basico.obtener_precio() + 1} €")
            for elemento in menu_basico.elementos:
                print(f"- {elemento.nombre}")
            print(f"\nMenu Simple Queso: {menu_queso.obtener_precio() + 1} €")
            for elemento in menu_queso.elementos:
                print(f"- {elemento.nombre}")
            print(f"\nMenu Simple Carbonara: {menu_carbonara.obtener_precio() + 1} €")
            for elemento in menu_carbonara.elementos:
                print(f"- {elemento.nombre}")

            print("\nTipos de Menús Compuestos disponibles:")
            print(f"\nMenu Compuesto Carnívoro: {menu_bbq.obtener_precio() + menu_carbonara.obtener_precio() + 2} €")
            print("- Menu Simple BBQ + Menu Simple Carbonara")
            print(f"\nMenu Compuesto Vegetariano: {menu_basico.obtener_precio() + menu_queso.obtener_precio() + 2} €")
            print("- Menu Simple Básico + Menu Simple Queso")

            eleccion_tipo_menu = input("\n¿Deseas un menú simple (S) o uno compuesto (C)? ").upper()
            if eleccion_tipo_menu == "S":
                self.simple = True
                # Mostrar elementos de los menús. Al precio de cada menú se le suma 1 € por la bebida que se añadirá después
                print("\nMenús simples disponibles:")
                print("1. Menu Simple BBQ")
                print("2. Menu Simple Básico")
                print("3. Menu Simple Queso")
                print("4. Menu Simple Carbonara")

                # Pedir al usuario que elija un menú simple
                while True:
                    eleccion_menu = input("\nElige un número de menú: ")
                    if eleccion_menu == "1":
                        menu = menu_bbq
                        menu.agregar(Elemento(self.elegir_bebida(), 1))
                        break
                    elif eleccion_menu == "2":
                        menu = menu_basico
                        menu.agregar(Elemento(self.elegir_bebida(), 1))
                        break
                    elif eleccion_menu == "3":
                        menu = menu_queso
                        menu.agregar(Elemento(self.elegir_bebida(), 1))
                        break
                    elif eleccion_menu == "4":
                        menu = menu_carbonara
                        menu.agregar(Elemento(self.elegir_bebida(), 1))
                        break
                    else:
                        print("Opción no válida. Intenta de nuevo.")
                break
            elif eleccion_tipo_menu == "C":
                self.simple = False
                # Mostrar opciones de menús compuestos. Al precio de cada menú se le suma 2 € por las bebidas que se añadirán después
                print("\nMenús Compuestos disponibles:")
                print("1. Menu Compuesto Carnívoro")
                print("2. Menu Compuesto Vegetariano")
                
                # Pedir al usuario que elija un menú compuesto
                while True:
                    eleccion_menu_compuesto = input("\nElige una opción (1, 2): ")
                    if eleccion_menu_compuesto == "1":
                        menu_bbq.agregar(Elemento(self.elegir_bebida(), 1))
                        menu_carbonara.agregar(Elemento(self.elegir_bebida(), 1))
                        menu = MenuCompuesto("Menu Compuesto A", menu_bbq, menu_carbonara)
                        break
                    elif eleccion_menu_compuesto == "2":
                        menu_basico.agregar(Elemento(self.elegir_bebida(), 1))
                        menu_queso.agregar(Elemento(self.elegir_bebida(), 1))
                        menu = MenuCompuesto("Menu Compuesto B", menu_basico, menu_queso)
                        break
                    else:
                        print("Opción no válida. Intenta de nuevo.")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")
        return menu

    def numero_pedido(self):
        if self.simple:
            archivo = 'pizzeria/menus/menus_simples.csv'
        else:
            archivo = 'pizzeria/menus/menus_compuestos.csv'
        try:
            menu_df = pd.read_csv(archivo)
            if not menu_df.empty:
                ultimo_id = menu_df['Numero'].max()
                nuevo_id = ultimo_id + 1
            else:
                nuevo_id = 1
        except FileNotFoundError:
            nuevo_id = 1
        return nuevo_id

        
    def guardar_menu(self,menu):
        # obtener el numero de menu
        numero = self.numero_pedido()

        # guardar el menu en el archivo CSV
        if self.simple:
            try:
                menu_df = pd.read_csv('pizzeria/menus/menus_simples.csv')
            except FileNotFoundError:
                menu_df = pd.DataFrame(columns=['Menu', 'Entrante', 'Pizza', 'Postre', 'Bebida', 'Precio', 'Numero'])
            menu_df = pd.concat([menu_df, pd.DataFrame([{'Menu': menu.nombre, 'Entrante': menu.elementos[0].nombre, 'Pizza': menu.elementos[1].nombre, 'Postre': menu.elementos[2].nombre, 'Bebida': menu.elementos[3].nombre, 'Precio': menu.obtener_precio(), 'Numero': numero}])], ignore_index=True)
            menu_df.to_csv('pizzeria/menus/menus_simples.csv', index=False)
        else:
            try:
                menu_df = pd.read_csv('pizzeria/menus/menus_compuestos.csv')
            except FileNotFoundError:
                menu_df = pd.DataFrame(columns=['Menu', 'Menu 1', 'Bebida 1', 'Menu 2', 'Bebida 2', 'Precio', 'Numero'])
            menu_df = pd.concat([menu_df, pd.DataFrame([{'Menu': menu.nombre, 'Menu 1': menu.menu1.nombre, 'Bebida 1': menu.menu1.elementos[3].nombre, 'Menu 2': menu.menu2.nombre, 'Bebida 2': menu.menu2.elementos[3].nombre, 'Precio': menu.obtener_precio(), 'Numero': numero}])], ignore_index=True)
            menu_df.to_csv('pizzeria/menus/menus_compuestos.csv', index=False) 

    # Funcion que accede a unos menus simples dada una lista de id y devuelve una lista con los elementos
    def obtener_elementos_simples(self, lista_id):
        menu_df = pd.read_csv('pizzeria/menus/menus_simples.csv')
        if lista_id == 0:
            return []
        else:
            elementos = []
            i = 0
            for num in lista_id:
                elementos.append([])
                num =int(float(num))
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Menu'].iloc[0])
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Entrante'].iloc[0])
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Pizza'].iloc[0])
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Postre'].iloc[0])
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Bebida'].iloc[0])
                i += 1
            return elementos

    # Funcion que accede a unos menus compuestos dada una lista de id y devuelve una lista con los elementos
    def obtener_elementos_compuestos(self, lista_id):
        menu_df = pd.read_csv('pizzeria/menus/menus_compuestos.csv')
        if lista_id == 0:
            return []
        else:
            elementos = []
            i = 0
            for num in lista_id:
                elementos.append([])
                num =int(float(num))
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Menu'].iloc[0])
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Menu 1'].iloc[0])
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Bebida 1'].iloc[0])
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Menu 2'].iloc[0])
                elementos[i].append(menu_df[menu_df['Numero'] == num]['Bebida 2'].iloc[0])
                i += 1
            return elementos