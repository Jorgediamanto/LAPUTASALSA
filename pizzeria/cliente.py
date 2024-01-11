import pandas as pd
import numpy as np
import warnings
from pizzeria.menus.menu import Menu

# Clase Cliente
class Cliente():
    def __init__(self):
        # Inicializa las variables vacias que luego se llenaran
        self.usuario = ''
        self.contraseña = ''
        self.telefono = ''
        self.domicilio = ''
        self.pedidos = []
        # Lee el archivo CSV clientes.csv y lo guarda en una variable
        self.clientes_df = pd.read_csv('pizzeria/clientes.csv')

    # Funcion para iniciar sesion o crear un nuevo usuario
    def iniciar(self):
        # Bucle para iniciar sesion o crear un nuevo usuario
        while True:
            nuevo = input('¿Eres un cliente nuevo? (S/N): ')
            if nuevo.lower() == 's':
                # Si es un nuevo cliente, lo registra
                self.telefono = input('Teléfono: ')
                self.domicilio = input('Dirección: ')
                self.usuario = input('Usuario: ')
                self.contraseña = input('Contraseña: ')
                # Crea un DataFrame con los datos del nuevo cliente
                nuevo_cliente = pd.DataFrame({'Usuario': [self.usuario], 'Contraseña': [self.contraseña], 'Telefono': [self.telefono], 'Domicilio': [self.domicilio]})
                # Concatena el nuevo DataFrame con el DataFrame de clientes
                self.clientes_df = pd.concat([self.clientes_df, nuevo_cliente], ignore_index=True)
                # Guarda el DataFrame actualizado en el archivo CSV
                self.clientes_df.to_csv('pizzeria/clientes.csv', index=False)
                break
            elif nuevo.lower() == 'n':
                # Si no es un nuevo cliente, inicia sesion
                self.usuario = input('Usuario: ')
                self.contraseña = input('Contraseña: ')
                # Verifica si el usuario existe
                if self.usuario in self.clientes_df['Usuario'].values.tolist():
                    # Verifica si la contraseña coincide
                    index = self.clientes_df.index[self.clientes_df['Usuario'] == self.usuario].tolist()[0]
                    stored_password = self.clientes_df.at[index, 'Contraseña']
                    if self.contraseña == stored_password:
                        print('Inicio de sesión exitoso. ¡Bienvenido de nuevo!')
                        break
                    else:
                        print('La contraseña no coincide. Intenta de nuevo.')
                else:
                    print('El usuario no existe. Intenta de nuevo.')
            else:
                print('Opción no válida. Intenta de nuevo.')
    
    # Funcion que obtiene el numero de pedido de la pizza, menú simple o menú compuesto y lo guarda en el archivo CSV
    def pedido_pizzas(self, pedido, tipo):
        if tipo == 'Pizzas':
            n_pedido = pedido.numero_pedido() -1
        else:
            n_pedido = pedido.numero_pedido() -1
        n_pedido = str(n_pedido)
        user_index = self.clientes_df[self.clientes_df['Usuario'] == self.usuario].index[0]
        pedidos_anteriores = self.clientes_df.at[user_index, tipo]
        # Verifica si el cliente tiene pedidos anteriores
        if pd.notna(pedidos_anteriores):
            nuevos_pedidos = f"{pedidos_anteriores}/{n_pedido}"
        else:
            nuevos_pedidos = n_pedido

        # Suprime temporalmente las advertencias FutureWarning
        warnings.simplefilter(action='ignore', category=FutureWarning)
        # Actualiza la columna 'Pedidos' con los nuevos pedidos
        self.clientes_df.at[user_index, tipo] = nuevos_pedidos
        warnings.resetwarnings()

        # Guarda el DataFrame actualizado en el archivo CSV
        self.clientes_df.to_csv('pizzeria/clientes.csv', index=False)
    
    # Funcion que obtiene las pizzas anteriores del cliente y devuelve los ingredientes de estas
    def acceder_pizzas(self, pedido):
        # Obtiene los pedidos anteriores del cliente
        user_index = self.clientes_df[self.clientes_df['Usuario'] == self.usuario].index[0]
        pedidos_anteriores = self.clientes_df.at[user_index, 'Pizzas']
        # Verifica si el cliente tiene pedidos anteriores
        if pd.isna(pedidos_anteriores):
            numero_ped = 0
        else:
            # Verificar si hay solo un pedido
            if isinstance(pedidos_anteriores, (int, np.int64)):
                numero_ped = [pedidos_anteriores]
            else:
                # Si hay mas de un pedido, los separa
                numero_ped = str(pedidos_anteriores).split('/')
        # Llama a la funcion ingredientes_anteriores de la clase Pedido que le devuelve los ingredientes
        ingredientes = pedido.ingredientes_anteriores(numero_ped)
        return ingredientes
    
    # Funcion que obtiene los menus simples anteriores del cliente
    def acceder_menu_simple(self, menu):
        # Obtiene los pedidos anteriores del cliente
        user_index = self.clientes_df[self.clientes_df['Usuario'] == self.usuario].index[0]
        pedidos_anteriores = self.clientes_df.at[user_index, 'Menus Simples']
        # Verifica si el cliente tiene pedidos anteriores
        if pd.isna(pedidos_anteriores):
            numero_ped = 0
        else:
            # Verificar si hay solo un pedido
            if isinstance(pedidos_anteriores, (int, np.int64)):
                numero_ped = [pedidos_anteriores]
            else:
                # Si hay mas de un pedido, los separa
                numero_ped = str(pedidos_anteriores).split('/')
        # Llama a la funcion elementos que le devuelve los elementos del menu
        lista_menus = menu.obtener_elementos_simples(numero_ped)
        return lista_menus
    
    # Funcion que obtiene los menus compuestos anteriores del cliente
    def acceder_menu_compuesto(self, menu):
        # Obtiene los pedidos anteriores del cliente
        user_index = self.clientes_df[self.clientes_df['Usuario'] == self.usuario].index[0]
        pedidos_anteriores = self.clientes_df.at[user_index, 'Menus Compuestos']
        # Verifica si el cliente tiene pedidos anteriores
        if pd.isna(pedidos_anteriores):
            numero_ped = 0
        else:
            # Verificar si hay solo un pedido
            if isinstance(pedidos_anteriores, (int, np.int64)):
                numero_ped = [pedidos_anteriores]
            else:
                # Si hay mas de un pedido, los separa
                numero_ped = str(pedidos_anteriores).split('/')
        # Llama a la funcion elementos que le devuelve los elementos del menu
        lista_menus = menu.obtener_elementos_compuestos(numero_ped)
        return lista_menus
