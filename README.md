# Indeed Web Scraper
Indeed Web Scrapper es un script que se encarga de recoger los datos de las ofertas de trabajo de _Data scientist_ en Barcelona que se suben a [indeed.com](https://es.indeed.com), y almacenarlos en un CSV. Así evitas tener de recorrer las cientos de ofertas de trabajo que permanecen en la web.

El trabajo forma parte de la Practica 1 de la asignatura _Tipología y ciclo de vida de los datos_, del Máster en Ciencia de Datos de la Universitat Oberta de Catalunya.

## Miembros del equipo

Se ha realiada por [Joan Prieto](https://github.com/joanPri) y [Ricardo Martinez](https://github.com/), ambos pertenecen al aula 2 de _Tipología y ciclo de vida de los datos_.

## Instalación

Para ejecutar el script (en python) es necesaria la instalación de diversas bibliotecas:

```
import selenium
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
```

Para usar selenium se necesita un driver que haga de interficie con el navegador, estos drivers estan en la carpeta Drivers, en este proyecto el driver està vinculado con el navegador ["inserte navegador aquí"].
Para descargar los drivers:
[enlace driver]

## Entorno de desarrollo
Para llevar a cabo el proyecto nos hemos ayudado de la distribucion de Anaconda. Esta nos facilita el paquete Python para poder trabajar con dicho lenguaje de progrmación.
Por lo tanto es necesario disponer de Anaconda instalado en Windows10 (se opta por este sistema operativo por ser de fácil manejo y de amplia implemetnación).

## Ejecturar script (usage)
Para poder ejecutar el script dispuesto en este proyecto, deberemos de disponer en la misma caparpeta el Driver "geckodriver", este driver corresponde a Firefox. Es el que hemos elegido aunque se podria dispuesto de otro driver (en la carpeta adjunta se disponen lo drives de Edge y de Chrome) para implementar el scrapper.
Por lo tanto desde la linea de comandados en el prompt de Anaconda, y situandonos en el directorio donde se encuentre el fichero, tenemos que:
Ejecutar de la siguiente manera el script:
```
python nombreArchivo.py
```
El script se encarga de recoger los datos de indeed y extraer los siguiente campos exportados en un dataset en csv:
- Título del trabajo - String(recoge el tag titulo de cada clickcard)
- Empresa - String (recoge el tag de la compañia anunciante)
- Descripción - String (recoge la descripción completa que se obtiene 
- Link
- Localización
- Descripcion empleo
- Fecha de publicación
- Profile

Debemos de comentar los siguientes puntos de intere:
- Para poder interactuar con los elementos que nos ofrecia la pagina web seleccionada empleamos Selenium.
Al emplear dicho paquete frente a Request, hemos encontrado un inconveniente y es la detección de los bots por parte de las páginas Web así como la denegación de acceso a la web por "hcaptcha". Tras investigar como intentar implementar un comportamiento mas humano a nuestro bot, (modificanod el user agent en la options del driver cuando lanzamos las peticiones, como cancelando los alert dialog que se nos muestran,etc) no hemos podido conseguir pasar del paginado número 5.
Por lo tanto obtenemos el total de los puesto de trabajo de las 4 paginas primeras.

## Futuros pasos
Para continuar indagando en el mundo del scrapping debemos conocer en mayor medida como trabajan estos detectores de bots, asi como implementar tecnicas que recreen de manera mas correcta la interacción humana. Además seria buena idea añadir un menú o la posibilidad de añadir parametros a la ejecución del script. 

## 
