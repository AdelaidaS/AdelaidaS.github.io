# Adelaida Suarez
# https://www.linkedin.com/in/adelaidasuarezp/

#importar las librerias necesarias
import random

#crear la funcion para generar cuentos: 
def generate_story():
    when = ['Hace años','La noche del viernes','Hace muchos, muchos años','El 15 de abril del 90',  'En el siglo XIX','Durante las vacaciones de verano','Erase una vez que se era','En el futuro', 'En un dia soleado','En un lluvioso dia de verano','En un Universo paralelo','En el mundo de los sueños', 'En una noche oscura y triste','En la edad de los dinosaurios','En los tiempos de Maricastaña']
    who = ['un conejo', 'un ratón', 'una tortuga',  'un viejo caballero', 'una brillante joven','un simpático alienigena','un viajero en el tiempo','un incansable detective', 'un pirata tuerto','un superheroe chiflado','un dragón feroz','una reina sabia','un loco rey']
    name = ['Ali', 'Miriam','Tokyo','Oma', 'Maximus','Barbie','Pepa','Denver','Liliana','Paula','Ale','Madalena','Sansón']
    residence = ['Barcelona', 'Bilbao', 'Venecia', 'Venice', 'Escocia', 'New York', 'Adelaide','Paris', 'Sydney','Rio de Janeiro','Miami', 'Dubai','Toronto','Cuenca','Sevilla','Singapur']
    went = ['cine', 'campus universitario','curso de Python','colegio', 'mercado', 'museo',  'concierto','refugio de montaña', 'bosque mágico','bosque de gominolas','mundo submarino','observatorio lunar','monte perdido','mundo del revés','portal en el tiempo','rio embrujado de pirañas','bar',  'agujero negro']
    happened = ['hizo muchos amigos','comió hasta explotar','encontró la llave secreta del tesoro de la Niñera','resolvió un misterio misterioso','escribió el libro más pequeño del munfo. "Fin"','construyó una casa rosa en el árbol','creó una nueva receta de arroz negro', 'descubrió un tesoro escondido','aprendió el idioma de los elfos','ganó un concurso de regeton', 'inventó una máquina del tiempo','rescató a un animal perdido','organizó un baile de disfraces','navegó a través del océano protegiendo el mediom ambiente','completó un maratón de ver pelis en Netflix', 'pintó una hermosa obra de arte','logró su sueño de toda la vida','ayudó a su hermano con los deberes', 'exploró un nuevo planeta y le `p`puso de nombre Pimpilipauxa','se encontró con una criatura mítica cubierta de chuches y caramelos', 'derrotó a un hechicero malvado','resolvió un enigma ancestral', 'rompió el récord mundial de baile', 'salvó un reino mágico','desentrañó una maldición mágica']

    story = (
        random.choice(when) + ', ' +
        random.choice(who) + ' de nombre ' +
        random.choice(name) + ' que vivía en ' +
        random.choice(residence) + ', fué al ' +
        random.choice(went) + ' y ' +
        random.choice(happened) + '.'
    )
    return story

# Pedir al usuario cuántas historias desea crear
num_stories = int(input("¿Cuántas historias aleatorias deseas generar? "))

# Crear y mostrar las historias
for _ in range(num_stories):
    print('Esta historia que te voy a contar, siempre será diferente... ¡Escucha!')
    print(generate_story())
    print('Y colorín colorado, este cuento se ha acabado.')