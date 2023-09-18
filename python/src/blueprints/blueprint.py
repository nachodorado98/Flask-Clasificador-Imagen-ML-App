from flask import Blueprint, render_template, request
import os
from keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input, decode_predictions, VGG16

from src.utilidades.utils import crearCarpeta

bp=Blueprint("blueprint", __name__)

modelo=VGG16()

@bp.route("/", methods=["GET"])
def obtenerInicio():

	return render_template("inicio.html")

@bp.route("/", methods=["POST"])
def enviarImagen():

	permitidos=["jpg", "jpeg", "png"]

	imagen=request.files["imagen"]

	if imagen.filename=="" or imagen.filename.split(".")[-1] not in permitidos:

		return render_template("inicio.html")

	ruta=os.path.dirname(os.path.join(os.path.dirname(__file__)))

	carpeta=os.path.join(ruta, "imagenes")

	crearCarpeta(carpeta)

	ruta_imagen=os.path.join(carpeta, imagen.filename)

	imagen.save(ruta_imagen)

	imagen_cargada=img_to_array(load_img(ruta_imagen, target_size=(224,224)))

	imagen_ajustada=imagen_cargada.reshape((1,imagen_cargada.shape[0], imagen_cargada.shape[1], imagen_cargada.shape[2]))

	imagen_preprocesada=preprocess_input(imagen_ajustada)

	prediccion=modelo.predict(imagen_preprocesada)

	clase=decode_predictions(prediccion)

	datos_resultado=clase[0][0]

	resultado=f"{datos_resultado[1]} ({round(datos_resultado[2]*100, 2)}%)"

	return render_template("inicio.html", prediccion=resultado)