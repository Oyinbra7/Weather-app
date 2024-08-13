preferences.json:

Stores user preferences, such as the default city. This file is created and managed automatically by the application.
data.py:

Handles loading, saving, and updating user preferences. This includes managing the preferences.json file.
utility.py:

Contains helper functions for validation and formatting, keeping the code clean and modular.
logic.py:

Fetches and processes weather data from the OpenWeatherMap API, using the default city stored in preferences.json.
gui.py:

The GUI handles user interactions, displays weather information, and allows the user to set a new default city, which is then stored in preferences.json.
main.py:

Initializes and runs the application.