class Roupa: 
        def __init__(self):
            self.__tamanho: str = ""

        def getTamanho(self):
            return self.__tamanho

        def setTamanho(self, numeracao):
            tamanhos_validos = ["P", "PP", "M", "G", "GG", "XG"]    
            if numeracao not in tamanhos_validos:
                print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
            else: 
                 self.__tamanho = numeracao
        
        def __str__(self):
            if self.__tamanho == "":
                return "size: ()"
            else:
                return f"size: ({self.__tamanho})"

def main():
             roupa = Roupa()
            
             while True: 
                line = input()    
                print("$" + line) 
                args = line.split(" ")

                if args[0] == "end":
                     break 
                if args[0] == "show":
                     print(roupa)
                if args[0] == "size":
                     numeracao = args[1]
                     roupa.setTamanho(numeracao)
main()                     
