import sqlite3

conn = sqlite3.connect('produtos.db')

cursor = conn.cursor ()

novo_produto = ('camiseta, 79.99, 53')

inserir_produto = "INSERT INTO produtos( nome, preço, estoque) VALUES (?,?,?)"

cursor.execute(inserir_produto , novo_produto)

conn.commit()

conn .close()