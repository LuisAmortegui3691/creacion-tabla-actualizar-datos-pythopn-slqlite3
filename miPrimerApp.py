import sqlite3

conexion = sqlite3.connect('DataBase')

cursor = conexion.cursor()
cursor.execute(''' CREATE TABLE alumnos_dos(
                        nombre TEXT,
                        apellido TEXT,
                        edad INT,
                        email TEXT,
                        id VARCHAR(20)
                    )

              ''')

cursor.execute("INSERT INTO alumnos_dos(nombre, apellido, edad, email, id) VALUES('Luis', 'Hernando', 28, 'luisamortegui.3691@gmail.com', '1')")

print('Se actualizo la tabla')
conexion.commit()
conexion.close()