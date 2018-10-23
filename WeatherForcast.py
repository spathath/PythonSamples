import re
import string
import uuid
import requests
import json

class WeatherInfo:
    def __init__(self, weatherData):
        self.data = json.loads(weatherData)
    def name(self):
        return self.data['name']
    def country(self):
        return self.data['sys']['country']
    def status(self):
        return self.data['weather'][0]['description']
    def sunrise(self):
        return self.data['sys']['sunrise']
    def sunset(self):
        return self.data['sys']['sunset']
    

class WeatherForcast:
    def ValidateInput(self):
        if self.zipCode is None:
            print("Invalid zipCode")
            return False
        #.....
        return True

    def GetWeatherData(self):
        if(self.ValidateInput()):
            print(self.wheatherAPIurl + "?zip=" + self.zipCode + ","+self.countryCode + "&APPID=" + self.appid)
            response = requests.get(self.wheatherAPIurl + "?zip=" + self.zipCode + ","+self.countryCode + "&APPID=" + self.appid)
            if response.status_code == 200:
                self.weatherData = WeatherInfo(response.text)
                return True
            else:
                print("Error in API call, enter valid zip and country. Response code received:" + str(response.status_code) + " message:" + response.text)
                return False
            
    def DisplayWheatherInfo(self):
        if(self.weatherData is not None):
            print("Weather for the City:" + self.weatherData.name() + "," + self.weatherData.country())
            print("Status:" + self.weatherData.status())
            print("Sunrise:" + str(self.weatherData.sunrise()))
            print("Sunset:" + str(self.weatherData.sunset()))

    def __init__(self, zipCode, countryCode):
        self.zipCode = zipCode
        if countryCode is None:
            countryCode = "us"
        self.countryCode = countryCode
        self.wheatherAPIurl = "https://api.openweathermap.org/data/2.5/weather"
        self.appid="eac5f12bd15be6243e7842762867b334"
        self.weatherData = None


print("Get weather information")
zipCode = input("Enter Zip code:")
countryCode = input("Enter Country (Default 'US'):")
weather =  WeatherForcast(zipCode,countryCode)
if weather.GetWeatherData():
    weather.DisplayWheatherInfo()

