#!/usr/local/bin/python
import requests
import json

#Metodo para solicitar el progreso de las descargas 
def getTaskProgress():
	#r = requests.post("http://127.0.0.1:9091", json={"action":"Update State", "ram":""})
	#rjsonload = json.loads(r.text)
	return "tasks"

#Metodo para enviar reporte de descargas
def doRequest():
	r = requests.put("http://127.0.0.1:5005/tasks_progress", json={"action":"Update Tasks", "task1":"", "task2":""})
	rjsonload = json.loads(r.text)
	if(rjsonload['task'] == "updated"):
		return "Estado actualizado correctamente"
	else:
		return "No se acturlizo el estado"

print doRequest()