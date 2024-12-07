from animal import Animal
class Gato(Animal):
    def __init__(self, idade, nome, raca):
        super().__init__(idade, nome)
        self.__raca=raca
    def setRaca(self, raca):
        self.__raca=raca
    def getRaca(self):
        return self.__raca
    
    def mostrar(self):
        return (f"Gato de idade: {self.getIdade()}, nome: {self.getNome()} e da raca {self.getRaca()} foi criado.")