from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, idade, nome):
        self.__nome=nome
        self.__idade=idade
        
    @abstractmethod
    def mostrar(self):
        pass
    def getNome(self):
        return self.__nome
    def getIdade(self):
        return self.__idade
    def setNome(self,nome):
        self.__nome=nome
    def setIdade(self,idade):
        self.__idade=idade