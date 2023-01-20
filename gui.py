from tkinter import *
from tkinter import ttk
import actions as fn

# Function to open a new window
# for add DeviceGUI
def add_deviceGUI(master):
	# Toplevel object which will
	# be treated as a new window
	currentWin = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	currentWin.title("Agregar Dispositivo")

	# sets the geometry of toplevel
	currentWin.geometry("450x300")

	# A Label widget to show in toplevel
	Label(currentWin,
		text ="Agregar Dispositivo", font = ("Comic Sans MS", 17)).pack()
	
	Label(currentWin,
		text ="Comunidad:", font = ("Comic Sans MS", 10)).pack()
	comunidad = Text(currentWin, height= 1, width= 50)
	comunidad.pack()
	Label(currentWin,
		text ="Host:", font = ("Comic Sans MS", 10)).pack()
	host = Text(currentWin, height= 1, width= 50)
	host.pack()
	Label(currentWin,
		text ="OID:", font = ("Comic Sans MS", 10)).pack()
	oid = Text(currentWin, height= 1, width= 50)
	oid.pack()

	Button(currentWin, height = 2, width = 25, text ="Show",
		command = lambda: 
		fn.add_device(currentWin,comunidad,host,oid)).pack()


# Function to open a new window
# for delete DeviceGUI 
def delete_deviceGUI(master):
	# Toplevel object which will
	# be treated as a new window
	currentWin = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	currentWin.title("Eliminar Dispositivo")

	# sets the geometry of toplevel
	currentWin.geometry("200x200")

	# A Label widget to show in toplevel
	Label(currentWin,
		text ="Eliminar Dispositivo").pack()

# Function to open a new window
# for delete DeviceGUI 
def edit_deviceGUI(master):
	# Toplevel object which will
	# be treated as a new window
	currentWin = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	currentWin.title("Editar Dispositivo")

	# sets the geometry of toplevel
	currentWin.geometry("200x200")

	# A Label widget to show in toplevel
	Label(currentWin,
		text ="Editar Dispositivo").pack()

# Function to open a new window
def generateReportGUI(master):
	
	# Toplevel object which will
	# be treated as a new window
	currentWin = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	currentWin.title("New Window")

	# sets the geometry of toplevel
	currentWin.geometry("200x200")

	# A Label widget to show in toplevel
	Label(currentWin,
		text ="This is a new window").pack()
