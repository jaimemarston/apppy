import json
import xlwt
import sqlite3
from itertools import islice

def lista():
    
    print ("Lista de contactos")
    print ("------------------")
    print ("")

    con = sqlite3.connect("agenda.db")
    cursor = con.cursor()

    cursor.execute("SELECT * FROM datos")
    resultado = cursor.fetchall()

    for i in resultado:
        print ("%s %s %s %s %s %s %s" % (i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

    cursor.close()

    print ("")

con = sqlite3.connect("agenda.db")
cursor = con.cursor()

cursor.execute('''DELETE FROM datos''')
con.commit()


# Insert user 1
#

#con.executemany('''INSERT INTO datos(nombre, telefono, correo, dire,empresa,vigente)
#                  VALUES(?,?,?,?,?,?)''', (nombre, telefono, correo, dire,empresa,vigente))



g = open("destino.txt", "r")

line_number=6
#for linea in g.readlines():
#    print linea
row_num =0
datosfinal = {}
insertadatos = [] #empty list
with g as fichero:         
    
    
    ntelf = 0
    ncorreo = 0
    ndire=0
    ndepa=0
    direccion=""
    departamento=""
    nombre=""
    for linea in fichero:
        description = linea
        row_num += 1

        #print (row_num,description)
        if description.find('teléfono:')>=0:
           #print (lines[row_num])
           #print (row_num,description)
           ntelf = row_num
          

           with open("destino.txt", "r") as f:
                line=f.readlines()[row_num - 3]
                
           nombre = line[:-1]

        if description.find('correo electrónico:')>=0:
           ncorreo = row_num
           
        if description.find('dirección:')>=0:   
           ndire = row_num

        if description.find('departamento:')>=0:   
           ndepa = row_num
           # 

        
        if ntelf + 2 == row_num:
           telefono = description[:-1]
        
        if ncorreo + 2 == row_num:
           correo = description[:-1]   

        if ndire + 2 == row_num:
           direccion = description[:-1]   

        if ndepa + 2 == row_num:
           departamento = description[:-1]   

           empdatos={'telefono':telefono,'correo':correo,'nombre':nombre,'direccion':direccion,'departamento':departamento,'vigente': '1',}
           cursor.execute('INSERT INTO datos VALUES (:nombre ,:telefono , :correo, :direccion, :nombre, :departamento, :vigente, null)', empdatos)
                      
           insertadatos.append(empdatos)

           print (telefono, correo, nombre, direccion, departamento)
        #datosfinal = 'telefono:'telefono
        
g.close()



#cursor.execute('INSERT INTO datos VALUES(?,?,?,?,?,?)', insertadatos)
#values = {'telefono':'jack', 'correo':'dire', 'nombre':'Action', 'direccion':'k','departamento':'p','vigente':'1'}



   
con.commit()
cursor.close()
#print (insertadatos)
lista()

#with open(ruta, "r") as fichero:
#        for linea in fichero:
##            nombre, contr = linea[8: -1].split("  Contraseña:", 1)
##            if usuario == nombre and password == contr:
#                return True
#        return False
