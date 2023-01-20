from tkinter import *
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
	currentWin.resizable(False, False)
	# sets the geometry of toplevel
	currentWin.geometry("450x250")

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

	Button(currentWin, height = 1, width = 25, text ="Agregar Dispositivos", pady = 10,
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
	currentWin.resizable(False, False)
	# sets the geometry of toplevel
	currentWin.geometry("450x150")

	# A Label widget to show in toplevel
	Label(currentWin,
		text ="Eliminar Dispositivo", font = ("Comic Sans MS", 17)).pack()
	
	Label(currentWin,
		text ="Seleccione el dispositivo:", font = ("Comic Sans MS", 10)).pack()
	comunidad = Text(currentWin, height= 1, width= 50)
	comunidad.pack()

	Button(currentWin, height = 1, width = 25, text ="Eliminar Dispositivo", pady = 10,
		command = lambda: 
		fn.add_device(currentWin,comunidad,host,oid)).pack()

# Function to open a new window
# for delete DeviceGUI 
def edit_deviceGUI(master):
	# Toplevel object which will
	# be treated as a new window
	currentWin = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	currentWin.title("Editar Dispositivo")
	currentWin.resizable(False, False)
	# sets the geometry of toplevel
	currentWin.geometry("450x250")

	# A Label widget to show in toplevel
	Label(currentWin,
		text ="Editar Dispositivo", font = ("Comic Sans MS", 17)).pack()
	
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

	Button(currentWin, height = 1, width = 25, text ="Editar Dispositivo", pady = 10,
		command = lambda: 
		fn.add_device(currentWin,comunidad,host,oid)).pack()

# Function to open a new window
def generateReportGUI(master):
	# Toplevel object which will
	# be treated as a new window
	currentWin = Toplevel(master)

	# sets the title of the
	# Toplevel widget
	currentWin.title("Generar Reporte")
	currentWin.resizable(False, False)
	# sets the geometry of toplevel
	currentWin.geometry("450x150")

	# A Label widget to show in toplevel
	Label(currentWin,
		text ="Reporte", font = ("Comic Sans MS", 17)).pack()
	
	Label(currentWin,
		text ="Seleccione el dispositivo:", font = ("Comic Sans MS", 10)).pack()
	comunidad = Text(currentWin, height= 1, width= 50)
	comunidad.pack()

	Button(currentWin, height = 1, width = 25, text ="Generar Dispositivo", pady = 10,
		command = lambda: 
		fn.add_device(currentWin,comunidad,host,oid)).pack()
