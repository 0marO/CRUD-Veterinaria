from unittest import result
import mysql.connector

from constantes import *

def ConectarConDb():

        mydb = mysql.connector.connect(
        host="localhost",
        user="root",   #MAS ADELANTE CAMBIAR 
        port= "3306",
        password="abc123", #MAS ADELANTE CAMBIAR 
        database="vete_db"
        )

        return mydb


def IngresarDueñoDB(nombre, apellido, email, dni, direccion, telefono):

        mydb = ConectarConDb()
        mycursor = mydb.cursor()

        mycursor.execute("""CREATE TABLE IF NOT EXISTS duenio 
                            (id_duenio int NOT NULL AUTO_INCREMENT,
                            Nombre varchar(50),
                            Apellido varchar(50),
                            Email varchar(50),
                            DNI int, 
                            Direccion varchar(200),
                            Telefono int,
                            PRIMARY KEY(id_duenio)
                            );
                        """)

        # TEMPORAL
        mycursor.execute("SHOW TABLES")
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        # ----------------------------


        mycursor.execute(f"""INSERT INTO duenio(Nombre, Apellido, Email, DNI, Direccion, Telefono)
                            VALUES ('{nombre}',
                                    '{apellido}',
                                    '{email}',
                                     {dni},
                                    '{direccion}',
                                     {telefono});
                        """)
        
        mydb.commit()

        # TEMPORAL
        mycursor.execute("SELECT * FROM duenio")
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        # ----------------------------

        mydb.close()


def IngresarMascotaDB(nombre, tipo, raza, edad, dni_dueño, dni_dueño2 = ''):

        mydb = ConectarConDb()
        mycursor = mydb.cursor()

        mycursor.execute("""CREATE TABLE IF NOT EXISTS paciente (id_mascota int NOT NULL AUTO_INCREMENT,
                                                                 Nombre varchar(50) NOT NULL,
                                                                 Tipo varchar(50) NOT NULL,
                                                                 Raza varchar(50) NOT NULL,
                                                                 Edad int NOT NULL,
                                                                 id_duenio int NOT NULL,
                                                                 id_duenio2 int,
                                                                 PRIMARY KEY (id_mascota),
                                                                 FOREIGN KEY (id_duenio) REFERENCES duenio(id_duenio),
                                                                 FOREIGN KEY (id_duenio2) REFERENCES duenio(id_duenio)
                                                                );
                        """)

        # TEMPORAL
        mycursor.execute("SHOW TABLES")
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        # ----------------------------

        # TEMPORAL
        mycursor.execute("SELECT * FROM duenio")
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        # ----------------------------

        if dni_dueño2 != '':
                mycursor.execute(f"""INSERT INTO paciente(Nombre, Tipo,Raza,Edad,id_duenio,id_duenio2)
                                VALUES ('{nombre}',
                                        '{tipo}',
                                        '{raza}',
                                         {edad},
                                        (SELECT id_duenio FROM duenio WHERE DNI = {dni_dueño} LIMIT 1),
                                        (SELECT id_duenio FROM duenio WHERE DNI = {dni_dueño2} LIMIT 1));
                                """)
                
                mydb.commit()
        else:
                mycursor.execute(f"""INSERT INTO paciente(Nombre, Tipo,Raza,Edad,id_duenio)
                                VALUES ('{nombre}',
                                        '{tipo}',
                                        '{raza}',
                                         {edad},
                                        (SELECT id_duenio FROM duenio WHERE DNI = {dni_dueño} LIMIT 1));
                                """)
                
                mydb.commit()


        print('\nAHORA TODO DE PACIENTES:\n')
        # TEMPORAL
        mycursor.execute("SELECT * FROM paciente")
        myresult = mycursor.fetchall()
        for x in myresult:
                print(x)
        # ----------------------------

        mydb.close()


def BuscarRegistroPorIdMascota(IdMascota):

        mydb = ConectarConDb()
        mycursor = mydb.cursor()

        mycursor.execute(f"""   SELECT  p.Nombre, p.id_mascota, p.Raza, p.Edad, 
                                        d.Nombre, d.DNI, d.Email, d.Telefono,            -- Dueño 1
                                        d2.Nombre, d2.DNI, d2.Email, d2.Telefono         -- Dueño 2
                                FROM paciente AS p
                                        INNER JOIN duenio AS d
                                                ON p.id_duenio = d.id_duenio
                                        LEFT JOIN duenio AS d2
                                                ON p.id_duenio2 = d2.id_duenio
                                WHERE p.id_mascota = {IdMascota};""")

        myresult = mycursor.fetchall()
        mydb.close()
        return myresult

