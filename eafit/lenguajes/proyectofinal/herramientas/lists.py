from eafit.lenguajes.proyectofinal.herramientas.node import Node


class SinglyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def empty(self):
        return self.first is None

    def Insert(self, dia):
        newNode = Node(dia)
        if self.empty():
            self.first = self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.size += 1

    def Show(self, node, dia):
        if node is not None and node.data.dia == dia:
            print(node)
            print("-"*50)

        if node is None:
            print("Fin de historial del dia ", dia)
        else:
            self.Show(node.next, dia)
