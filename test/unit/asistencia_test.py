from unittest import TestCase
from asistencia import Asistencia
from trabajador import Trabajador
class AsistenciaTest(TestCase):
    def test_registrar_asistencia(self):
        asis = Asistencia(Trabajador("mijares","75975766","cajero"))
        self.assertDictEqual(
            {'nombre':'mijares',
             'dni':'75975766',
             'trabajo':'cajero',
             'tipo':'entrada',
             'tiempo':8
             },
             asis.registrar_asistencia('entrada',8)
        )

    def test_descontar_descanso(self):
        asis = Asistencia(Trabajador("mijares","75975766","cajero"))
        self.assertEqual(9,asis.descontar_descanso(10))
    def test_obtener_horas(self):
        asis = Asistencia(Trabajador("mijares","75975766","cajero"))
        self.assertEqual(7,asis.obtener_horas(8,15))