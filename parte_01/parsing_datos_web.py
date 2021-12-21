import requests
import feedparser
from requests.api import head

url = "https://github.com/Fhernd/Python-Curso"
respuesta = requests.get(url)
print(respuesta.status_code)
print()
html = respuesta.text
print(html)
print(respuesta.json)

print()

headers = respuesta.headers
print(type(headers))
print(headers)

print()

print(respuesta.encoding)

print()

url = "https://www.reddit.com/r/Python/.rss"
respuesta = feedparser.parse(url)
print(respuesta["feed"]["title"])

print()

print(respuesta.headers)

print(type(respuesta.entries))

for i in respuesta.entries:
    print(i.link)