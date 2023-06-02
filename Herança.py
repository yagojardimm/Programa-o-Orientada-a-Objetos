#Ao usar a herança, é possível criar uma hierarquia de classes, onde as classes mais específicas (subclasses)]
#herdam características das classes mais gerais (superclasses), fornecendo uma estrutura organizada e modular para o código.
#A Herança tambem permite a organização lógica do programa


class Circulo(FormaGeometrica):
    PI = 3.14159  # Constante para o valor de PI

    def __init__(self, r):
        self.raio = r  # Atributo específico da classe Circulo para armazenar o raio

    def desenha(self):
        pass
        # Método que desenha o círculo.
        # A implementação real seria fornecida nas subclasses.

    def area(self):
        return Circulo.PI * (self.raio ** 2)
        # Método para calcular a área do círculo.
        # Utiliza a constante PI e o atributo raio para realizar o cálculo.
