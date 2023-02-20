from django.apps import AppConfig
from scheduler import main

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        print("APP CONFIG!")
        main.start()
