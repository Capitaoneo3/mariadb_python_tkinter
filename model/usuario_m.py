import sqlite3

class Usuario:
    def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade

class UsuarioModel:
    def __init__(self, db_name='exemplo.db'):#caminho do banco
        self.conn = sqlite3.connect(db_name)#comando que conecta e cria o banco
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                idade INTEGER
            )
        ''')
        self.conn.commit()

    def inserir_usuario(self, nome, idade):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO usuarios (nome, idade)
            VALUES (?, ?)
        ''', (nome, idade))
        self.conn.commit()

    def selecionar_usuarios(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM usuarios')
        return cursor.fetchall()

    def fechar_conexao(self):
        self.conn.close()


