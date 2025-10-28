class Pessoa: 
   def _init_(self, nome: str = "", idade: int = 0): 
         self.__nome: str = nome
         self.__idade: int = idade
    
    def get_nome(self) -> str: 
        return self.__nome 

    def get_idade(self) -> int: 
        return self.__idade 
   
    def _str_(self)-> str:
        return f"{self._nome}:{self._idade}"

class Moto: 
    def _init_(self):
        self.__power:int = 1
        self.__time:int = 0 
        self.__person: Cliente | None = None 

    def getPower(self)->int: 
        return self.__power

    def getTime (self)->int: 
        return self.__time 

    def getPerson(self)-> Cliente | None:
        return self.__person

    def inserir ( self,person:Cliente)->bool:
        if self.__person != None:
            print("fail: busy motorcycle")
            return false
        else:
            self.__person = person
            return True

    def remover (self, Cliente= None):
        if self.__person is None:
            print ("fail: empty motorcycle")
            return None
        aux: Cliente= self.__person  
        self.__person= None
        print(aux)

    def drive (self, time: int):
        if self.__time ==0:
            print("fail: buy time first")
            return
        if self.__person is None: 
            print("fail: empty motorcycle")
            return
        if self.__person.get_idade()>10:
            print("fail: too")
