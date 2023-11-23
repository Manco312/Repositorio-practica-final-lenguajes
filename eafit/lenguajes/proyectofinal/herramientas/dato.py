import random


class Dato:

    def __init__(self, nom, id, dia):
        self.nom = nom
        self.id = id
        self.tiempo = random.randint(10, 120)
        self.dia = dia
        self.ultimaPreg = random.randint(0, 15)
        self.plantado = random.choice(["Sí", "No"])
        self.premio = self.calcularPremio()
        self.comodin = random.choice(["Ninguno", "50/50", "Llamada a un amigo", "Ayuda del público", "50/50 y Llamada a un amigo", "50/50 y Ayuda del público", "Llamada a un amigo y ayuda del público", "50/50, llamada a un amigo y ayuda del público"])

    def calcularPremio(self):
        premios = [0, 100000, 200000, 300000, 500000, 1000000, 2000000, 3000000, 5000000, 7000000, 10000000, 12000000, 20000000, 50000000, 100000000, 300000000]

        if self.ultimaPreg == 15:
            return 300000000
        elif self.plantado == "Sí":
            return premios[self.ultimaPreg]
        elif self.ultimaPreg < 5:
            return 0
        elif 5 <= self.ultimaPreg < 10:
            return 1000000
        elif self.ultimaPreg >= 10:
            return 10000000

    def __str__(self):
        return (f'Nombre del concursante: {self.nom}\n'
                f'ID: {self.id}\n'
                f'Tiempo de respuesta en pregunta clasificatoria: {self.tiempo} segundos\n'
                f'Día de asistencia al concurso: {self.dia}\n'
                f'Ultima pregunta respondida correctamente: {self.ultimaPreg}\n'
                f'¿Se plantó?: {self.plantado}\n'
                f'Premio: ${self.premio} pesos\n'
                f'Comodine(s) usado(s): {self.comodin}')
