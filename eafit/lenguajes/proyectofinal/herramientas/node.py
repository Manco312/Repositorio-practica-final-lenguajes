import random
from eafit.lenguajes.proyectofinal.herramientas.dato import Dato


class Node:
    def __init__(self, dia, next = None):

        nombres = ["Santiago", "Juan", "Juan José", "Diego", "David", "Luciana", "Kenia", "Nicolás", "Edison", "Andrés", "Marta"]
        apellidos = ["Manco", "Gómez", "Cruz", "Hoyos", "Valencia", "Vélez", "Álvarez", "Rico", "Montesino", "Maya", "Martínez", "Díaz", "Flores"]

        self.data = Dato(f'{random.choice(nombres)} {random.choice(apellidos)} {random.choice(apellidos)}', random.randint(1000000000, 1999999999), dia)  # Dato asignado al nodo
        self.next = next

    def __str__(self):
        return str(self.data)
