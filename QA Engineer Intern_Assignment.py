import requests

API_KEY = "b6907d289e10d714a6e88b30761fae22"
API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data(location, api_key):
    url = f"{API_URL}?q={location}&appid={api_key}"
    response = requests.get(url)
    return response.json()

def get_temperature(data, date):
    for entry in data['list']:
        if entry['dt_txt'] == date:
            return entry['main']['temp']
    return None

def get_wind_speed(data, date):
    for entry in data['list']:
        if entry['dt_txt'] == date:
            return entry['wind']['speed']
    return None

def get_pressure(data, date):
    for entry in data['list']:
        if entry['dt_txt'] == date:
            return entry['main']['pressure']
    return None

def main():
    location = input("Enter the location (e.g., London,us): ")
    data = get_weather_data(location, API_KEY)

    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date in the format 'YYYY-MM-DD HH:MM:SS': ")
            temperature = get_temperature(data, date)
            if temperature is not None:
                print(f"The temperature at {date} is {temperature}°C")
            else:
                print("Data not available for the specified date.")

        elif choice == "2":
            date = input("Enter the date in the format 'YYYY-MM-DD HH:MM:SS': ")
            wind_speed = get_wind_speed(data, date)
            if wind_speed is not None:
                print(f"The wind speed at {date} is {wind_speed} m/s")
            else:
                print("Data not available for the specified date.")

        elif choice == "3":
            date = input("Enter the date in the format 'YYYY-MM-DD HH:MM:SS': ")
            pressure = get_pressure(data, date)
            if pressure is not None:
                print(f"The pressure at {date} is {pressure} hPa")
            else:
                print("Data not available for the specified date.")

        elif choice == "0":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
