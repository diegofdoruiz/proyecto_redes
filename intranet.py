#!/usr/local/bin/python
import psutil
import requests
import json

def useRam():
   memory_use = float(psutil.virtual_memory()[3]) / float(psutil.virtual_memory()[0]) * 100
   return memory_use

def loadCpu():
   load_cpu = float(psutil.virtual_memory()[3]) / float(psutil.virtual_memory()[0]) * 100
   return load_cpu

def useDisk():
	use_disk = float(psutil.disk_usage('/')[1]) / float(psutil.disk_usage('/')[0]) * 100
	return use_disk

ram = 22

def doRequest():
	r = requests.put("http://127.0.0.1:5005/set_state", json={"action":"Update State", "ram":ram})
	rjsonload = json.loads(r.text)
	if(rjsonload['task'] == "updated"):
		return "Estado actualizado correctamente", rjsonload['ram']
	else:
		return "No se acturlizo el estado"

print doRequest()