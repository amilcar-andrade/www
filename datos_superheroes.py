

import MySQLdb

# connect to the MySQL server

conn = MySQLdb.connect (host = "localhost", user = "root", db = "prueba")

# create the animal table and populate it


cursor = conn.cursor ()
cursor.execute ("DROP TABLE IF EXISTS superheroes")
cursor.execute ("""
      CREATE TABLE superheroes
      (
        nombre     CHAR(40),
        identidad CHAR(40),
        sexo CHAR(40)

      )
    """)

cursor.execute ("""
      INSERT INTO superheroes (nombre,identidad, sexo)
      VALUES
        ('Superman', 'Clark Kent', 'Masculino'),
	         ('Hombre Arana', 'Peter Parker', 'Masculino'),
	         ('Boltie', 'Libby', 'Femenino'),
	         ('Capitan America', 'Steve Rogers', 'Masculino'),
	         ('Linterna Verde', 'Hal Jordan', 'Masculino'),
	         ('Mujer Maravilla', 'Diana Prince', 'Femenino'),
	         ('Lobezno', 'Logan', 'Masculino'),
	         ('Batichica', 'Barbara Gordon', 'Femenino'),
	         ('El Increible Hulk', 'Bruce Banner', 'Masculino'),
	         ('Mujer Invisible', 'Susan Storm de Richards', 'Femenino'),
	         ('Thor', 'Donald Blake', 'Masculino'),
	         ('Viuda Negra', 'Natasha Romanoff', 'Femenino'),
	         ('Hombre Plancha', 'Anthony Stark', 'Masculino'),
	         ('Batman', 'Bruno Diaz', 'Masculino'),
	         ('Ruby Thursday', 'Thursday Rubinstein', 'Femenino')
	     """)


cursor.close ()
conn.commit ()
conn.close ()



