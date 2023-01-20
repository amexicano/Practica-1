import json
def add_device(GUI, comunidad, host, oid):
    hola = {
        'comunidad': comunidad.get("1.0", "end-1c"), 
        'host': host.get("1.0", "end-1c"), 
        'oid':oid.get("1.0", "end-1c")
    }
    # Opening JSON file
    f = open('data.json','w')
  
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
  
    # Iterating through the json
    # list
    for i in data['emp_details']:
        print(i)
    print(hola)
    GUI.destroy()

def delete_device(GUI, index):
    GUI.destroy()

def editDevice(GUI):
    GUI.destroy() 

# def read_json():
#     with open("devices.json") as filedata:
#         datos = json.load(filedata)
#     return datos

# def append_json():
#     with open("devices.json", 'w') as archivo: 
#     return datos