from trabajador import Trabajador
class Asistencia:
    def __init__(self,trabajador):
        self.trabajador=trabajador
    
    def registrar_asistencia(self,tipo,hora):
        return {
            'nombre':self.trabajador.nombre,
            'dni':self.trabajador.dni,
            'trabajo':self.trabajador.trabajo,
            'tipo':tipo,
            'tiempo':hora
        }
        
    def descontar_descanso(self,tiempo):
        return tiempo - 1
    def obtener_horas(self,inicio,fin):
        return fin - inicio