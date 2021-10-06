import unittest
import sys
import io
from contextlib import contextmanager

from solucion_p1 import *


@contextmanager
def redirected():
    '''
    Context manager para capturar las salida de print (sys.stdout en general).
    Nos va a permitir capturar la salida por pantalla de las funciones del ejercicio.

    Sería mejor separar el código de mostrar_tareas en dos funciones: una que devuelve el
    texto, y otra que llama a la primera y lo muestra. Así no haría falta este tipo de
    programación avanzada.
    '''
    saved = sys.stdout
    out = io.StringIO()
    sys.stdout = out
    try:
        yield out
    finally:
        sys.stdout = saved


def red(fun, *args, **kwargs):
    with redirected() as out:
        fun(*args, **kwargs)
    return out.getvalue()


class TestUtilidades(unittest.TestCase):

    '''
    def test_cifrar(self):
        assert cifrar('hola mundo', 0) == 'HOLA MUNDO'
        assert cifrar('hola mundo', 20) == 'ÉDAU BJNXD'
        assert cifrar('adiós, mundo', 20) == 'UXÍSH, BJNXD'

    def test_descifrar(self):
        assert descifrar('UXÍSH, BJNXD', 20) ==  'ADIÓS, MUNDO'
        assert descifrar('ÉDAU BJNXD', 20) == 'HOLA MUNDO'
    '''

    def test_convertir(self):
        assert (euros_a_bitcoins(10000) - 0.22) < 0.1
        assert (bitcoins_a_euros(2) - 89140.34) < 1

    def test_contar(self):
        assert contar_vocales('esto son ocho vocales') == 8
        assert contar_vocales('  3 vocales ') == 3

    def test_palindromo(self):
        assert es_palindromo('ella te da detalle') == True
        assert es_palindromo('  Este texto no es un palindromo ') == False

    def test_temperaturas(self):
        assert max_temperaturas([12.0, 3.0, 4.0, 17.0, 26.0], 11) == [12.0, 17.0, 26.0]
        assert max_temperaturas([12.0, 3.0, 4.0, 17.0, 26.0], 32) == []

    def test_productos_vacios(self):
        lista_productos().clear()
        v = red(productos)
        assert 'No hay productos' in v
        assert len(lista_productos()) == 0

    def test_insertar(self):
        insertar('prueba')
        insertar('final')
        assert len(lista_productos()) == 2
        assert lista_productos()[0] == 'prueba'
        assert lista_productos()[1] == 'final'

    def test_borrar(self):
        lista_productos().clear()
        insertar('prueba')
        insertar('final')
        borrar(1)
        assert len(lista_productos()) == 1
        borrar(0)
        assert len(lista_productos()) == 0

    def test_mostrar_productos(self):
        lista_productos().clear()
        v = red(productos)
        assert 'No hay productos' in v
        assert ':' not in v
        insertar('prueba')
        v = red(productos)
        assert 'prueba' in v

if __name__ == '__main__':
    unittest.main(verbosity=0)
