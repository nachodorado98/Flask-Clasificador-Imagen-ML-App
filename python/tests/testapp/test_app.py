import os

def test_pagina_inicial_get(cliente):

	respuesta=cliente.get("/")

	contenido=respuesta.data.decode()

	respuesta.status_code==200
	assert "Clasificador" in contenido

def test_pagina_inicial_post(cliente):

	ruta_imagen=os.path.join(os.getcwd(), "testapp", "imagen_tests.jpg")

	data={"imagen":open(ruta_imagen, "rb")}

	respuesta=cliente.post("/", data=data, buffered=True, content_type="multipart/form-data")

	contenido=respuesta.data.decode()

	respuesta.status_code==200
	assert "La imagen es un" in contenido
