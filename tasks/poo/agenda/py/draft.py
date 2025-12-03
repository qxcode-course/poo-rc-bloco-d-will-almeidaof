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
        self.fone: list[Fone] = []

    def addFone(self, id: str, number: str):
        fone = Fone(id, number)
        if fone.isValid():
            self.fone.append(fone)
        else:
            print("fail: invalid number")




    def __str__(self):
        lista = ", ".join([str(x) for x in self.fone])
        return f"{self.__name} [{lista}]"





class Agenda:
    def __init__(self):
        self.contacts: list[Contact] = []


    def addContact(self, name: str, id: str, number: str):
        contact = Contact(name)
        contact.addFone(id, number)
        self.contacts.append(contact)



    def __str__(self):
        lista = "/n ".join([str(x) for x in self.contacts])
        return f"{lista}"





fone = Fone("eva","8890")
print(fone)
contact = Contact("Will")
print(contact)
contact.addFone("ester","8800")
print(contact)
agenda = Agenda()
agenda.addContact("Will","Ester","8800")
agenda.addContact("Ester","Will","8800")
print(agenda)