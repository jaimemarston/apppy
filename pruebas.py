import sqlite3
print ("Lista de contactos")
print ("------------------")
print ("")

con = sqlite3.connect("agenda.db")
cursor = con.cursor()

cursor.execute("SELECT * FROM datos")
resultado = cursor.fetchall()

for i in resultado:
    #print ("%s %s %s %s %s %s %s" % (i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
    print (i[0].ljust(80),i[1].ljust(30),i[2].ljust(40),i[3],i[5],sep="|")
  

cursor.close()

print ("")
input("Presione una tecla para continuar...")