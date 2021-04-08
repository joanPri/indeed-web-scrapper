import pandas as pd
from bs4 import BeautifulSoup
import requests
import lxml
import re


def findContentByClass(atributo, clase, arrayData, soup):
    if(atributo == ''):
        items = soup.find_all(class_=clase, partial=False)
    else:
        items = soup.find_all(atributo, class_=clase, partial=False)
    for item in items:
        s = str(item)
        cleanHtml = re.sub('<[^>]+>', '', s).strip()
        arrayData.append(cleanHtml)
    return arrayData

def findHrefByClass(clase, arrayData, soup):
    items = soup.find_all('a', class_=clase, partial=False)
    for item in items:
        href = item.get('href')
        href = 'https://es.indeed.com' + str(href)
        arrayData.append(href)
    return arrayData


URL = "https://es.indeed.com/jobs?q=data+scientist&l=Barcelona&filter=0&sort=date&start=0"

respuesta = requests.get(URL)
status_code = respuesta.status_code
if status_code == 200:

    jobtitleArray = []
    CompanyArray = []
    locationArray = []
    linkArray = []

    # Pasamos el contenido HTML de la web a un objeto lxml
    soup = BeautifulSoup(respuesta.content, "lxml")
    paginas = soup.find(id='searchCountPages')
    res = str(paginas).split()
    numElements = int(res[5]) #number of elements
    print(URL[75:])  # substring from "start" to final

    start = 0
    while start < numElements:

        respuesta = requests.get(URL)
        soup = BeautifulSoup(respuesta.content, "lxml")

        jobtitle = findContentByClass('a', "jobtitle", jobtitleArray, soup)
        companyName = findContentByClass('span', "company", CompanyArray, soup)
        location = findContentByClass('', "accessible-contrast-color-location", locationArray, soup)
        link = findHrefByClass("jobtitle", linkArray, soup)

        replace = "start=" + str(start)
        iterateURL = URL.replace(URL[75:], replace)
        print(iterateURL)
        start += 10  # Esto es lo mismo que escribir:  count = count + 1

    data = {'title': jobtitle, 'company': companyName, 'location': location, 'URL': link}
    df = pd.DataFrame(data)
    print(df)

    df.to_csv('indeedScrap.csv', index=False)







else:
    print("Status Code %d" % status_code)