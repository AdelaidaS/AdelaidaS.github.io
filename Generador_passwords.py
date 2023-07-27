# Adelaida Suarez
# https://www.linkedin.com/in/adelaidasuarezp/

#importamos las librerias necesarias
import random
import os

# pregunytamos al usuario por la longitud de la contraseña
lon_passw = int(input("¿Cuántos caracteres necesitas en tu contraseña? "))

# Carcateres posibles para la contraseña
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

# Unimos la longitud con los caracteres de forma random
p = "".join(random.sample(s, lon_passw))
print("Tu nueva contraseña es:", p)

# Pedir al usuario el nombre que quiere dar al archivo 
nombre_archivo = input("Escribe el nombre del archivo para guardar la contraseña: ")

# Ruta del directorio donde guardar el archivo de la contraseña
carpeta_passwords = "C:\\Documentos\\passwords"

# Verificar si la carpeta existe. Si no existe, la creamos
if not os.path.exists(carpeta_passwords):
    os.makedirs(carpeta_passwords)

# Ruta completa del archivo que contendrá la contraseña
ruta_archivo = os.path.join(carpeta_passwords, nombre_archivo)

# Guardar la contraseña en el archivo
with open(ruta_archivo, "w") as archivo:
    archivo.write(p)

print("Contraseña guardada exitosamente en", ruta_archivo)