# utility.py

def validate_city_name(city_name):
    """Validates the city name entered by the user."""
    return city_name.replace(" ", "").isalpha()

def format_weather_data(temp, description):
    """Formats weather data into a string for display."""
    return f"Temperature: {temp}°C\n" \
            f"Weather Description: {description.title()}"
           #f"Humidity: {humidity}%\n" \
           #f"Pressure: {pressure} hPa\n" \
         
