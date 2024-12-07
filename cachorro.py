from animal import Animal
class Cachorro(Animal):
    def __init__(self, idade, nome, porte):
        super().__init__(idade, nome)
        self.__nome=nome
        self.__idade=idade
        self.__porte=porte
    
    def setPorte(self,porte):
        self.__porte=porte
    def getPorte(self):
        return self.__porte
    
    def mostrar(self):
        return f"Cachorro com idade: {self.getIdade()}, nome: {self.getNome()} e de porte de {self.getPorte()}cm foi criado."