#!/usr/local/bin/python
from flask import Flask, jsonify, abort, make_response, request

#instanciar un objeto.
app = Flask(__name__)

##################################################################
#########             Pagina principal               #############
##################################################################
#Indicar al servidor cual es la ruta a cceder
#index() funcion que regesa un string cuando se acceda a esta ruta
#Luego se debe configurar otro tipo de contenido front end
#visualizar desde el navegador en internet
@app.route("/")
#index() funcion que regesa un string cuando se acceda a esta ruta
#Luego se debe configurar otro tipo de contenido front end
#visualizar desde el navegador en internet
def index():  
    return "Bienvenido A esta web"


##################################################################
#########        Manejo del lado de internet         #############
##################################################################

#Siguiente ruta sera para procesar la solicitud estado de recursos
#en el host de intranet, en este caso se retornara el ultimo estado 
#de los tres recursos.
#Para onbtener los datos hay que consultal la base de datos en esta funcion
@app.route("/get_state", methods=['GET'])
def retornarEstados():
	return "ram, load, disk"

#Siguiente ruta sera para procesar la solicitud estado de recursos
#en el host de intranet, con el parametro nombre_recurso se especifica 
#un recurso en especifico para retornar su ultimo estado. Ej ram
#Para onbtener el dato hay que consultal la base de datos en esta funcion
@app.route("/get_state/<string:nombre_recurso>", methods=['GET'])
def retornarEstado(nombre_recurso):
	return nombre_recurso

#Respuesa en forma de json para manejar el error
@app.errorhandler(404)
def not_found(error):
 return make_response(jsonify({'error': 'Not found'}), 404)

#Metodo que crea un nuevo registro en una tabla de la base de datos con la nueva 
#tarea
#recibe un json como parametro con los datos suficientes para generar la tarea
@app.route("/set_task",  methods=['POST'])
def crearNuevaTarea():
 if not request.json or not 'action' in request.json:
  abort(400)
 response = "Creada correctamente"
  	#Procesar el json para crear el nuevo registro con la tarea en la base datos
 return jsonify({'response': response}), 201

#Inserta un registro de peticion de progreso de una descarga en la base de datos para que sea visible
#al host de intranet la proxima vez que consulte
#recibe un json como parametro con los datos suficientes para generar la tarea
#Este nuevo registro se crea cuando no se haya creado antes para una tarea en especifico,
#Si ya ha creado se verifica si el host de intranet ha respondido y se retorna el ultimo reporte
#de lo contrario se retorna un mensaje que indicando que se espera respuesta del host
@app.route("/task_progress",  methods=['POST'])
def progressTask():
 if not request.json or not 'action' in request.json:
  abort(400)
 #posible respuesta
 response = "Creada correctamente" or "ya esta creada, esperando respuesta" or "enviando ultimo reporte recibido"
 #Procesar el json para crear el nuevo registro con la tarea en la base datos
 return jsonify({'response': response}), 201


##################################################################
#########       Manejo del lado de la intranet       #############
##################################################################

#Metodo que recibe un json con los datos nuevos para actualizar los campos 
#de la tabla en la base de datos que contienen el estado de los recursos 
#del host de la intranet
@app.route("/set_state", methods=['PUT'])
def actualizarEstado():
 if not request.json or not 'action' in request.json:
  abort(400)
 return jsonify({'task': 'updated', "ram":request.json['ram']})

#Metodo para retornar las nuevas tareas pedidas desde internet y que previamente no hayan sido 
#retornadas
@app.route("/get_tasks", methods=['GET'])
def retornarNuevasTareas():
 response = {task1: {},
 			 task2: {},
 			 taskn: {}}
 return jsonify(response)

#Metodo para retornar las peticiones de progreso de una descarga programada previamnete
#retorna un json con la identificacion de la tarea a revisar 
@app.route("/get_tasks/request_progress", methods=['GET'])
def retornarSolicitudProgresos():
 response = {request1: '',
 			 request2: '',
 			 requestn: ''}
 return jsonify(response)

#Metodo que recibe un json con los datos nuevos para actualizar los campos 
#de la tabla en la base de datos que contienen el estado, progreso y timestamp
#de las descargas programadas.
@app.route("/tasks_progress", methods=['PUT'])
def actualizarProgresoDescargas():
 if not request.json or not 'action' in request.json:
  abort(400)
 jsonify({'task': 'updated'})

##################################################################
#########        Inicializacion del servidor         #############
##################################################################
#Ejecucion del servidor por default en el puerto 5000
#se puede cambiar el puerto con app.run( debug = True, port=5005 )
if __name__ == '__main__':
    app.run(debug=True, port=5005)