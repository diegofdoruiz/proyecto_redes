#!/usr/local/bin/python
import psutil
import requests
import json

#Metodo para retornar el valor correspondiente al porcentaje de uso de la memoria ram
def useRam():
   memory_use = float(psutil.virtual_memory()[3]) / float(psutil.virtual_memory()[0]) * 100
   return memory_use

#Metodo para retornar el valor correspondiente al porcentaje de carga de la cpu
def loadCpu():
   load_cpu = float(psutil.virtual_memory()[3]) / float(psutil.virtual_memory()[0]) * 100
   return load_cpu

#Metodo para retornar el valor correspondiente al porcentaje de uso de disco duro
def useDisk():
	use_disk = float(psutil.disk_usage('/')[1]) / float(psutil.disk_usage('/')[0]) * 100
	return use_disk

ram = 22

#Metodo para hacer un request con el metodo PUT y enviar los datos correspondientes al
#estado actual de los recursos memoria ram, procesador y disco duro, la url sera la que 
#se consiga en heroku
#El servidor interpretara la ruta para set_state y por medio de la funcion actualizarEstado()
#procesara la solicitud
def doRequest():
	r = requests.put("http://127.0.0.1:5005/set_state", json={"action":"Update State", "ram":ram})
	rjsonload = json.loads(r.text)
	if(rjsonload['task'] == "updated"):
		return "Estado actualizado correctamente", rjsonload['ram']
	else:
		return "No se acturlizo el estado"

print doRequest()