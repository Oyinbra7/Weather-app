import json
import os

# Path to the preferences.json file
PREFERENCES_FILE = "preferences.json"

def load_preferences():
    """Load user preferences from the preferences.json file."""
    if os.path.exists(PREFERENCES_FILE):
        with open(PREFERENCES_FILE, 'r') as file:
            return json.load(file)
    else:
        return create_default_preferences()

def create_default_preferences():
    """Create a default preferences.json file."""
    default_prefs = {
        "default_city": "New York"
    }
    save_preferences(default_prefs)
    return default_prefs

def save_preferences(preferences):
    """Save user preferences to the preferences.json file."""
    with open(PREFERENCES_FILE, 'w') as file:
        json.dump(preferences, file, indent=4)

def update_default_city(city_name):
    """Update the default city in the preferences."""
    preferences = load_preferences()
    preferences["default_city"] = city_name
    save_preferences(preferences)

