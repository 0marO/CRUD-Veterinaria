
from asyncio.windows_events import NULL
from contextlib import nullcontext
from re import A
import tkinter as tk
from tkinter import *
from tkinter import ttk

from constantes import *
from backend.backend import *
from comprobaciones_de_entradas import *

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
                fila = 0
                EntryNombre = EntryCustom(self.card, text='Nombre')
                EntryNombre.grid(row= fila, column= 0,sticky= W)
                fila += 1

                EntryApellido = EntryCustom(self.card, text='Apellido')
                EntryApellido.grid(row= fila, column= 0,sticky= W)
                fila += 1

                EntryEmail = EntryCustom(self.card, text='Email')
                EntryEmail.grid(row= fila, column= 0,sticky= W)
                fila += 1

                EntryDNI = EntryCustom(self.card, text='DNI')
                EntryDNI.grid(row= fila, column= 0,sticky= W)
                fila += 1

                EntryDirección = EntryCustom(self.card, text='Dirección')
                EntryDirección.grid(row= fila, column= 0,sticky= W)
                fila += 1

                EntryTelefono = EntryCustom(self.card, text='Teléfono')
                EntryTelefono.grid(row= fila, column= 0,sticky= W)
                fila += 1

                self.IngresarMascota = ttk.Button(self.card,
                                                text='Confirmar Datos',  
                                                style='Accent.TButton',
                                                command= lambda: self.FuncionMagicaDeBackend(EntryNombre.Entrada.get(),
                                                                                             EntryApellido.Entrada.get(),
                                                                                             EntryEmail.Entrada.get(),
                                                                                             EntryDNI.Entrada.get(),
                                                                                             EntryDirección.Entrada.get(),
                                                                                             EntryTelefono.Entrada.get()
                                                                                             )
                                                )
                self.IngresarMascota.grid(row= fila, column= 0,sticky= W)
                fila += 1


                self.Cruz = PhotoImage(file= CWD +'imagenes\\cruz_chica.png')
                self.LabelCruz = Label(self.card, image = self.Cruz)


        def FuncionMagicaDeBackend(self, nombre, apellido, email, dni, direccion, telefono):

                if ComprobarEntradaNombre(nombre) == False:
                        print('Error. El nombre ingresado es inválido.')
                        self.LabelCruz.forget()
                        self.LabelCruz.grid(row= 0, column= 1)
                        return
                if ComprobarEntradaNombre(apellido) == False:
                        print('Error. El apellido ingresado es inválido.')
                        self.LabelCruz.forget()
                        self.LabelCruz.grid(row= 1, column= 1)
                        return
                if ComprobarEntradaEmail(email) == False:
                        print('Error. El email ingresado es inválido.')
                        self.LabelCruz.forget()
                        self.LabelCruz.grid(row= 2, column= 1)
                        return
                if ComprobarEntradaDni(dni) == False:
                        print('Error. El DNI ingresado es inválido.')
                        self.LabelCruz.forget()
                        self.LabelCruz.grid(row= 3, column= 1)
                        return
                if ComprobarEntradaTelefono(telefono) == False:
                        print('Error. El Telefono ingresado es inválido.')
                        self.LabelCruz.forget()
                        self.LabelCruz.grid(row= 5, column= 1)
                        return

                self.LabelCruz.forget()
                IngresarDueñoDB(nombre, apellido, email, dni, direccion, telefono)

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
                EntryNombre.grid(row= 0, column= 0,sticky= W)

                ComboBoxTipoAnimal = ttk.Combobox(self.card, values = ["Canino",'Felino','Equino',
                                                                       'Rumiante','Roedor','Ave',
                                                                       'Reptil', 'Otro'
                                                                       ])
                ComboBoxTipoAnimal.grid(row= 1, column= 0)

                EntryRaza = EntryCustom(self.card, text='Raza')
                EntryRaza.grid(row= 2, column= 0,sticky= W)

                EntryEdad = EntryCustom(self.card, text='Edad')
                EntryEdad.grid(row= 3, column= 0,sticky= W)

                EntryDniDueño = EntryCustom(self.card, text='DNI Dueño')
                EntryDniDueño.grid(row= 4, column= 0,sticky= W)

                EntryDniDueño2 = EntryCustom(self.card, text='DNI segundo Dueño')
                EntryDniDueño2.grid(row= 5, column= 0,sticky= W)
                

                self.IngresarMascota = ttk.Button(self.card,
                                                text='Confirmar Datos',  
                                                style='Accent.TButton',
                                                command= lambda: self.FuncionMagicaDeBackend(EntryNombre.Entrada.get(),
                                                                                             ComboBoxTipoAnimal.get(),
                                                                                             EntryRaza.Entrada.get(),
                                                                                             EntryEdad.Entrada.get(),
                                                                                             EntryDniDueño.Entrada.get(),
                                                                                             EntryDniDueño2.Entrada.get(),
                                                                                             )
                                                )
                self.IngresarMascota.grid(row= 6, column= 0, pady= 5,sticky= W)

                
                self.Cruz = PhotoImage(file= CWD +'imagenes\\cruz_chica.png')
                self.LabelCruz = Label(self.card, image = self.Cruz)

        def FuncionMagicaDeBackend(self, nombre, tipo, raza, edad, dni_dueño, dni_dueño2):
                #esta función será remplazada por otra del backend.
                #En el caso feliz se encargará de ingresar un nuevo paciente a la base de datos
                if ComprobarEntradaNombre(nombre) == False:
                        print('Error. El nombre ingresado es inválido.')
                        self.LabelCruz.forget()
                        self.LabelCruz.grid(row= 0, column= 1)
                        return
                if ComprobarEntradaNombre(raza) == False:
                        print('Error. El nombre ingresado es inválido.')
                        self.LabelCruz.forget()
                        self.LabelCruz.grid(row= 2, column= 1)
                        return
                if ComprobarEntradaEdad(edad) == False:
                        print('Error. Edad acepta solo numeros.')
                        self.LabelCruz.forget()
                        self.LabelCruz.grid(row= 3, column= 1)
                        return
                if ComprobarEntradaDni(dni_dueño) == False:
                        print('Error. El DNI ingresado es inválido.')
                        self.LabelCruz.forget()
                        self.LabelCruz.grid(row= 4, column= 1)
                        return
                if ComprobarEntradaDni(dni_dueño2) == False and (dni_dueño2 != '' and dni_dueño2 != 'DNI segundo Dueño'):
                        print('Error. El DNI ingresado es inválido.')
                        self.LabelCruz.forget()
                        self.LabelCruz.grid(row= 5, column= 1)
                        return

                self.LabelCruz.forget()
                if dni_dueño2 == '' or dni_dueño2 == 'DNI segundo Dueño':
                        IngresarMascotaDB(nombre, tipo, raza, edad, dni_dueño)
                else:
                        IngresarMascotaDB(nombre, tipo, raza, edad, dni_dueño, dni_dueño2)


