from tkinter import *
from tkinter import ttk

# Function to open a new window
# for add device
def addDevice(master):
	# Toplevel object which will
	# be treated as a new window
	newWindow = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	newWindow.title("Agregar Dispositivo")

	# sets the geometry of toplevel
	newWindow.geometry("600x200")

	# A Label widget to show in toplevel
	Label(newWindow,
		text ="Agregar Dispositivo").pack()

# Function to open a new window
# for delete device 
def deleteDevice(master):
	# Toplevel object which will
	# be treated as a new window
	newWindow = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	newWindow.title("Eliminar Dispositivo")

	# sets the geometry of toplevel
	newWindow.geometry("200x200")

	# A Label widget to show in toplevel
	Label(newWindow,
		text ="Eliminar Dispositivo").pack()

# Function to open a new window
# for delete device 
def editDevice(master):
	# Toplevel object which will
	# be treated as a new window
	newWindow = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	newWindow.title("Editar Dispositivo")

	# sets the geometry of toplevel
	newWindow.geometry("200x200")

	# A Label widget to show in toplevel
	Label(newWindow,
		text ="Editar Dispositivo").pack()

# Function to open a new window
def generateReport(master):
	
	# Toplevel object which will
	# be treated as a new window
	newWindow = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	newWindow.title("New Window")

	# sets the geometry of toplevel
	newWindow.geometry("200x200")

	# A Label widget to show in toplevel
	Label(newWindow,
		text ="This is a new window").pack()
    
