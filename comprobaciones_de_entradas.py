
def ComprobarEntradaNombre(StringNombre):
        
        LongNombre = len(StringNombre)
        if StringNombre == 'Nombre' or StringNombre == 'Mascota' or LongNombre > 20:
                return False
        
        UltimaPos = LongNombre-1
        es_valido = True
        i = 0
        while (i <= UltimaPos and es_valido != False):
                if StringNombre[i] in '0123456789:;.,+*-{}[]/\¿?¡!':
                        es_valido = False
                i+=1

        return es_valido


"""
print(ComprobarEntradaNombre(123))
print(ComprobarEntradaNombre('Nombre'))
print(ComprobarEntradaNombre('Mascota'))
print(ComprobarEntradaNombre('Perrito123'))
print(ComprobarEntradaNombre('1Perrito13'))
print(ComprobarEntradaNombre('Perrito:'))
print(ComprobarEntradaNombre('Perrito.'))
print(ComprobarEntradaNombre('Perrito;'))
print(ComprobarEntradaNombre('Perrito'))
"""


def ComprobarEntradaDni(StringDni):
        
        LongDni = len(StringDni)
        if StringDni == 'DNI' or (LongDni != 8 and LongDni != 7):
                return False
        
        UltimaPos = LongDni-1
        es_valido = True
        i = 0
        while (i <= UltimaPos and es_valido != False):
                if StringDni[i] not in '0123456789':
                        es_valido = False
                i+=1

        return es_valido

"""
print(ComprobarEntradaDni('DNI'))
print(ComprobarEntradaDni('123'))
print(ComprobarEntradaDni('112223334'))
print(ComprobarEntradaDni('1122233t'))
print(ComprobarEntradaDni('t1222333'))
print(ComprobarEntradaDni('39490841'))
print(ComprobarEntradaDni('5490841'))
"""

def ComprobarEntradaTelefono(StringTelefono):
        
        LongTelefono = len(StringTelefono)
        if StringTelefono == 'Teléfono' or LongTelefono > 11 or LongTelefono < 10:
                return False
        
        UltimaPos = LongTelefono-1
        es_valido = True
        i = 0
        while (i <= UltimaPos and es_valido != False):
                if StringTelefono[i] not in '0123456789':
                        es_valido = False
                i+=1

        return es_valido

"""
print(ComprobarEntradaTelefono('123'))
print(ComprobarEntradaTelefono('123123123123123213'))
print(ComprobarEntradaTelefono('Hola123456'))
print(ComprobarEntradaTelefono('1135929824'))
print(ComprobarEntradaTelefono('20335929824'))
"""


def ComprobarEntradaEmail(StringEmail):
        
        LongTelefono = len(StringEmail)
        if StringEmail == 'Email' or LongTelefono > 40 or ('@' not in StringEmail) or (StringEmail[0] == '@') or (StringEmail[-1] == '@'):
                return False
        return True

"""
print(ComprobarEntradaEmail('@gmail.com'))
print(ComprobarEntradaEmail('Email'))
print(ComprobarEntradaEmail('123@'))
print(ComprobarEntradaEmail('123@asdfasdfasdfasdfasdfadfaadsfasdfasdfasd.com'))
print(ComprobarEntradaEmail('1@ejemplo.com'))
"""