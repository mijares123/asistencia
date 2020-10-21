from unittest import TestCase
from trabajador import Trabajador
class TrabajadorTest(TestCase):
    def test_crear_trabajador(self):
        trabajador=Trabajador('mijares','75975766','cajero')
        self.assertEqual('mijares',trabajador.nombre)
        self.assertEqual('75975766',trabajador.dni)
        self.assertEqual('cajero',trabajador.trabajo)
        