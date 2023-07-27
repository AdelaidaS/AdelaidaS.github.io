#Adelaida Suarez 
# https://github.com/AdelaidaS

#pip install qrcode

import qrcode
import os

data = 'https://www.linkedin.com/in/adelaidasuarezp/'

#personalizamos la apariencia del qr code
qr = qrcode.QRCode(version = 1, box_size=10, border=5)
qr.add_data(data)
qr.make (fit=True)

#generamos la imagen del qr code
img = qr.make_image(fill_color = 'purple', back_color = 'white')

# Obtener la ruta actual del archivo .py
current_directory = os.path.dirname(os.path.abspath(__file__))

# Pedir al usuario el nombre del archivo
file_name = input("Ingresa el nombre del archivo sin la extensión (.png): ")

# Combinar la ruta y el nombre del archivo
file_path = os.path.join(current_directory, f"{file_name}.png")

# Guardar como un archivo de imagen
img.save(file_path)

print(f"El código QR se ha guardado exitosamente como '{file_name}.png' en la misma ubicación que este archivo Python.")

