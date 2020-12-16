import sqlite3

banco = sqlite3.connect("banco_funcionarios.db")

cursor = banco.cursor()

#cursor.execute("CREATE TABLE funcionarios (nome text, CPF integer, Atestado text )")

#cursor.execute("INSERT INTO funcionarios VALUES ('Pâmela Cassiano Cunha', 08680254434, 'NÃO') ")
#cursor.execute("INSERT INTO funcionarios VALUES ('Maria Eduarda Lopes', 12345678898, 'SIM') ")
#cursor.execute("INSERT INTO funcionarios VALUES ('Lucas Silva Junior', 08675434543, 'SIM') ")
banco.commit()
cursor.execute("SELECT * FROM funcionarios")
print(cursor.fetchall())