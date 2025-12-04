class Fone: 
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number

    def __str__(self):
        return f"{self.__id}:{self.__number}"
    
    def isValid(self):
        valid = "0123456789()."
        for _ in self.__number:
            if _ not in valid:
                return False
        return True
    
    def Get_id(self):
        return self.__id
    def Get_Number(self):
        return self.__number
    def set_id(self, id: str):
        self.__id = id
    def set_number(self, number: str):
        self.__number = number


class Contact:
    def __init__(self, name: str):
        self.__name = name
        self.favorited = False
        self.fone: list[Fone] = []

    def addFone(self, id: str, number: str):
        fone = Fone(id, number)
        if fone.isValid():
            self.fone.append(fone)
        else:
            raise Exception ("fail: invalid number")
        
    def RemoveFone(self, index: int):
        if 0 <= index < len(self.fone):
            self.fone.pop(index)
        else:
            raise Exception ("fail: index errado")
        
    def tfav(self):
        self.favorited = not self.favorited

    def fav(self):
        return self.favorited


    def getFone(self):
        return self.fone
    
    def getName(self):
        return self.__name
    
    def setName(self, name: str):
        self.__name = name



    def __str__(self):
        lista = ", ".join([str(x) for x in self.fone])
        if self.favorited:
            return f"@ {self.__name} [{lista}]"
        else:
            return f"- {self.__name} [{lista}]"





class Agenda:
    def __init__(self):
        self.contacts: list[Contact] = []


    def posicition(self, name: str):
        for i, n in enumerate(self.contacts):
            if n.getName() == name:
                return i
            
        return -1
    

    def removeContact(self, name: str):
        pos = self.posicition(name)
        if pos == -1:
            raise Exception ("fail: nao encontrado")
        else:
            self.contacts.pop(pos)

    def getFavorited(self):
        return [contatos for contatos in self.contacts if contatos.fav()]

    def Get_contact(self, name: str):
        pos = self.posicition(name)
        if pos == -1:
            raise Exception ("fail: nao encontrado")
        return self.contacts[pos]



    def addContact(self, name: str, fones: Fone):
        pos = self.posicition(name)
        if pos != -1:
            for _ in fones:
                self.contacts[pos].addFone(_.Get_id(), _.Get_Number())
        else:
            contact = Contact(name)
            for _ in fones:
                contact.addFone(_.Get_id(), _.Get_Number())
            self.contacts.append(contact)
            self.contacts.sort(key=lambda x: x.getName().lower())


    def busca(self, padrao: str):
        resultado = []
        padrao = padrao.lower()

        for contact in self.contacts:
            found = False


            if padrao in contact.getName().lower():
                found = True
            else:
                for fone in contact.getFone():
                    if padrao in fone.Get_id().lower() or padrao in fone.Get_Number():
                        found = True

            if found:
                resultado.append(contact)
        return resultado





    def __str__(self):
        lista = "\n".join([str(x) for x in self.contacts])
        return f"{lista}"





def main():
    agenda = Agenda()
    while True:
        try:
            line = input()
            print("$"+line)
            args = line.split()
            if args[0] == "end":
                break
            elif args[0] == "show":
                print(agenda)
            elif args[0] == "add":
                name = args[1]
                fones = []
                for itens in args[2:]:
                    id, number = itens.split(":")
                    fones.append(Fone(id, number))
                agenda.addContact(name, fones)
            elif args[0] == "rmFone":
                name = args[1]
                index = int(args[2])
                contact = agenda.Get_contact(name)
                contact.RemoveFone(index)
            elif args[0] == "rm":
                agenda.removeContact(args[1])

            elif args[0] == "search":
                res = agenda.busca(args[1])
                for c in res:
                    print(c)
            elif args[0] == "tfav":
                try:
                    contact = agenda.Get_contact(args[1])
                    contact.tfav()
                except Exception as e:
                    print(e)
            elif args[0] == "favs":
                for contact in agenda.getFavorited():
                    print(contact)
            else:
                print("fail: comando não encontrado")
        except Exception as e:
            print(e)



main()





