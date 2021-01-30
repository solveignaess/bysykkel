#Hvor kan jeg finne/ sette fra meg en bysykkel?
=================================================================================
[Python](https://www.python.org/downloads/)-metode som skriver ut en tabell med
oversikt over hvor mange ledige sykler og låser som finnes ved hver av Oslo Bysykkels stasjoner.

Informasjonen blir hentet fra Oslo bysykkels åpne API: [https://oslobysykkel.no/apne-data/sanntid](https://oslobysykkel.no/apne-data/sanntid)

Avhenger av to Python-bibliotek: [Requests](https://pypi.org/project/requests/)
 og [Pandas](https://pypi.org/project/pandas/), som kan installeres med pip fra terminalen

```
$ pip install requests
```
```
$ pip install pandas
```
Kjøres fra terminal:

```
$ python bysykkel.py
```
