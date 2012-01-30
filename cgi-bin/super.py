#!/usr/bin/env python
# coding: utf-8

import MySQLdb

# connect to the MySQL server
conn = MySQLdb.connect (host = "localhost",user = "root", db = "prueba")

print 'Content-type: text/html; charset=utf-8'

# MUY IMPORTANTE: Imprimir una linea en blanco para delimitar
# los encabezados del cuerpo de la respuesta.

print 

print '''<!DOCTYPE html>

<html lang="es">

    <head>
        <link rel="stylesheet" href="http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css">
        <meta charset="utf-8"/>
        <title>Primera Pracitca</title>
    </head>
    <body>
       <div class="container well">

      <div class="content">
        <div class="page-header">
        <h1>Tabla SuperHeroes</h1>
        </div>
        <div class="row">
          <div class="span16">
		<table class="bordered-table zebra-striped">
		        <thead>
		          <tr>
		            <th>Nombre</th>
		            <th>Identidad</th>
		            <th>Sexo</th>
		          </tr>
		        </thead>
		        <tbody>

''' 


# perform a fetch loop using fetchall()
cursor = conn.cursor ()
cursor.execute ("SELECT * FROM superheroes ORDER BY sexo, identidad ASC")
rows = cursor.fetchall ()
for row in rows:
   	print '<tr>'
	print '<td>' + row[0] + '</td>' + '<td>' + row[1] + '</td>' + '<td>' + row[2] + '</td>'	
	print '</tr>'

	
print '''


		        </tbody>
		      </table>

        </div>
      </div>        
    </body>

</html>'''

cursor.close ()
conn.commit ()
conn.close ()


