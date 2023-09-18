import os

from src.utilidades.utils import crearCarpeta

def borrarCarpeta(ruta):

	if os.path.exists(ruta):

		os.rmdir(ruta)


def test_carpeta_no_existe():

	ruta_carpeta=os.path.join(os.getcwd(), "Prueba")

	assert crearCarpeta(ruta_carpeta)

def test_carpeta_existe():

	ruta_carpeta=os.path.join(os.getcwd(), "Prueba")

	assert not crearCarpeta(ruta_carpeta)

	borrarCarpeta(ruta_carpeta)

