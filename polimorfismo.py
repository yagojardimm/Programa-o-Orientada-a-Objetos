# Através do polimorfismo é possível permitir que os  objetos das classes derivadas sejam tratado como objetos da classe base.


#polimorfismo

# Definição da classe abstrata Veiculo
class Veiculo:
    def __init__(self, marca: str):
        self.marca = marca

    def ligar(self) -> str:
        raise NotImplementedError("Método 'ligar' não implementado")

    def acelerar(self) -> str:
        raise NotImplementedError("Método 'acelerar' não implementado")

# Definição da classe Carro, que herda de Veiculo
class Carro(Veiculo):
    def ligar(self) -> str:
        return f"{self.marca}: ligando o motor do carro"

    def acelerar(self) -> str:
        return f"{self.marca}: acelerando o carro"

# Definição da classe Moto, que herda de Veiculo
class Moto(Veiculo):
    def ligar(self) -> str:
        return f"{self.marca}: ligando o motor da moto"

    def acelerar(self) -> str:
        return f"{self.marca}: acelerando a moto"

# Função para testar o polimorfismo com veículos
def teste_polimorfismo(veiculo: Veiculo) -> None:
    print(veiculo.ligar())
    print(veiculo.acelerar())

# Criando instâncias das classes
carro = Carro("Ford")  # Instância de Carro com a marca "Ford"
moto = Moto("Honda")  # Instância de Moto com a marca "Honda"

# Chamando a função teste_polimorfismo() com diferentes instâncias
teste_polimorfismo(carro)  # Chamando a função com um objeto Carro
teste_polimorfismo(moto)  # Chamando a função com um objeto Moto

