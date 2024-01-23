from sqlite3.dbapi2 import Cursor 
from .conexion import ConexionDB
from tkinter import messagebox


def listarHistoria(idPersona):
    conexion = ConexionDB()
    listaHistoria = []
    sql = f'SELECT h.idHistoriaMedica, p.apellidoPaterno || " " || p.apellidoMaterno AS Apellidos, h.fechaHistoria, h.motivo, h.examenAuxiliar, h.tratamiento, h.detalle FROM historiaMedica h INNER JOIN Persona p ON p.idPersona = h.idPersona WHERE p.idPersona = {idPersona}'

    try:
        conexion.cursor.execute(sql)
        listaHistoria = conexion.cursor.fetchall()
        conexion.cerrarConexion()

    except:
        title = 'LISTAR HISTORIA'
        mensaje = 'Error al listar historial medica'
        messagebox.showerror(title, mensaje)
    return listaHistoria

def guardarHistoria(idPersona, fechaHistoria, motivo, examenAuxiliar, tratamiento, detalle):
    conexion = ConexionDB()
    sql = f"""INSERT INTO historiaMedica (idPersona, fechaHistoria, motivo, examenAuxiliar, tratamiento, detalle) VALUES
            ({idPersona},'{fechaHistoria}','{motivo}','{examenAuxiliar}','{tratamiento}','{detalle}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registro Historial Medica'
        mensaje = 'Historia Registrada Exitosamente'
        messagebox.showinfo(title, mensaje)

    except:
        title = 'Registro Historial Medica'
        mensaje = 'Error al Registrar Historial'
        messagebox.showerror(title, mensaje)

def eliminarHistoria(idHistoriaMedica):
    conexion = ConexionDB()
    sql = f'DELETE FROM historiaMedica WHERE idHistoriaMedica = {idHistoriaMedica}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Eliminar Historial'
        mensaje = 'Historial Medica Eliminada Con Exito'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Eliminar Historial'
        mensaje = 'Error al Eliminar Historial'
        messagebox.showwarning(title, mensaje)

def editarHistoria(fechaHistoria, motivo, examenAuxiliar, tratamiento, detalle, idHistoriaMedica):
    conexion = ConexionDB()
    sql = f"""UPDATE historiaMedica SET fechaHistoria = '{fechaHistoria}', motivo = '{motivo}', examenAuxiliar = '{examenAuxiliar}', tratamiento = '{tratamiento}', detalle = '{detalle}' WHERE idHistoriaMedica = {idHistoriaMedica}"""
    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Historial'
        mensaje = 'Historial Medica Editada Con Exito'
        messagebox.showinfo(title, mensaje)
    except:
        title = 'Editar Historial'
        mensaje = 'Error Al Editar Historial Medica'
        messagebox.showerror(title, mensaje)


class historiaMedica:
    def __init__(self, idPersona, fechaHistoria, motivo, examenAuxiliar, tratamiento, detalle):
        self.idHistoriaMedica = None
        self.idPersona = idPersona
        self.fechaHistoria = fechaHistoria
        self.motivo = motivo
        self.examenAuxiliar = examenAuxiliar
        self.tratamiento = tratamiento
        self.detalle = detalle

    def __str__(self):
        return f'historiaMedica[{self.idPersona},{self.fechaHistoria},{self.motivo},{self.examenAuxiliar},{self.tratamiento},{self.detalle}]'