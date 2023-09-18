import os

# Funcion para crear una carpeta si no existe 
def crearCarpeta(ruta:str)->bool:

	if not os.path.exists(ruta):

		os.mkdir(ruta)
		return True

	return False