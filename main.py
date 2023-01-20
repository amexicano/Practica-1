from tkinter import *
import gui

if (__name__ == "__main__"):
	# Run the main program
	# creates a Tk() object
	master = Tk()
	master.resizable(False, False)
	# sets the geometry of main
	# root window
	master.title("Sistema de Administracion de Red")
	master.geometry("600x200")

	menubar = Menu(master)

	# create a pulldown menu, and add it to the menu bar
	filemenu = Menu(menubar, tearoff=0)
	menubar.add_cascade(label="Dispositivos", menu=filemenu)
	filemenu.add_command(label="Agregar Dispositivo", command= lambda: gui.add_deviceGUI(master))
	filemenu.add_command(label="Editar Dispositivo", command= lambda: gui.edit_deviceGUI(master))
	filemenu.add_command(label="Eliminar Dispositivo", command= lambda: gui.delete_deviceGUI(master))
	filemenu.add_separator()

	# create more pulldown menus
	filemenu.add_command(label="Generar reporte", command=lambda: gui.generateReportGUI(master))

	Label(master, 
        text= "Sistema de Administracion de Red", 
        font= ("Comic Sans MS", 17)
        ).pack(pady= 10)

	Label(master, 
        text= "Práctica 1 - Adquisición de Información", 
        font= ("Comic Sans MS", 10)
        ).pack(pady= 15)

	Label(master, 
        text= "Mexicano Ixtepan Alejandro   4CM16   2013090237", 
        font= ("Comic Sans MS", 10)
        ).pack(pady= 15)

	master.config(menu=menubar)
	# mainloop, runs infinitely
	master.mainloop()
	