
import tkinter as tk
from tkinter import *
from tkinter import ttk

from constantes import *


class App(tk.Tk):

        def __init__(self) -> None:
                super().__init__()
                
                # configuración de la ventana 
                self.title('Logi Vet')
                self.geometry('460x460')

                # Configuración del tema
                self.tk.call("source", CWD + "forest-light.tcl")
                ttk.Style().theme_use('forest-light')
                self.style = ttk.Style()
                self.style.configure('.', font = ('Calibri light', 15))

                # MARCO
                self.card = ttk.Frame(self, style='Card', padding=(5, 6, 7, 8))
                self.card.pack(pady = ESPACIO_Y)


                # LOGO
                self.logo = PhotoImage(file= CWD +'imagenes\\logo.png')
                self.LabelLogo = Label(self.card, image = self.logo)
                self.LabelLogo.pack(pady = ESPACIO_Y)

                # label SUCURSAL
                self.label = ttk.Label(self.card, text='Sucursal nro 1923')
                self.label.pack(pady = ESPACIO_Y, anchor= W)

                # BOTONES
                self.BuscarRegistro = ttk.Button(self.card,
                                                text='Buscar registro...', 
                                                style='Accent.TButton',
                                                command= lambda: self.buscar_un_registro())
                self.BuscarRegistro.pack(pady = ESPACIO_Y, anchor= W)

                self.EstadoIngresarDueño = False
                self.IngresarDueño = ttk.Button(self.card,
                                                text='Ingresar nuevo dueño',
                                                style='Accent.TButton',
                                                command= lambda: self.ingresar_dueño())
                self.IngresarDueño.pack(pady = ESPACIO_Y, anchor= W)

                self.IngresarMascota = ttk.Button(self.card,
                                                text='Ingresar nueva mascota',  
                                                style='Accent.TButton',
                                                command= lambda: self.ingresar_mascota())
                self.IngresarMascota.pack(pady = ESPACIO_Y, anchor= W)

                # MARCO BUSQUEDA
                self.MarcoBusqueda = ttk.Frame(self.card, style='Card', padding=(5, 6, 7, 8))
                self.MarcoBusqueda.pack(pady = ESPACIO_Y)

                self.label2 = ttk.Label( self.MarcoBusqueda, text='Busqueda con ID único de paciente')
                self.label2.pack(pady = ESPACIO_Y)

                self.EntradaID = EntryCustom(self.MarcoBusqueda, text='ID de mascota')
                self.EntradaID.pack(anchor= S)

        def ingresar_dueño(self):
                self.IngresoDueño = IngresoDueño()

        def ingresar_mascota(self):
                self.IngresoDueño = IngresoMascota()
                
        def buscar_un_registro(self):
                self.IngresoDueño = BuscarRegistro()

class IngresoDueño(tk.Toplevel):

        def __init__(self):
                super().__init__()
                # configuración de la ventana 
                self.title('Logi Vet Ingreso de nuevo dueño.')
                self.geometry('200x400')

                # MARCO
                self.card = ttk.Frame(self, style='Card', padding=(5, 6, 7, 8))
                self.card.pack(pady = ESPACIO_Y)

                #ENTRY
                EntryNombre = EntryCustom(self.card, text='Nombre')
                EntryNombre.pack(anchor = W, pady = ESPACIO_Y)

                EntryApellido = EntryCustom(self.card, text='Apellido')
                EntryApellido.pack(anchor = W, pady = ESPACIO_Y)

                EntryEmail = EntryCustom(self.card, text='Email')
                EntryEmail.pack(anchor = W, pady = ESPACIO_Y)

                EntryDNI = EntryCustom(self.card, text='DNI')
                EntryDNI.pack(anchor = W, pady = ESPACIO_Y)

                EntryDirección = EntryCustom(self.card, text='Dirección')
                EntryDirección.pack(anchor = W, pady = ESPACIO_Y)

                EntryTelefono = EntryCustom(self.card, text='Teléfono')
                EntryTelefono.pack(anchor = W, pady = ESPACIO_Y)

                self.IngresarMascota = ttk.Button(self.card,
                                                text='Confirmar Datos',  
                                                style='Accent.TButton',
                                                command= lambda: self.FuncionMagicaDeBackend(EntryNombre.EntradaID.get(),
                                                                                             EntryApellido.EntradaID.get(),
                                                                                             EntryEmail.EntradaID.get(),
                                                                                             EntryDNI.EntradaID.get(),
                                                                                             EntryDirección.EntradaID.get(),
                                                                                             EntryTelefono.EntradaID.get()
                                                                                             )
                                                )
                self.IngresarMascota.pack(pady = ESPACIO_Y, anchor= S)


        def FuncionMagicaDeBackend(self, nombre, apellido, email, dni, direccion, telefono):
                #esta función será remplazada por otra del backend.
                #En el caso feliz se encargará de ingresar un nuevo propietario a la base de datos
                print(nombre, apellido, email, dni, direccion, telefono)

