# logic.py
import requests
from utility import format_weather_data
from data import load_preferences

def get_weather(city_name):
    preferences = load_preferences()
    api_key = "c77a9a07e848d7ca4e9270b5b4362255"  # Ideally, you would load this securely or from preferences
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        weather_data = response.json()
        
        if weather_data["cod"] != "404":
            main_data = weather_data["main"]
            weather_desc = weather_data["weather"][0]["description"]
            temp = main_data["temp"]
            #humidity = main_data["humidity"]
            #pressure = main_data["pressure"]
            
            return format_weather_data(temp, weather_desc)
        else:
            return "City Not Found!"
    
    except requests.exceptions.RequestException:
        return "Failed to retrieve data. Check your internet connection."
