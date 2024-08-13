# gui.py
import tkinter as tk
from tkinter import messagebox
from logic import get_weather
from utility import validate_city_name
from data import load_preferences, update_default_city

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lagos Weather App")
        self.root.geometry("400x400")

        # GUI Elements
        self.city_label = tk.Label(root, text="Enter city name:", font=("Helvetica", 12))
        self.city_label.pack(pady=10)

        self.city_entry = tk.Entry(root, width=30, font=("Helvetica", 14))
        self.city_entry.pack(pady=10)

        self.search_button = tk.Button(root, text="Search", command=self.search_weather, font=("Helvetica", 12), bg="lightblue")
        self.search_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.result_label.pack(pady=20)
        
        self.save_default_button = tk.Button(root, text="Set as Default City", command=self.save_default_city, font=("Helvetica", 10), bg="yellow")
        self.save_default_button.pack(pady=10)
        
        # Load default city weather at startup
        self.load_default_city_weather()

    def search_weather(self):
        city_name = self.city_entry.get()
        if city_name:
            if validate_city_name(city_name):
                weather_info = get_weather(city_name)
                if "Failed to retrieve data" in weather_info or "City Not Found!" in weather_info:
                    messagebox.showerror("Error", weather_info)
                else:
                    self.result_label.config(text=weather_info)
            else:
                messagebox.showwarning("Input Error", "Invalid city name! Please enter a valid city name.")
        else:
            messagebox.showwarning("Input Error", "Please enter a city name!")

    def save_default_city(self):
        """Save the currently entered city as the default city."""
        city_name = self.city_entry.get()
        if validate_city_name(city_name):
            update_default_city(city_name)
            messagebox.showinfo("Success", f"{city_name} has been set as the default city.")
        else:
            messagebox.showwarning("Input Error", "Please enter a valid city name before saving.")

    def load_default_city_weather(self):
        """Load weather information for the default city."""
        preferences = load_preferences()
        default_city = preferences["default_city"]
        weather_info = get_weather(default_city)
        if "Failed to retrieve data" not in weather_info:
            self.result_label.config(text=weather_info)
            self.city_entry.insert(0, default_city)
        else:
            self.result_label.config(text="Welcome! Please enter a city to get started.")
