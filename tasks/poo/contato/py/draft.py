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