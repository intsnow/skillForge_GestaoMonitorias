class Mentor:

    def __init__(self, nome, email, idade, precoHora, id=None ):
        self.nome = nome
        self.email = email
        self.idade = idade
        self.precoHora = precoHora

    @classmethod
    def empty(cls):
        return cls("Sem nome", "n/a", 0, 0.0)
    
    
    @classmethod
    def inputDados(cls, dados):

        valores = [val for val in dados.values() ]

        return cls(valores[0], valores[1], valores[2], valores[3])
    



