class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number

    def isValid(self) -> bool:
        valid = "0123456789()."
        for _ in self.number:
            if _ not in valid:
                return False
        return True

    def Get_id(self):
        return self.id
    
    def Get_Number(self):
        return self.number
    
    def Set_id(self, id: str):
        self.id = id

    def Set_Number(self, number:str):
        self.number = number

    def __str__(self) -> str:
        return f"{self.id}:{self.number}"
    
class Contact:
    def __init__(self, name: str = ""):
        self.name = name
        self.favorited = False
        self.fone: list[Fone] = []


    def addFone(self, id: str, number: str):
        fone = Fone(id, number)
        if fone.isValid():
            self.fone.append(fone)
        else:
            print("fail: invalid number")

    def rmFone(self, index: int):
        if index <0 or index > len(self.fone):
            print("fail: index errado")
            return
        self.fone.pop(index)


    def offFavorite(self):
        self.favorited = not self.favorited


    def __str__(self):
        lista = ", ".join([str(x) for x in self.fone])
        if self.favorited:
            return f"@ {self.name} [{lista}]"
        else:
            return f"- {self.name} [{lista}]"








def main():
    contact = Contact()
    while True:
        line = input()
        print("$"+line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "init":
            name = args[1] if len(args) > 1 else ""
            contact = Contact(name)
        elif args[0] == "show":
            print(contact)
        elif args[0] == "add":
            id = args[1]
            number = args[2]
            contact.addFone(id,number)
        elif args[0] == "rm":
            index = int(args[1])
            contact.rmFone(index)
        elif args[0] == "tfav":
            contact.offFavorite()
        else:
            print("fail: comando invalido")

main()
