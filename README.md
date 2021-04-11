# Indeed Web Scraper
Indeed Web Scrapper es un script que se encarga de recoger los datos de las ofertas de trabajo de _Data scientist_ en Barcelona que se suben a [indeed.com](https://es.indeed.com), y almacenarlos en un CSV. Así evitas tener de recorrer las cientos de ofertas de trabajo que permanecen en la web.

El trabajo forma parte de la Practica 1 de la asignatura _Tipología y ciclo de vida de los datos_, del Máster en Ciencia de Datos de la Universitat Oberta de Catalunya.

## Miembros del equipo

Se ha realiada por [Joan Prieto](https://github.com/joanPri) y [Ricardo Martinez](https://github.com/), ambos pertenecen al aula 2 de _Tipología y ciclo de vida de los datos_.

## Instalación

Para ejecutar el script (en python) es necesaria la instalación de diversas bibliotecas:

```
pip install pandas
pip install beautifulsoup4
pip install request
pip install lxml
pip install re
pip install time
pip install selenium
```

Para usar selenium se necesita un driver que haga de interficie con el navegador, estos drivers estan en la carpeta Drivers, en este proyecto el driver està vinculado con el navegador ["inserte navegador aquí"].
Para descargar los drivers:
[enlace driver]

## Ejecturar script (usage)

El script se debe ejecutar de la siguiente manera:

```
python nombreArchivo.py
```
El script se encarga de recoger los datos de indeed y extraer los siguiente campos exportados en un dataset en csv:
- Título del trabajo
- Empresa
- Descricpión
- Link
- Localización

## 
