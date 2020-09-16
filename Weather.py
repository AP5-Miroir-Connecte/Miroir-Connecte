from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import requests, json
class Weather(QWidget):
    
    def __init__(self, *args, **kwargs):
        super(Weather, self).__init__(*args, **kwargs)
        self.api_key = "c0735eb48963d2eea782623d14502b53"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"
        self.city_name = "Lille"
        self.complete_url = self.base_url + "appid=" + self.api_key + "&q=" + self.city_name
        self.weather = QLabel("", self)
        self.weather.setStyleSheet('color: white')
        self.weather.setFont(QFont('caviar dreams', 24))
        self.weather.setAlignment(Qt.AlignRight)
        self.updateWeather()
    
    def toCelsius(self, kelvin):
        return kelvin - 273.15;
    
    def getWeather(self):        
        response = requests.get(self.complete_url) 
        x = response.json()
        #print(json.dumps(x, indent=2))
        if x["cod"] != "404": 
            self.y = x["main"] 
            self.current_temperature = round(self.toCelsius(self.y["temp"]), 1) 
            self.current_pressure = self.y["pressure"] 
            self.current_humidiy = self.y["humidity"] 
            self.z = x["weather"] 
            self.weather_description = self.z[0]["description"]
            self.weather_icon = self.z[0]["icon"]
            return str(self.current_temperature) + "°C à " + self.city_name
        return "N/A"
    
    def updateWeather(self):
        self.weather.setText(self.getWeather())
    
    def getCurrentTemperature(self):
        return self.current_temperature