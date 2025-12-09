from cadastro import Cadastro
from mentor import Mentor
from database import Database as db
import textwrap

class SistemaCadastro:

    def __init__(self, dbNome): 
        self.dbNome = dbNome
        self.db = self.startBD()


    def startBD(self):
        return db(self.dbNome)
    

    def cadastrarMentor(self, mentor=None):
        print("\nIniciando cadastro...\n")

        if not mentor:
            dados = {}

            mentor = Mentor.empty()

            #    Itera sobre as chaves, ou seja, nomes_atributos de Mentor
            #   e adiciona valores de input_usuario à cada chave.
            for atr in mentor.__dict__.keys():
                dados.__setitem__(atr, input(f"\nDigite o {atr}_mentor: \t"))

            mentor = Mentor.inputDados(dados)

        # cad = Cadastro(mentor)

        if int(mentor.idade) >= 18:
            self.db.addMentor(mentor)
            print(f"\nMentor \"{mentor.nome}\" cadastrado com sucesso!!")
            
        # else:
        #     self.cadastrosInvalidos.append(cad)

            
    def listarMentores(self):
        print("\n(opçao 2) --> Display da lista de Mentores Deferidos: ")
        
        linhas, atributos = self.db.listMentores()

        cont = 0
        for linha in linhas:
            print(f"\n\n\tDados do Mentor_ID_({cont}):")

            # Posição ZERO possui o ID, entao: linha[1] em diante
            for i in range(len(atributos)):
                print(f"\n\t\t{atributos[i]}:  {linha[i+1]}")

            cont += 1

    
    def excluirMentor(self, mentor=None):

        if mentor and self.db.rmvMentor(mentor):
            print(f"\nMentor {mentor.nome} removido do Sistema!")

        else:
            opComando = input(
                "\n\tPara exclusão filtrada, dentre as opções:" \
                "\n\t\t1:   via EMAIL" \
                "\n\t\t\tDigite a opção de escolha:\t")
            
            atributos = {
                "email" : None
            }
            
            match int(opComando):

                case 1:
                    atributos = {
                        "email": input(f"\nDigite o EMAIL do mentor a ser deletado:\t")
                    }
                    
        

            #  Coleta mentor no BD através do atributo EMAIL escolhido
            mentorTmp = self.db.getMentorByAtributo(atributos)

            if self.db.rmvMentor(mentorTmp, opComando):   
                print(f"\nMentor {mentorTmp.nome} removido do Sistema!")
            


    def displayInfo(self):
        i = 1
        
        print("\nCadastrados bem sucedidos:")
        for cad in self.cadastrosValidos:
            print()
            print(f"\nInfos de Cadastro_{i}:")
            cad.displayInfo()
            i += 1

        print("\n\nCadastros MAL sucedidos ( idade < 18 anos):")
        for cad in self.cadastrosInvalidos:
            print()
            cad.displayInfo()
            print()


    def displayMenu(self):
        while True:

            op = input(
                "\n\t\t=== SISTEMA DE MENTORIA === \n" \
                "\n\t1. Cadastrar Novo Mentor " \
                "\n\t2. Listar Mentores (Ler do Banco de Dados)" \
                "\n\t3. Excluir Mentor (Pelo E-mail)"   \
                "\n\t4. Sair" \
                "\n\n\tDigite o numero_comando:\t"
            )

            match int(op):
                case 1:
                    self.cadastrarMentor()
                case 2:
                    self.listarMentores()
                case 3:
                    self.excluirMentor()

                case 4: 
                    print("Finalizando...") 
                    self.db.exitBD()
                    return