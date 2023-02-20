import requests
from testproj.main import models

x = requests.get("""https://api.openweathermap.org/data/2.5/weather?q=Караганда&appid=14951c93f3d11e8ac8bed96dd90e8bc7&units=mehttpstric""")

print(x.text)

weather = models.Weather()

weather.coord = x.get("coord")
