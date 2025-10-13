class Watch:
    def __init__(self, hora: int = 0, minuto: int = 0, segundo: int = 0):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0
        self.set_hora(hora)
        self.set_minuto(minuto)
        self.set_segundo(segundo)

    def __str__(self):
        return f"{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}"
    
    def get_hora(self) -> int:
        return self.__hora
    
    def get_minuto(self) -> int:
        return self.__minuto
    
    def get_segundo(self) -> int:
        return self.__segundo

    def set_hora(self, hora: int) -> None:
        if not (0 <= hora <= 23):
            print("fail: hora invalida")
            return False
        self.__hora = hora
        return True

    def set_minuto(self, minuto: int) -> None:
        if not (0 <= minuto <= 60):
            print("fail: minuto invalido")
            return False
        self.__minuto = minuto
        return True

    def set_segundo(self, segundo: int) -> None:
        if not (0 <= segundo <= 60):
            print("fail: segundo invalido")
            return False
        self.__segundo = segundo
        return True

    def nextSecond(self):
        self.__segundo += 1
        if self.__segundo > 59:
            self.__segundo = 0
            self.__minuto += 1
        if self.__minuto > 59:
            self.__minuto = 0
            self.__hora += 1
        if self.__hora > 23:
            self.__hora = 0

def main():
    relogio = Watch()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")
        if args[0] == "end":
            break
        elif args[0] in ["init", "set"]:
            hora = int(args[1])
            minuto = int(args[2])
            segundo = int(args[3])
            relogio.set_hora(hora)
            relogio.set_minuto(minuto)
            relogio.set_segundo(segundo)
        elif args[0] == "next":
            relogio.nextSecond()
        elif args[0] == "show":
            print(relogio)
    
main()

