from mentor import Mentor
from cadastro import Cadastro
from sistemaCadastro import SistemaCadastro
from database import Database as db

# print("\n\nIniciando Cadastro:  ")
# mentores = [
#     Mentor("Ana", "ana@email.com", 17, 12.40),
#     Mentor("Iago", "iago@email.com", 27, 15.00),
#     Mentor("Lilás", "lilas@email.com", 20, 12.00) 1
# ]


sistema = SistemaCadastro("bd_cadastrosMentoriaValidos.db")
sistema.displayMenu()


