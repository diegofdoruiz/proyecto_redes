#!/usr/local/bin/python
import requests
import json
import commands


#Metodo para pedir solicitudes de descarga y posterior ejecución de la tarea en transmission
def doRequest():
	r = requests.get("http://127.0.0.1:5005/request_progress")
	rjsonload = json.loads(r.text)
	task1 rjsonload['task1']
	task2 rjsonload['task1']
	return True

#Metodo encargado de iniciar las descagas en transmision
def setTaskTransmission():

	return True

print doRequest()