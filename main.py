from fastapi import FastAPI #Importar FastAPI para crear la aplicación web
import uvicorn #Importar uvicorn para ejecutar la aplicación FastAPI
from pydantic import BaseModel #Importar BaseModel para crear el modelo de usuario
from typing import Optional #Importar Optional para campos opcionales en el modelo de usuario
from datetime import datetime #Importar datetime para manejar la fecha de creación del usuario

#User model
class User(BaseModel): #Schema
    id:int
    nombre:str
    apellido:str
    direccion:Optional[str]
    telefono:int
    creacion_user:datetime = datetime.now()

class userId(BaseModel): #class de prueba para obtener un usuario por su ID usando POST
    id:int


app = FastAPI()
usuarios = [] #Base de datos simulada

@app.get('/ruta1') #Ruta de prueba
def ruta1(): #Funcion de prueba
    return {"mensaje": "Bienvenido a tu primera api :)"}


@app.get('/user') #Ruta para obtener todos los usuarios
def obtener_usuarios():
    return usuarios #Devolver la lista de usuarios

@app.post('/crear_usuario') #Ruta para crear un usuario
def crear_usuario(user: User):
    usuario = user.dict() #Convertir el objeto User a un diccionario
    usuarios.append(usuario) #Agregar el usuario a la base de datos simulada
    return ({"mensaje": "Usuario creado exitosamente", "usuario": usuario})

@app.get('/user/{user_id}') #Ruta para obtener un usuario por su ID
def obtener_usuario(user_id: int):
    for user in usuarios:
        if user['id'] == user_id: #Buscar el usuario por su ID
            return user #Devolver el usuario encontrado
    return {"mensaje": "Usuario no encontrado"} #Devolver un mensaje si el usuario no se encuentra

@app.post('/user') #si tiene body, se debe usar POST
def obtener_usuario_por_id(user_id: userId): #Ruta para obtener un usuario por su ID usando POST, se recibe un objeto userId con el ID del usuario a buscar
    for user in usuarios:
        if user['id'] == user_id.id: #Buscar el usuario por su ID
            print(user)
            return user #Devolver el usuario encontrado
    return {"mensaje": "Usuario no encontrado"} #Devolver un mensaje si el usuario no se encuentra

@app.delete('/user/{user_id}') #Ruta para eliminar un usuario por su ID
def eliminar_usuario(user_id: int):
    for user in usuarios:
        if user['id'] == user_id: #Buscar el usuario por su ID
            usuarios.remove(user) #Eliminar el usuario encontrado #remove o pop
            return {"mensaje": "Usuario eliminado exitosamente"} #Devolver un mensaje de éxito
    return {"mensaje": "Usuario no encontrado"} #Devolver un mensaje si el usuario no se encuentra

@app.put('/user/{user_id}') #Ruta para actualizar un usuario por su ID
def actualizar_usuario(user_id: int, user: User): #Se pone el id y el modelo o class que se va a actualizar
    for i, u in enumerate(usuarios): #Enumerate para obtener el índice y el usuario en la iteración
        if u['id'] == user_id: #Buscar el usuario por su ID
            usuarios[i] = user.dict() #Actualizar el usuario encontrado con los nuevos datos
            return {"mensaje": "Usuario actualizado exitosamente", "usuario": usuarios[i]} #Devolver un mensaje de éxito y el usuario actualizado
    return {"mensaje": "Usuario no encontrado"} #Devolver un mensaje si el usuario no se encuentra

if __name__ == "__main__": #Ejecutar la aplicación FastAPI con uvicorn
    uvicorn.run("main:app", port=8000, reload=True) #Ejecutar la aplicación FastAPI con uvicorn, especificando el módulo y la aplicación, el puerto y la opción de recarga automática

