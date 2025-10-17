class Carta:
    def __init__(self, valor, palo, nombre):
        self.nombre = nombre
        self.valor = valor
        self.palo = palo
    def __str__(self):
        return f"{self.nombre} de {self.palo}"