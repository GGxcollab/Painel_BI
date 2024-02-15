
import mariadb
import sys
from dotenv import load_dotenv
import os

load_dotenv()


host = os.environ['HOST']
user = os.environ['USER']
password = os.environ['PASSWORD']
database = os.environ['DATABASE']
port = int(os.environ['PORT'])

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user=user,
        password=password,
        host=host,
        port=port,
        database=database
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    #sys.exit(1)

# # Get Cursor
cursor = conn.cursor() 

# READ
comando = f'SELECT * FROM alerts'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)

cursor.close()
conn.close()



# CREATE
# nome_produto = "chocolate"
# valor = 15
# comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
# cursor.execute(comando)
# conexao.commit() # edita o banco de dados


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



