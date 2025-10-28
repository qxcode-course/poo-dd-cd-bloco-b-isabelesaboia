class Grafite:
    def __init__(self, tamanho:int, calibre:float, dureza:str):
        self.__tamanho:int=tamanho
        self.__calibre:float=calibre
        self.__dureza:str= dureza
    
    def get_tamanho(self)->int:
        return self.__tamanho

    def get_calibre(self)->float:
        return self.__calibre

    def get_dureza(self)->str:
        return self.__dureza

    def set_tamanho(self,tamanho:int):
        self.__tamanho=tamanho

    def consumo_folha(self)->int:
       consumo={"HB":1,"2B":2, "4B":4, "6B":6}[self.__dureza]
       self.__tamanho -=consumo
       return self.__tamanho

    def set_tamanho(self,tamanho:int)->int:
        self.__tamanho=tamanho

    def __str__(self)->str:
        return f"[{self.__calibre}:{self.__dureza}:{self.__tamanho}]"
    
class Lapiseira:
    def __init__(self, calibre:float):
        self.__ponta:Grafite | None = None
        self.__calibre:float = calibre

    def get_ponta(self)->Grafite:
        return self.__ponta
    
    def hasGrafite(self)->bool:
        if self.__ponta is None:
            return False
        if self.__ponta !=None:
            return True

    def inserir(self,grafite:Grafite)->bool:
        if self.__ponta != None:
            print ("fail: ja existe grafite")
            return False

        if grafite.get_calibre()!=self.__calibre:
            print("fail: calibre incompativel")
            return False

        self.__ponta = grafite
        return True

    def remove(self)->Grafite|None:
        aux=self.__ponta
        self.__ponta=None
        return aux

    def writePage(self):
        if self.__ponta is None:
            print("fail: nao existe grafite")
            return
        consumo={"HB":1, "2B":2, "4B":4,"6B":6}[self.__ponta.get_dureza()]

        if self.__ponta.get_tamanho()<=10:
            print("fail: tamanho insuficiente")
            return
        if self.__ponta.get_tamanho()-consumo<10:
           self.__ponta.set_tamanho(10)
           print("fail: folha incompleta")
           return
        self.__ponta.consumo_folha()

    def __str__(self)->str:
        if self.__ponta is None:
            ponta_print= "null"
        else:
            ponta_print=str(self.__ponta)
        return f"calibre: {self.__calibre}, grafite: {ponta_print}"

       

def main():
    lapiseira=Lapiseira("")
    while True:
        line:str=input()
        print ("$"+ line)
        args:list[str]=line.split(" ")
        if args[0] == "end":
            break
        elif args [0] == "show":
            print (lapiseira)
        elif args [0]== "init":
            calibre= float(args[1])
            lapiseira=Lapiseira(calibre)
        elif args [0]== "insert":
            calibre=float(args[1])
            dureza=str(args[2])
            tamanho=int(args[3])
            grafite=Grafite(tamanho,calibre,dureza)
            lapiseira.inserir(grafite)
        elif args [0]=="remove":
            lapiseira.remove()
        elif args [0]=="write":
            lapiseira.writePage()
        
main()
