# Sobrecarga de métodos al calcular el total de dinero (por semana y total)
from eafit.lenguajes.proyectofinal.herramientas.lists import SinglyLinkedList
import random


class Concurso:
    def __init__(self):
        self.concursantes = SinglyLinkedList()
        self.dineroTotalSemana = 0

    def generarConcurso(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

        for dia in dias:
            for _ in range(random.randint(1, 5)):
                self.concursantes.Insert(dia)

    def visualizarRegistroConcurso(self):
        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        for dia in dias:
            print("-" * 50)
            print(f'Registro del día: {dia}')
            print("-" * 50)
            self.concursantes.Show(self.concursantes.first, dia)
            self.calcularPremio(self.concursantes.first, 0, dia)
        self.calcularPremioSemana(self.concursantes.first)

    def calcularPremio(self, node, dinero, dia):
        if node is not None:
            if node.data.dia == dia:
                dinero += node.data.premio
            self.calcularPremio(node.next, dinero, dia)
        else:
            print(f'El dinero entregado en la emisión del día {dia} fue de: ${dinero} pesos')
            print("-"*50)

    def calcularPremioSemana(self, node):
        if node is not None:
            self.dineroTotalSemana += node.data.premio

        if node is None:
            print(f'El dinero entregado en las emisiones de la semana fue de: ${self.dineroTotalSemana} pesos')
        else:
            self.calcularPremioSemana(node.next)
