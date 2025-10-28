class Pessoa:
    def __init__(self, nome:str , dinheiro:int=0):
        self.__nome:str = nome
        self.__dinheiro:int = dinheiro

    def get_nome(self)->str:
        return self.__nome

    def get_dinheiro(self)->int:
        return self.__dinheiro

    def pagar (self, valor:int)->bool:
        if self.__dinheiro >=valor:
            self.__dinheiro -=valor
            return True
        else:
            return False
    def recebe_dinheiro(self, valor:int):
        self.__dinheiro +=valor

    def __str__ (self)->str:
        return f"{self.__nome}:{self.__dinheiro}"

class MotoUb:
    def __init__(self, passageiro:Pessoa | None , motorista:Pessoa | None , custo:int=0):
        self.__passageiro:Pessoa |None = None 
        self.__motorista:Pessoa |None = None 
        self.__custo:int = 0

    def get_passageiro(self)->Pessoa|None:
        return self.__passageiro

    def get_motorista(self)->Pessoa|None:
        return self.__motorista

    def get_custo(self)->int:
        return self.__custo

    def __str__(self) -> str:
        return f"Cost: {self.__custo}, Driver: {"None" if self.__motorista is None else self.__motorista}, Passenger: {"None" if self.__passageiro is None else self.__passageiro}"

    def set_Driver (self, pessoa:Pessoa)->bool:
        if self.__motorista is None:
            self.__motorista = pessoa
            return True
        else:
            return False
    
    def set_Pass(self, pessoa :Pessoa)->bool:
        if self.__motorista is None:
            return False
        if self.__passageiro is None:
            self.__passageiro = pessoa
            self.__custo=0
            return True
        else:
            return False

    def drive (self, km:int)->bool:
        if self.__motorista != None and self.__passageiro != None:
            self.__custo +=km
            return True
        else:
            return False
    
    def leavePass(self)->bool:
        if self.__passageiro is None:
            return False
        
        aux= self.__passageiro.get_dinheiro()

        if aux >=self.__custo:
           self.__passageiro.pagar(self.__custo)
           self.__motorista.recebe_dinheiro(self.__custo)
           print (f"{self.__passageiro} left")
        else:
            self.__passageiro.pagar(aux)
            self.__motorista.recebe_dinheiro(self.__custo)
            print ("fail: Passenger does not have enough money")
            print (f"{self.__passageiro} left")

        self.__custo=0
        self.__passageiro = None
        return True

def main():
    motoub=MotoUb(None,None)
    while True:
        line : str = input()
        print ("$" + line)
        args:list[str]=line.split(" ")
        if args[0] == "end":
            break
        if args [0] == "show":
            print(motoub)
        elif args [0]== "setDriver":
            nome =str (args[1])
            dinheiro=int (args[2])
            motorista=Pessoa(nome,dinheiro)
            motoub.set_Driver(motorista)
        elif args [0]=="setPass":
            nome = str (args[1])
            dinheiro = int (args[2])
            passageiro=Pessoa(nome,dinheiro)
            motoub.set_Pass(passageiro)
        elif args [0] == "drive":
            km=int(args[1])
            motoub.drive(km)
        elif args [0] == "leavePass":
            motoub.leavePass()

main()