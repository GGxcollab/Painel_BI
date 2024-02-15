
# host='10.194.5.163:3306',
# user='analiseddos',
# password='59kYxAp84wj8TNx',
# database='analiseddos',

import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="analiseddos",
        password="59kYxAp84wj8TNx",
        host="10.197.5.248",
        port=3306,
        database="analiseddos"

    
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cursor = conn.cursor() 

# CREATE
# nome_produto = "chocolate"
# valor = 15
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados


# READ
comando = f'SELECT * FROM alerts'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)


# UPDATE
# nome_produto = "todynho"
# valor = 6
# comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados

# DELETE
# nome_produto = "todynho"
# comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados


cursor.close()
conn.close()


# # Conectar ao banco de dados
# try:
#     conexao = mysql.connector.connect(
#         host='10.194.5.163:3306',
#         database='analiseddos',
#         user='analiseddos',
#         password='59kYxAp84wj8TNx'
#     )

#     if conexao.is_connected():
#         print("Conexão bem-sucedida!")

#         # Executar consultas ou operações no banco de dados aqui

# except mysql.connector.Error as err:
#     print(f"Erro de conexão: {err}")

# finally:
#     # Fechar a conexão quando terminar
#     if 'conexao' in locals():
#         conexao.close()
#         print("Conexão encerrada.")


# #cursor = conexao.cursor()

