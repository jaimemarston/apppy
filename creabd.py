#! usr/bin/python
# -*- coding: utf-8 -*-
 
#Agenda con base de datos Sqlite3
#www.pythondiario.com
#Autor: Diego Caraballo
 
#Modulos importados
import sqlite3
import time 
import os
 
#Conexion con Base de Datos Sqlite3
con = sqlite3.connect("agenda.db")
cursor = con.cursor()
#Comprueba si la tabla existe, en caso de no existir la crea
cursor.execute("""CREATE TABLE IF NOT EXISTS datos (nombre TEXT, telefono TEXT, correo 
    TEXT, dire TEXT,empresa TEXT,departamento TEXT,  vigente TEXT, id INTEGER PRIMARY KEY AUTOINCREMENT )""")
 
cursor.close()
 
#Declaracion de las funciones
 
def limpiar():
 
    """Limpia la pantalla"""
 
    if os.name == "posix":
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system("cls")
 
def agregar():
  
    """Agrega un nuevo contacto a la Agenda"""
 
    print ("Agregar contacto")
    print ("----------------")
    print ("")
 
    con = sqlite3.connect("agenda.db")
    cursor = con.cursor()
 
    nombre = input("Nombre: ")
    telefono = input("Telefono: ")
    correo  = input("Correo: ")
    dire    = input("Direccion: ")
    empresa    = input("Empresa: ")
    departamento    = input("departamento: ")
    vigente = input("vigente (1) No (0): ")
    

    cursor.execute("insert into datos (nombre, telefono, correo, dire, empresa, departamento, vigente) \
        values ('%s','%s','%s','%s','%s','%s','%s')"%(nombre,telefono,correo,dire,empresa,departamento,vigente))
 
    con.commit()
 
    print ("Los datos fueron agregados correctamente")
 
    cursor.close()
    time.sleep(2)
    main()
 
def ver():
  
    """Devuelve todos los contactos de la agenda"""
 
    print ("Lista de contactos")
    print ("------------------")
    print ("")
 
    con = sqlite3.connect("agenda.db")
    cursor = con.cursor()
 
    cursor.execute("SELECT * FROM datos")
    resultado = cursor.fetchall()
 
    for i in resultado:
        #print ("%s %s %s %s %s" % (i[0],i[1],i[2],i[3],i[5]))
        print (i[0].ljust(80),i[1].ljust(30),i[2].ljust(40),i[3],i[5],sep="|")
 
    cursor.close()
 
    print ("")
    input("Presione una tecla para continuar...")
 
    main()
 
def buscar():
  
    """Busca un contacto en la agenda y lo lista"""
 
    print ("Buscar contacto")
    print ("---------------")
    print ("")
 
    con = sqlite3.connect("agenda.db")
    cursor = con.cursor()
 
    buscar = input("Nombre a buscar: ")
    consulta="SELECT * FROM datos WHERE nombre LIKE '%"+buscar+"%'"
    cursor.execute (consulta)
 
    x = cursor.fetchall()
 
    print ("")
 
    for i in x:
        print (i[0].ljust(80),i[1].ljust(30),i[2].ljust(40),i[3],i[5],sep="|")
        
        print ("")
 
    cursor.close()
 
    print ("")
    input("Presione una tecla para continuar...")
 
    main()
 
def eliminar():
  
    """Elimina un contacto de la Agenda"""
 
    print ("Eliminar contacto")
    print ("-----------------")
    print ("")
 
    con = sqlite3.connect("agenda.db")
    cursor = con.cursor()
 
    eliminar = input ("Nombre de contacto a eliminar: ")
 
    cursor.execute("DELETE FROM datos WHERE nombre='%s'"%(eliminar))
 
    con.commit()
 
    cursor.close()
 
    print ("Contacto eliminao correctamente...")
    input()
    main()
 
def main():
 
    """Funcion principal de la Agenda"""
 
    limpiar()
 
    print ("-----------------------------------------")
    print ("Esta es la agenda de www.MarstonSoftware.com")
    print ("-----------------------------------------")
    print ("                              Version 1.0")
    print ("""
    [1] Ingresar Contacto
    [2] Listar Contactos
    [3] Buscar Contacto
    [4] Eliminar Contacto
    [0] Salir
    """)

    
    opcion = input("Ingresa una opción -> ")

    if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "0":
        print ("Opcion incorrecta")
        input()
        main()
    elif opcion == "1":
        limpiar()
        agregar()
    elif opcion == "2":
        limpiar()
        ver()
    elif opcion == "3":
        limpiar()
        buscar()
    elif opcion == "4":
        limpiar()
        eliminar()
    elif  opcion == "0":
        print ("")
        print ("Bye...")
        print ("No te olvides de visitar www.MarstonSoftware.com :")
        print ("")
        print ("")
        time.sleep(3)
        exit()
  
 
main()