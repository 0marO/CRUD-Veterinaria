import mysql.connector

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
                            (id_duenio,
                            Nombre varchar(50),
                            Apellido varchar(50),
                            Email varchar(50),
                            DNI int, 
                            Direccion varchar(200),
                            Telefono int,
                            PRIMARY KEY(id_duenio)
                            );
                        """)

        mycursor.execute(f"""INSERT INTO duenio 
                            VALUES ('{nombre}',
                                    '{apellido}',
                                    '{email}',
                                     {dni},
                                    '{direccion}',
                                     {telefono});
                        """)
        
        mydb.commit()
        mydb.close()


def IngresarMascotaDB(nombre, tipo, raza, edad, id_duenio, id_duenio2):

        mydb = ConectarConDb()
        mycursor = mydb.cursor()

        mycursor.execute("""CREATE TABLE IF NOT EXISTS paciente (id_mascota NOT NULL AUTO_INCREMENT,
                                                                 Nombre varchar(50) NOT NULL,
                                                                 Tipo varchar(50) NOT NULL,
                                                                 Raza varchar(50) NOT NULL,
                                                                 Edad int NOT NULL,
                                                                 id_duenio int NOT NULL,
                                                                 id_duenio2 ints,
                                                                 PRIMARY KEY (id_mascota),
                                                                 FOREIGN KEY (id_duenio) REFERENCES Persons(id_duenio),
                                                                 FOREIGN KEY (id_duenio2) REFERENCES Persons(id_duenio2)
                                                                );
                        """)

        mycursor.execute(f"""INSERT INTO paciente 
                            VALUES ('{nombre}',
                                    '{tipo}',
                                    '{raza}',
                                     {edad},
                                     {id_duenio},
                                     {id_duenio2},
                                    );
                        """)
        
        mydb.commit()
        mydb.close()


def BuscarRegistroPorIdMascota(IdMascota):

        mydb = ConectarConDb()
        mycursor = mydb.cursor()

        mycursor.execute(f"""SELECT * FROM paciente WHERE id_mascota == {IdMascota}""")

        myresult = mycursor.fetchall()
        mydb.close()

        return myresult

def BuscarRegistroPorDniDueño(DniDueño):

        mydb = ConectarConDb()
        cursor = mydb.cursor()

        cursor.execute(f"""SELECT * FROM paciente WHERE DniDuenio == {DniDueño} OR DniDuenio2 == {DniDueño}""")

        resultado =  cursor.fetchall()
        mydb.close()

        return resultado

def BuscarRegistroPorNombreDueño(NombreDueño):

        mydb = ConectarConDb()
        cursor = mydb.cursor()

        cursor.execute(f"""SELECT * FROM paciente 
                           WHERE nombreDuenio LIKE '%{NombreDueño}%' OR nombreDuenio2 LIKE '%{NombreDueño}%' """)

        resultado =  cursor.fetchall()
        mydb.close()

        return resultado

def BuscarRegistroPorNombrePaciente(NombrePaciente):

        mydb = ConectarConDb()
        cursor = mydb.cursor()

        cursor.execute(f"""SELECT * FROM paciente 
                           WHERE Nombre LIKE '%{NombrePaciente}%' OR Nombre LIKE '%{NombrePaciente}%' """)

        resultado =  cursor.fetchall()
        mydb.close()

        return resultado