class BuscarRegistro(tk.Toplevel):
        def __init__(self):
                super().__init__()
                # configuración de la ventana 
                self.title('Logi Vet Búsqueda de registros.')
                self.geometry('1130x500')

                # MARCO BUSQUEDA
                self.CartaBusqueda = ttk.Frame(self, style='Card', padding=(5, 6, 10, 9))
                self.CartaBusqueda.place(x = ESPACIO_X*2, y = ESPACIO_Y*2)

                # SELECCION DE BUSQUEDA
                self.LabelBuscar = Label(self.CartaBusqueda, text= "Buscar por ")
                self.LabelBuscar.grid(row= 0, column= 0)
                

                self.ComboBuscarPor = ttk.Combobox(self.CartaBusqueda, values = ["ID Mascota",'Nombre Dueño',
                                                                       'DNI dueño','Nombre Paciente',],
                                               state="readonly")
                self.ComboBuscarPor.current(0)
                self.ComboBuscarPor.grid(row= 0, column= 1)
                
                self.EntryBuscar = EntryCustom(self.CartaBusqueda, text='')
                self.EntryBuscar.grid(row= 0, column= 2, padx= 10)

                self.ListaRegistrosBuscados = []
                self.BtBuscar = Button(self.CartaBusqueda, text ='--->',
                                        command= lambda: self.buscar_magicamente(self.ListaRegistrosBuscados),
                                        borderwidth = 0)
                self.BtBuscar.grid(row = 0, column = 3, padx= 10)
                
                # MARCO DATOS
                self.card = ttk.Frame(self, style='Card', padding=(5, 6, 100, 9))
                self.card.place(x = ESPACIO_X*2, y = ESPACIO_Y+MARCO_DE_BUSQUEDA_Y)

                #ENTRY
                fila = 0
                self.EntryNombre = EntryCustom(self.card, text='Nombre')
                self.EntryNombre.grid(row= fila, column= 0)
                fila +=1

                self.EntryID = EntryCustom(self.card, text='ID mascota')
                self.EntryID.grid(row= fila, column= 0)
                fila +=1

                self.EntryRaza = EntryCustom(self.card, text='Raza')
                self.EntryRaza.grid(row= fila, column= 0)
                fila +=1

                self.EntryEdad = EntryCustom(self.card, text='Edad')
                self.EntryEdad.grid(row= fila, column= 0)
                fila +=1

                self.EntryNombreDueño = EntryCustom(self.card, text='Nombre Dueño')
                self.EntryNombreDueño.grid(row= fila, column= 0)
                fila +=1

                self.EntryDniDueño = EntryCustom(self.card, text='DNI Dueño')
                self.EntryDniDueño.grid(row= fila, column= 0)
               
                self.EntryEmailDueño = EntryCustom(self.card, text='dueño@ejemplo.com')
                self.EntryEmailDueño.grid(row= fila, column= 1, padx= 10)

                self.EntryTelefono = EntryCustom(self.card, text='Telefono')
                self.EntryTelefono.grid(row= fila, column= 2)
                fila +=1

                self.EntryNombreDueño2 = EntryCustom(self.card, text='Nombre Dueño 2')
                self.EntryNombreDueño2.grid(row= fila, column= 0)
                fila +=1

                self.EntryDniDueño2 = EntryCustom(self.card, text='DNI segundo Dueño')
                self.EntryDniDueño2.grid(row= fila, column= 0)

                self.EntryEmailDueño2 = EntryCustom(self.card, text='dueño2@ejemplo.com')
                self.EntryEmailDueño2.grid(row= fila, column= 1, padx= 10)

                self.EntryTelefono2 = EntryCustom(self.card, text='Telefono dueño 2')
                self.EntryTelefono2.grid(row= fila, column= 2)
                fila +=1

                self.ListaEntry = [self.EntryNombre,self.EntryID,self.EntryRaza,self.EntryEdad,
                                   self.EntryNombreDueño,self.EntryDniDueño,self.EntryEmailDueño,self.EntryTelefono,
                                   self.EntryNombreDueño2,self.EntryDniDueño2, self.EntryEmailDueño2,self.EntryTelefono2]


                self.LabelFoto = Label(self.card, text="ACA VA LA FOTO", 
                                        height= 7, width= 15, bg='green')
                self.LabelFoto.place(x = 200, y = 20)

                

                # MARCO TREE VIEW
                self.CartaTreeView = ttk.Frame(self, padding=(5, 6, 10, 9))
                self.CartaTreeView.place(x = ANCHO_MARCO_DATOS, y = ESPACIO_Y + OCD)
                # Scrollbar TREE
                treeScroll = ttk.Scrollbar(self.CartaTreeView)
                treeScroll.pack(side="right", fill="y")
                # Treeview
                self.treeview = ttk.Treeview(self.CartaTreeView, selectmode="extended",
                                             yscrollcommand=treeScroll.set,
                                             columns=(1,2,3),
                                             height=17)
                self.treeview.pack(expand=True, fill="both")
                treeScroll.config(command=self.treeview.yview)

                # Treeview columns
                self.treeview.column("#0", width= 100)
                self.treeview.column(1, anchor="w", width=120)
                self.treeview.column(2, anchor="w", width=120)
                self.treeview.column(3, anchor="w", width=120)

                # Treeview headings
                self.treeview.heading("#0", text="Id Paciente", anchor="w")
                self.treeview.heading(1, text="Paciente", anchor="w")
                self.treeview.heading(2, text="Dueño", anchor="w")
                self.treeview.heading(3, text="Dni Dueño", anchor="w")

                self.treeview.bind("<<TreeviewSelect>>", lambda e: self.CargarDatosEnEntry(e))

                #BOTONES  MODIFICAR, HC Y ELIMINAR PACIENTE
                self.BtMod = Button(self, text='Modificar Datos', bg='yellow',
                                    command= lambda: self.EstadoNormalEntry())

                self.BtMod.place(x= ESPACIO_X*2, y= MARCO_DE_DATOS_Y)

                self.BtHc = Button(self, text='Historia Clínica', bg='dark turquoise')
                self.BtHc.place(x= ESPACIO_X*2+BOTON_MOD_X, y= MARCO_DE_DATOS_Y)

                self.BtEl = Button(self, text='Eliminar Paciente', bg='tomato')
                self.BtEl.place(x= ESPACIO_X*2+BOTON_MOD_X*4, y= MARCO_DE_DATOS_Y)


                # Configuracion estandar inicial de los campos de datos
                self.SoloLeerEntry()
        
        def CargarDatosEnEntry(self,e):

                self.EstadoNormalEntry()
                selected_id = self.treeview.selection()
                datos = self.ListaRegistrosBuscados[self.treeview.index(selected_id)]

                IndiceRegistro = 0
                for widget  in self.ListaEntry:
                        widget.Entrada.delete(0, tk.END)
                        widget.Entrada.insert(0, f"{datos[IndiceRegistro]}")
                        IndiceRegistro +=1
                self.SoloLeerEntry()


        def buscar_magicamente(self,ListaRegistrosBuscados):

                devolucion = NULL
                if self.ComboBuscarPor.current() == 0:
                        devolucion = BuscarRegistroPorIdMascota(self.EntryBuscar.Entrada.get())
                elif self.ComboBuscarPor.current() == 1:
                        devolucion = BuscarRegistroPorNombreDueño(self.EntryBuscar.Entrada.get())
                elif self.ComboBuscarPor.current() == 2:
                        devolucion = BuscarRegistroPorDniDueño(self.EntryBuscar.Entrada.get())
                elif self.ComboBuscarPor.current() == 3:
                        devolucion = BuscarRegistroPorNombrePaciente(self.EntryBuscar.Entrada.get())
        
                ListaRegistrosBuscados.clear()
                for i in self.treeview.get_children():
                        self.treeview.delete(i)

                for reg in devolucion:
                        self.treeview.insert(   "",
                                                tk.END,
                                                text= f"{reg[POS_ID_MASCOTA]}",
                                                values=(f"{reg[POS_NOMBRE_MASCOTA]}",
                                                        f"{reg[POS_NOMBRE_DUEÑO]}", f"{reg[POS_DNI_DUEÑO]}")
                                                )
                        ListaRegistrosBuscados.append(reg)

                print(ListaRegistrosBuscados)
                self.treeview.update()



        def SoloLeerEntry(self):
                for entry in self.ListaEntry:
                        entry.Entrada.config(state = 'readonly')
                self.BtMod.config(command= lambda: self.EstadoNormalEntry(), text='Modificar Datos')

        def EstadoNormalEntry(self):
                for entry in self.ListaEntry:
                        entry.Entrada.config(state = 'normal')
                self.BtMod.config(command= lambda: self.SoloLeerEntry(), text='Terminar Mods')


class EntryCustom(ttk.Frame):
        def __init__(self, parent, text="", *args, **options):
                tk.Frame.__init__(self, parent, *args, **options)

                self.frame = Frame(self,borderwidth=0)
                self.frame.grid()

                self.VarTexto = tk.StringVar()
                self.Entrada = ttk.Entry(self.frame, textvariable = self.VarTexto)
                self.Entrada.pack(pady = ESPACIO_Y)
                self.VarTexto.set(text)
                self.Entrada.bind('<Button-1>', lambda e: self.borrar_texto(e, text))
                self.Entrada.bind('<FocusOut>', lambda e: self.restaurar_texto(e, text))

        def borrar_texto(self, e, text):
                if self.VarTexto.get() == text:
                        self.VarTexto.set('')

        def restaurar_texto(self, e, text):
                if self.VarTexto.get() == '':
                        self.VarTexto.set(text)


if __name__ == "__main__":
        app = App()
        app.mainloop()