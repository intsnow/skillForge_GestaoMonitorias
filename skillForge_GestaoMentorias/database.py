import sqlite3 as sql
from mentor import Mentor 

class Database:

    def __init__(self, dbNome):
        self.dbNome = dbNome
        self.conn = None
        self.cursor = None
        self.exit = False
        self.connectBD()
        

    def createTabelas(self):
            
        # Desabilitar journal para evitar possiveis LOCK erros
        self.cursor.execute("PRAGMA journal_mode=OFF;")
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS mentores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT PRIMARY KEY NOT NULL,
                idade INTEGER NOT NULL,
                precoHora FLOAT NOT NULL
            );
        """)

        self.conn.commit()
            
            
    def addMentor(self, mentor):
        
        data = [(mentor.nome, mentor.email, mentor.idade, mentor.precoHora)]
        self.cursor.executemany("""
            INSERT INTO mentores (nome, email, idade, precoHora)
            VALUES (?, ?, ?, ?);
        """, data)

        self.conn.commit()



    def addMentores(self, mentores):

        # Tupla de parametros em cada Mentor, contra HACKERS SQL_Injection!!!
        data = [(mentor.nome, mentor.email, mentor.idade, mentor.precoHora) for mentor in mentores]
        self.cursor.executemany("""
            INSERT INTO mentores (nome, email, idade, precoHora)
            VALUES (?, ?, ?, ?);
        """, data)

        nomes = [mentor.nome for mentor in mentores]
        # print(f"\nMentores {nomes} registrados com sucesso!")
        self.conn.commit()


    def rmvMentor(self, mentor, opComando=None):

        if opComando:
            print("\n\tRemovendo by EMAIL...")
            match int(opComando):
                
                case 1:
                    self.cursor.execute("""
                        DELETE FROM mentores
                        WHERE email = ?
                        """, [mentor.email]
                    )
            
                    self.conn.commit()
                    return True
                
            return False
       

    def getMentorByAtributo(self, atributos):

        #   Criando coluna de chaves validas para evitar SQL Injection
        chaveValidas= {"id", "email"}

        #   Coleta primeiro atributo como chave
        chave = next(iter(atributos))

        # if chave not in chaveValidas:
        #     print("FALHA! Chave_index INVALIDA!!")
        #     return

        valor = atributos[chave]

        self.cursor.execute(str(f"""
            SELECT * FROM mentores
            WHERE {chave} = ?    
        """), [valor]
        )

        mentor = None

        linhaResu = self.cursor.fetchall()
        
        if len(linhaResu) == len(atributos.keys()):
            mentor = Mentor(
                linhaResu[0][1],
                linhaResu[0][2],
                linhaResu[0][3],
                linhaResu[0][4]
            )

        return mentor


    def listMentores(self):
        
        self.cursor.execute(
            "SELECT * FROM mentores"
        )

        linhas = self.cursor.fetchall()
        mentorTmp = Mentor.empty()
        atributos = [str(atr) for atr in vars(mentorTmp)] 

        return linhas, atributos

        
    def exitBD(self):
        self.exit = True


    def connectBD(self):
        
        try:
            self.conn = sql.connect(self.dbNome)
            self.cursor = self.conn.cursor()
            self.createTabelas()
            # self.exitBD()

            print("\n\nConexão com DB feita com sucesso!")

        except Exception as e:
            print("\n\nErro ao conectar: ", type(e).__name__, "-", e)

        finally:
            if self.conn and self.exit:
                self.conn.close()





        
