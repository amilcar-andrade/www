#!/usr/bin/env python
# coding: utf-8

# Archivo: movies.py
from xml.dom.minidom import parse, parseString, Document

# parsear un documento XML indicando su nombre de archivo
dom = parse('movies.xml')
film = dom.toprettyxml(encoding='UTF-8')
film = dom.getElementsByTagName('film')

print 'Content-type: text/html; charset=utf-8'

# MUY IMPORTANTE: Imprimir una linea en blanco para delimitar
# los encabezados del cuerpo de la respuesta.

print 

print '''<!DOCTYPE html>

<html lang="es">

    <head>
        <link rel="stylesheet" href="http://twitter.github.com/bootstrap/1.4.0/bootstrap.min.css">
        <meta charset="utf-8"/>
        <title>Práctica XML</title>
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
		           <th>Película</th>
                <th>Año</th>
                <th>Director</th>
                <th>Actores</th>
		          </tr>
		        </thead>
		        <tbody>

'''

               
for node in film:

    print '<tr>'
    print '<td>' + node.getAttribute('name') + '</td>' + '<td>' + node.getAttribute('year') + '</td>'

    try:
        print '<td>' + node.getElementsByTagName('director').item(0).firstChild.nodeValue + '</td>'

    except:
        print '<td> &nbsp; </td>'

    print '<td>'

    act_list = node.getElementsByTagName('cast')
    for v in act_list:
        print   v.firstChild.nodeValue + ","

    print '</td>  </tr>'

print '''
		        </tbody>
		      </table>

        </div>
      </div>
</div>
</div>        
    </body>

</html>'''