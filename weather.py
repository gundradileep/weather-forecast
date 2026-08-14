import requests

API_KEY = "93f7f980448d6f03b80cfa4f8b9336c9" 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str, api_key: str = API_KEY):
    """Fetch weather data for a given city and return a parsed dict."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius. Use "imperial" for Fahrenheit
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].title(),
            "wind_speed": data["wind"]["speed"],
        }

    except requests.exceptions.HTTPError:
        if response.status_code == 401:
            print("Error: Invalid API key. Check your API_KEY value.")
        elif response.status_code == 404:
            print(f"Error: City '{city}' not found. Check the spelling.")
        else:
            print(f"HTTP error occurred: {response.status_code}")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect. Check your internet connection.")
        return None
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def display_weather(weather: dict):
    """Print weather info in a readable format."""
    print("\n" + "=" * 35)
    print(f"  Weather in {weather['city']}, {weather['country']}")
    print("=" * 35)
    print(f"  Condition   : {weather['description']}")
    print(f"  Temperature : {weather['temperature']}°C")
    print(f"  Feels Like  : {weather['feels_like']}°C")
    print(f"  Humidity    : {weather['humidity']}%")
    print(f"  Wind Speed  : {weather['wind_speed']} m/s")
    print("=" * 35 + "\n")


def main():
    print("=== Weather App ===")
    if API_KEY == "YOUR_API_KEY_HERE":
        print("⚠  Please set your OpenWeatherMap API key in API_KEY before running.\n")

    while True:
        city = input("Enter city name (or 'quit' to exit): ").strip()
        if city.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break
        if not city:
            print("Please enter a valid city name.")
            continue

        weather = get_weather(city)
        if weather:
            display_weather(weather)


if __name__ == "__main__":
    main()
