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
                self.label.pack(pady = ESPACIO_Y)

                # BOTONES
                self.BuscarRegistro = ttk.Button(self.card,
                                                text='Buscar registro...', 
                                                style='Accent.TButton')
                self.BuscarRegistro.pack(pady = ESPACIO_Y, anchor= W)

                self.IngresarDueño = ttk.Button(self.card,
                                                text='Ingresar dueño...',
                                                style='Accent.TButton')
                self.IngresarDueño.pack(pady = ESPACIO_Y, anchor= W)

                self.IngresarMascota = ttk.Button(self.card,
                                                text='Ingresar mascota...',  
                                                style='Accent.TButton')
                self.IngresarMascota.pack(pady = ESPACIO_Y, anchor= W)


                self.label2 = ttk.Label(self.card, text='Busqueda con ID único de paciente')
                self.label2.pack(pady = ESPACIO_Y)

                self.VarTexto = tk.StringVar()
                self.EntradaID = ttk.Entry(self.card, textvariable = self.VarTexto)
                self.EntradaID.pack(pady = ESPACIO_Y)
                self.VarTexto.set("ID de mascota...")
                self.EntradaID.bind('<Button-1>', lambda e: self.borrar_texto(e))
                self.EntradaID.bind('<FocusOut>', lambda e: self.restaurar_texto(e))

        def borrar_texto(self, e):
                        self.VarTexto.set('')
        def restaurar_texto(self, e):
                        self.VarTexto.set("ID de mascota...")




if __name__ == "__main__":
        app = App()
        app.mainloop()