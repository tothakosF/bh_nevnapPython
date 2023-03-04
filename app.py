import requests
from datetime import date

response = requests.get('https://api.nevnapok.eu/ma')

long = date.today()

short = long.strftime(r"%m-%d")

first = response.json()[short][0]
second = response.json()[short][1]

print("Üdv Ákos!")
print("A mai névnapok: ", first, "és ", second)

input()
