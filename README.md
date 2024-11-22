# Gestión de Series con Flask

> Este proyecto se trata de una sencilla aplicación web realizada utilizando Flask que permite a 
los usuarios gestionar y clasificar series de televisión según su interés.

## Funciones principales
1. Registrar usuario.
2. Iniciar sesión.
3. Cerrar sesión.
4. Añadir serie.

Las series podrán ser clasificadas en **3 diferentes categorías**:
* Series que quiero ver.
* Series que estoy viendo.
* Series vistas.

Además, cada serie contendrá **información** sobre la misma como:
* Nombre de la serie.
* Sinopsis.
* Puntuación (de 0 a 10).
* Género.
* Fecha de estreno.
* Número de capítulos.
* Duración de los capítulos (en minutos).

## Ficheros que contiene este proyecto

### app.py
Contiene las funciones necesarias para que funcione la aplicación:
````
1. home()
2. register()
3. login()
4. logout_function()
5. add_series()
````

### Ficheros html
Estos ficheros contienen el código HTML para crear el esqueleto de la aplicación.
````
1. add_serie.html
2. home.html
3. login.html
4. register.html
````

### Ficheros CSS
Estos ficheros contienen el código CSS para dar formato a la aplicación y mostrarla por pantalla de
una manera más atractiva.
````
1. addserie.css
2. homepage.css
3. login.css
4. register.css
````
