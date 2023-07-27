# Adelaida Suarez 
# https://www.linkedin.com/in/adelaidasuarezp/


#importar la libreria time
import time
import winsound
from colorama import init, Fore

#crear la funcion del temporizador
# Inicializar colorama para los colores en Windows
init()

# Crear la función del temporizador
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(Fore.YELLOW + timer, end='\r')
        time.sleep(1)
        t -= 1

    print(Fore.GREEN + '¡Tiempo agotado!')
    winsound.Beep(1000, 800)  # Emitir un sonido al finalizar el temporizador

# El usuario ingresa el tiempo
t = input('Indica el tiempo en segundos: ')

# Llamamos a la función
print(Fore.CYAN + 'Iniciando temporizador...')
countdown(int(t))