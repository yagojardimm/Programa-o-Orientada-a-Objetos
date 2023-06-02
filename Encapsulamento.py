# O encapsulamento permite esconder os detalhes internos de uma classe, proteger os dados e 
# fornecer uma interface controlada para interagir com os objetos. Isso promove a modularidade, 
# proteção de dados e facilita a manutenção e extensibilidade do código.

#O método __init__ é o construtor da classe. Ele recebe o número da conta e o saldo inicial
# como parâmetros e os atribui aos atributos privados __nome e idade.
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome  # Atributo privado
        self.idade = idade  # Atributo público

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome


# Criando uma instância da classe Pessoa
pessoa = Pessoa("João", 25)

# Acessando o atributo público "idade"
print(pessoa.idade)  # Saída: 25

# Tentando acessar o atributo privado "__nome" (gerará um erro)
print(pessoa.__nome)  # Gera um erro: AttributeError

# Acessando o atributo privado "__nome" através do método get_nome()
print(pessoa.get_nome())  # Saída: João

# Alterando o atributo privado "__nome" através do método set_nome()
pessoa.set_nome("Pedro")

# Acessando o atributo privado "__nome" após a alteração
print(pessoa.get_nome())  # Saída: Pedro