def BuscarRegistroPorDniDueño(DniDueño):

        mydb = ConectarConDb()
        cursor = mydb.cursor()

        cursor.execute(f"""   SELECT  p.Nombre, p.id_mascota, p.Raza, p.Edad, 
                                        d.Nombre, d.DNI, d.Email, d.Telefono,            -- Dueño 1
                                        d2.Nombre, d2.DNI, d2.Email, d2.Telefono         -- Dueño 2
                                FROM paciente AS p
                                        INNER JOIN duenio AS d
                                                ON p.id_duenio = d.id_duenio
                                        LEFT JOIN duenio AS d2
                                                ON p.id_duenio2 = d2.id_duenio
                                WHERE d.DNI = {DniDueño} OR d2.DNI = {DniDueño};""")

        myresult = cursor.fetchall()
        mydb.close()
        return myresult

def BuscarRegistroPorNombreDueño(NombreDueño):

        mydb = ConectarConDb()
        cursor = mydb.cursor()

        cursor.execute(f"""   SELECT  p.Nombre, p.id_mascota, p.Raza, p.Edad, 
                                        d.Nombre, d.DNI, d.Email, d.Telefono,            -- Dueño 1
                                        d2.Nombre, d2.DNI, d2.Email, d2.Telefono         -- Dueño 2
                                FROM paciente AS p
                                        INNER JOIN duenio AS d
                                                ON p.id_duenio = d.id_duenio
                                        LEFT JOIN duenio AS d2
                                                ON p.id_duenio2 = d2.id_duenio
                                WHERE d.Nombre LIKE '%{NombreDueño}%' OR d2.Nombre LIKE '%{NombreDueño}%' """)

        resultado =  cursor.fetchall()
        mydb.close()
        return resultado

def BuscarRegistroPorNombrePaciente(NombrePaciente):

        mydb = ConectarConDb()
        cursor = mydb.cursor()

        cursor.execute(f"""   SELECT  p.Nombre, p.id_mascota, p.Raza, p.Edad, 
                                        d.Nombre, d.DNI, d.Email, d.Telefono,            -- Dueño 1
                                        d2.Nombre, d2.DNI, d2.Email, d2.Telefono         -- Dueño 2
                                FROM paciente AS p
                                        INNER JOIN duenio AS d
                                                ON p.id_duenio = d.id_duenio
                                        LEFT JOIN duenio AS d2
                                                ON p.id_duenio2 = d2.id_duenio
                                WHERE p.Nombre LIKE '%{NombrePaciente}%'  """)

        resultado =  cursor.fetchall()
        mydb.close()
        return resultado

def ObtenerDatosDueñoPorDni( DniDueño):
        mydb = ConectarConDb()
        mycursor = mydb.cursor()


        mycursor.execute(f"""   SELECT d.Nombre, d.id_duenio, d.DNI, d.Email, d.Telefono 
                                FROM duenio AS d
                                WHERE   d.DNI = {DniDueño}
                                LIMIT 1""")
        
        myresult = mycursor.fetchall()
        mydb.close()
        return myresult if len(myresult) >0 else False

def CambiarRegistro(NombreMasc, IdMasc, Raza, Edad, Iddueño1, Iddueño2 = -1):

        mydb = ConectarConDb()
        mycursor = mydb.cursor()

        if Iddueño2 != -1:
                mycursor.execute(f"""   UPDATE paciente AS p
                                        SET     p.Nombre = '{NombreMasc}', 
                                                p.Raza = '{Raza}', 
                                                p.Edad = {Edad},
                                                p.id_duenio = {Iddueño1},
                                                p.id_duenio2 = {Iddueño2}
                                        WHERE p.id_mascota = {IdMasc}""")
        else:
                mycursor.execute(f"""   UPDATE paciente AS p
                                        SET     p.Nombre = '{NombreMasc}', 
                                                p.Raza = '{Raza}', 
                                                p.Edad = {Edad},
                                                p.id_duenio = {Iddueño1},
                                                p.id_duenio2 = NULL
                                        WHERE p.id_mascota = {IdMasc}""")

        mydb.commit()

        mydb.close()

        