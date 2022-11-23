import mysql.connector
import random
from datetime import date


conexion = mysql.connector.connect(user='root', password='Dragonball2004*', host='localhost',
                                   database='mydb', port='3306')

print(conexion)


def buscarUsuario(usuario, clave):
    cur = conexion.cursor()
    contra = f'''select contraseña from mydb.usuarios where nombre_de_usuario = '{usuario}'; '''
    cur.execute(contra)
    contrasena = cur.fetchall()
    print(contrasena)
    return clave == contrasena[0][0]



def contarUsuarios():
    cur = conexion.cursor()
    sql = 'select count(1) from usuarios;'
    cur.execute(sql)
    cantidad = cur.fetchall()
    return cantidad


def crearUsuario(nombreCompleto, correo, usuario, clave, fechaNto):
    cur = conexion.cursor()
    cantidad = contarUsuarios()
    print(cantidad)
    membresia = ['Duo', 'Familiar', 'Individual', 'Premium Para Estudiantes']
    sql = f'''insert into mydb.usuarios(nombre_completo,nombre_de_usuario,tipo_membresia,correo,fecha_registro,contraseña,fecha_nacimiento,id_membresia) values('{nombreCompleto}', '{usuario}' , '{membresia[random.randint(0, len(membresia) - 1)]}' ,'{correo}' ,'{date.today().strftime('%Y-%m-%d')}' ,'{clave}' ,'2022-11-23', {random.randint(0, 10000)})'''
    print(sql)
    cur.execute(sql)


def buscarArtista(nombreArtista):
    cur = conexion.cursor()
    sql = f'''select nombre, media_oyentesXmes from artistas a where nombre = '{nombreArtista}';'''
    cur.execute(sql)
    resultado = cur.fetchall()
    return resultado


def buscarCancion(nombreCancion):
    cur = conexion.cursor()
    sql = f'''select c.nombre, a.nombre, m.nombre, c.fecha_publicacion, c.duracion from mydb.canciones c, mydb.artistas a, mydb.albumes m where c.nombre = '{nombreCancion}' and a.idArtistas = c.id_artista_principal'''
    cur.execute(sql)
    resultado = cur.fetchall()
    return resultado
