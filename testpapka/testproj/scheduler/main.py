from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler
from scheduler.weather_api import WeatherAPI

        
def start():
    weather_api = WeatherAPI()
    scheduler = BackgroundScheduler()
    scheduler.add_job(weather_api.print_weather, 'interval', seconds=1)
    scheduler.start()
