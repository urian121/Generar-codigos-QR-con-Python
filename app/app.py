from flask import Flask, render_template, request
import qrcode # Importamos el modulo necesario para trabajar con codigos QR
from flask import send_file #biblioteca o modulo send_file para forzar la descarga
import uuid  #Modulo de python para crear un string
from os import path #Modulo para obtener la ruta o directorio


#Declarando nombre de la aplicación e inicializando
app = Flask(__name__)


#Creando un Decorador
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('public/index.html')



@app.route("/qr", methods=['GET', 'POST'])
def CrearCodigoQR():
    #Recibiendo string desde el form para convertir a QR
    inputQR     = request.form['qr']

    # Codificando datos usando la función make(),
    img = qrcode.make(inputQR) 
    nombreQR = uuid.uuid4().hex + '.png'      #Nombre aleatorio
    #path para guardar el codigo qr
    basepath = path.dirname (__file__) + '/static/qrs/'
    # Guardar como un archivo de imagen
    img.save(basepath + nombreQR)

    msg=''
    return render_template('public/index.html', msg ='Codigo QR creado.!', imgQR = nombreQR)
    
    

@app.route("/qrs", methods=['GET', 'POST'])
def CrearCodigoQRS():
    inputQR     = request.form['qr']
    qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5
            )    
    qr.add_data(inputQR)
    
    # Este método con ( fit = Verdadero ) asegura que se utilice toda la dimensión del Código QR,
    # incluso si nuestros datos de entrada podrían caber en menos número de cuadros
    qr.make(fit=True)
    #El método make_image se utiliza para convertir el objeto QRCode en un archivo de imagen
    img = qr.make_image(
                fill='black',
                back_color='yellow'
            )
    
    basepath = path.dirname (__file__) + '/static/qrs/'
    nombreQR = uuid.uuid4().hex + '.png'      #Nombre aleatorio para la imagen QR
    img.save(basepath + nombreQR)
    
    msg=''
    return render_template('public/index.html', msg ='Codigo QR creado.!', imgQR = nombreQR)
   
        
        
@app.route('/descargar-qr/<string:nombreImagenQR>', methods=['GET','POST'])
def descargar_qr(nombreImagenQR=''):
    basepath = path.dirname (__file__) 
    url_File = path.join (basepath, 'static/qrs/', nombreImagenQR)
    #send_file toma 2 parametros, el primero será la ruta del archivo y el
    # 2 será as_attachment=True porque deseamos que el archivo sea descargable.
    resp =  send_file(url_File, as_attachment=True)
    return resp 



# Manejar el error 404 o el error de ruta no válida en Flask es definir
# un controlador de errores para manejar el error 404
@app.errorhandler(404)
def not_found(error):
    return render_template('public/index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000)