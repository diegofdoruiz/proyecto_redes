#!/usr/local/bin/python
import requests
import json
import commands


#Metodo para pedir solicitudes de progreso de una descarga y posteriormente ejecutar el 
#script que envia reportes de descargas
def doRequest():
	r = requests.get("http://127.0.0.1:5005/request_progress")
	rjsonload = json.loads(r.text)
	task1 rjsonload['task1']
	task2 rjsonload['task1']

	rout = commands.getoutput('/usr/bin/python task_progress.py')
	if(rout == "updated"):
		return "Estado actualizado correctamente"
	else:
		return "No se acturlizo el estado"

print doRequest()