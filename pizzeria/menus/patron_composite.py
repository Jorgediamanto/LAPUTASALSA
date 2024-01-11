from abc import ABC, abstractmethod

# Clase Component
class MenuComponent(ABC):
    @abstractmethod
    def obtener_precio(self):
        pass

# Clase Leaf
class Elemento(MenuComponent):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_precio(self):
        return self.precio

# Clase Composite
class MenuComposite(MenuComponent):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self, elemento):
        self.elementos.remove(elemento)

    def obtener_precio(self):
        precio_total = sum(elemento.obtener_precio() for elemento in self.elementos)
        return precio_total

# Clase Composite Compuesto por dos menús simples
class MenuCompuesto(MenuComponent):
    def __init__(self, nombre, menu1, menu2):
        self.nombre = nombre
        self.menu1 = menu1
        self.menu2 = menu2

    def obtener_precio(self):
        precio_total = self.menu1.obtener_precio() + self.menu2.obtener_precio()
        return precio_total