class IngresoMascota(tk.Toplevel):

        def __init__(self):
                super().__init__()
                # configuración de la ventana 
                self.title('Logi Vet Ingreso de nueva mascota.')
                self.geometry('460x460')

                # MARCO
                self.card = ttk.Frame(self, style='Card', padding=(5, 6, 100, 9))
                self.card.pack(pady = ESPACIO_Y)
                #ENTRY
                EntryNombre = EntryCustom(self.card, text='Nombre')
                EntryNombre.pack(anchor = W, pady = ESPACIO_Y)

                ComboBoxTipoAnimal = ttk.Combobox(self.card, values = ["Canino",'Felino','Equino'
                                                                       'Rumiante','Roedor','Ave',
                                                                       'Reptil', 'Otro'
                                                                       ])
                ComboBoxTipoAnimal.pack(anchor = W, pady = ESPACIO_Y)

                EntryRaza = EntryCustom(self.card, text='Raza')
                EntryRaza.pack(anchor = W, pady = ESPACIO_Y)

                EntryEdad = EntryCustom(self.card, text='Edad')
                EntryEdad.pack(anchor = W, pady = ESPACIO_Y)

                EntryDniDueño = EntryCustom(self.card, text='DNI Dueño')
                EntryDniDueño.pack(anchor = W, pady = ESPACIO_Y)

                EntryDniDueño2 = EntryCustom(self.card, text='DNI segundo Dueño')
                EntryDniDueño2.pack(anchor = W, pady = ESPACIO_Y)

                self.IngresarMascota = ttk.Button(self.card,
                                                text='Confirmar Datos',  
                                                style='Accent.TButton',
                                                command= lambda: self.FuncionMagicaDeBackend(EntryNombre.EntradaID.get(),
                                                                                             EntryRaza.EntradaID.get(),
                                                                                             EntryEdad.EntradaID.get(),
                                                                                             EntryDniDueño.EntradaID.get(),
                                                                                             EntryDniDueño2.EntradaID.get(),
                                                                                             )
                                                )
                self.IngresarMascota.pack(pady = ESPACIO_Y, anchor= S)

        def FuncionMagicaDeBackend(self, nombre, raza, edad, dni_dueño, dni_dueño2):
                #esta función será remplazada por otra del backend.
                #En el caso feliz se encargará de ingresar un nuevo paciente a la base de datos
                print(nombre, raza, edad, dni_dueño, dni_dueño2)


class BuscarRegistro(tk.Toplevel):
        def __init__(self):
                super().__init__()
                # configuración de la ventana 
                self.title('Logi Vet Búsqueda de registros.')
                self.geometry('700x700')

                # MARCO BUSQUEDA
                self.CartaBusqueda = ttk.Frame(self, style='Card', padding=(5, 6, 10, 9))
                self.CartaBusqueda.place(x = ESPACIO_X*2, y = ESPACIO_Y)

                # SELECCION DE BUSQUEDA
                self.LabelBuscar = Label(self.CartaBusqueda, text= "Buscar por ")
                self.LabelBuscar.grid(row= 0, column= 0)

                ComboBuscarPor = ttk.Combobox(self.CartaBusqueda, values = ["ID Mascota",'Nombre Dueño',
                                                                       'DNI dueño','Nombre Paciente',],
                                               state="readonly")
                ComboBuscarPor.current(0)
                ComboBuscarPor.grid(row= 0, column= 1)

                EntryNombre = EntryCustom(self.CartaBusqueda, text='')
                EntryNombre.grid(row= 0, column= 2, padx= 10)

                self.BtBuscar = Button(self.CartaBusqueda, text ='--->',
                                        command= self.buscar_magicamente,
                                        borderwidth = 0)
                self.BtBuscar.grid(row = 0, column = 3, padx= 10)
                
                # MARCO DATOS
                self.card = ttk.Frame(self, style='Card', padding=(5, 6, 100, 9))
                self.card.place(x = ESPACIO_X*2, y = ESPACIO_Y+MARCO_DE_BUSQUEDA)

                #ENTRY
                EntryNombre = EntryCustom(self.card, text='Nombre')
                EntryNombre.grid(row= 1, column= 0)

                EntryID = EntryCustom(self.card, text='ID mascota')
                EntryID.grid(row= 2, column= 0)

                EntryRaza = EntryCustom(self.card, text='Raza')
                EntryRaza.grid(row= 3, column= 0)

                EntryEdad = EntryCustom(self.card, text='Edad')
                EntryEdad.grid(row= 4, column= 0)

                EntryDniDueño = EntryCustom(self.card, text='DNI Dueño')
                EntryDniDueño.grid(row= 5, column= 0)

                EntryEmailDueño = EntryCustom(self.card, text='dueño@ejemplo.com')
                EntryEmailDueño.grid(row= 5, column= 1, padx= 10)

                EntryTelefono = EntryCustom(self.card, text='Telefono')
                EntryTelefono.grid(row= 5, column= 2)

                EntryDniDueño2 = EntryCustom(self.card, text='DNI segundo Dueño')
                EntryDniDueño2.grid(row= 6, column= 0)

                EntryEmailDueño2 = EntryCustom(self.card, text='dueño2@ejemplo.com')
                EntryEmailDueño2.grid(row= 6, column= 1, padx= 10)

                EntryTelefono2 = EntryCustom(self.card, text='Telefono dueño 2')
                EntryTelefono2.grid(row= 6, column= 2)

        def buscar_magicamente(self):
                pass


class EntryCustom(ttk.Frame):
        def __init__(self, parent, text="", *args, **options):
                tk.Frame.__init__(self, parent, *args, **options)

                self.frame = Frame(self,borderwidth=0)
                self.frame.grid()

                self.VarTexto = tk.StringVar()
                self.EntradaID = ttk.Entry(self.frame, textvariable = self.VarTexto)
                self.EntradaID.pack(pady = ESPACIO_Y)
                self.VarTexto.set(text)
                self.EntradaID.bind('<Button-1>', lambda e: self.borrar_texto(e, text))
                self.EntradaID.bind('<FocusOut>', lambda e: self.restaurar_texto(e, text))

        def borrar_texto(self, e, text):
                if self.VarTexto.get() == text:
                        self.VarTexto.set('')

        def restaurar_texto(self, e, text):
                if self.VarTexto.get() == '':
                        self.VarTexto.set(text)


if __name__ == "__main__":
        app = App()

        app.mainloop()