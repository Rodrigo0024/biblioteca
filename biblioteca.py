import mysql.connector
from mysql.connector import Error

def criar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='localhost',       # Substitua pelo seu host, se necessário
            database='biblioteca',
            user='root',            # Substitua pelo seu usuário
            password='geladeira12'    # Substitua pela sua senha
        )
        if conexao.is_connected():
            print("Conexão bem-sucedida!")
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None
    


def inserir_livro(conexao, titulo, autor, ano_publicacao):
    try:
        cursor = conexao.cursor()
        sql = " INSERT INTO Livros (titulo, autor, ano_publicacao) VALUES (%s, %s, %s)"
        valores = (titulo, autor, ano_publicacao)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"Livro '{titulo}' adicionado com sucesso!")
    except Error as e:
        print(f"Erro ao inserir livro: {e}")

def listar_livros(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM Livros")
        livros = cursor.fetchall()
        for livro in livros:
            print(livro)
    except Error as e:
        print(f"Erro ao listar livros: {e}")

def atualizar_livro(conexao, id, novo_titulo):
    try:
        cursor = conexao.cursor()
        sql = "UPDATE Livros SET titulo = %s WHERE id = %s"
        valores = (novo_titulo, id)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"Livro com ID {id} atualizado para '{novo_titulo}'!")
    except Error as e:
        print(f"Erro ao atualizar livro: {e}")
def excluir_livro(conexao, id):
    try:
        cursor = conexao.cursor()
        sql = "DELETE FROM Livros WHERE id = %s"
        valores = (id,)
        cursor.execute(sql, valores)
        conexao.commit()
        print(f"Livro com ID {id} excluído com sucesso!")
    except Error as e:
        print(f"Erro ao excluir livro: {e}")


if __name__ == "__main__":
    # Conectar ao banco de dados
    conexao = criar_conexao()
    if conexao is not None:
        # Inserir um livro
        inserir_livro(conexao, "ratão grande", "viuvinho", 1605)

        # Listar livros
       # print("\nLista de Livros:")
       # listar_livros(conexao)

        # Atualizar um livro
       # atualizar_livro(conexao, 1, "Dom Quixote (Edição Especial)")

        # Listar livros novamente
        print("\nLista de Livros após atualização:")
        listar_livros(conexao)

        # Excluir um livro
       # excluir_livro(conexao, 1)

        # Fechar conexão
        conexao.close()
        print("Conexão encerrada.")