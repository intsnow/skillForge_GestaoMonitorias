from mentor import Mentor

class Cadastro:

    def __init__(self, mentor):
        self.nome = mentor.nome
        self.email = mentor.email
        self.idade = mentor.idade
        self.precoHora = mentor.precoHora
        self.mentor = mentor


    def displayInfo(self):

        if self.mentor:
            print(f"\tNome : {self.nome} ")
            print(f"\tEmail : {self.email} ")
            print(f"\tIdade : {self.idade} ")
            print(f"\tPreço_Hora : {self.precoHora} ")
     