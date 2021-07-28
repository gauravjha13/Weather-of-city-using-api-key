# A program that displays the weather of a city using an API key and stores the data for the same in a text file.

import requests
from datetime import datetime

api_key = 'e51899a0d69119f5321530f7702155af'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

country = api_data['sys']['country']
lon = api_data['coord']['lon']
lat = api_data['coord']['lat']
temp = ((api_data['main']['temp']) - 273.15)  # - 273.15 used to convert F to C
weather = api_data['weather'][0]['description']
humid = api_data['main']['humidity']
wind_speed = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


def weather_write_data():   # Function Declaration

    print("-----------------------------------------------------------------")
    print("Weather Status of - {} ({}) || {}".format(location.upper(), country.upper(), date_time))
    print("-----------------------------------------------------------------")

    print(f"Longitude : {lon} || Latitude : {lat}")
    print("Current temperature is : {:.1f} Deg C".format(temp))
    print(f"Current weather Description : {weather}")
    print(f"Current Humidity : {humid} %")
    print(f"Current wind speed : {wind_speed} KmPh")

    print("-----------------------------------------------------------------")
    print(f"Complete Link : {complete_api_link}")
    print("-----------------------------------------------------------------")


weather_write_data()    # Function Call

# -----------------------File Operations Starts Here ------------------------------

file = open(r"weather.txt", "a+")   # append data at the end of file.

file.write("-----------------------------------------------------------------\n")
file.write("Weather Status of - {} ({}) || {} \n".format(location.upper(), country.upper(), date_time))
file.write("-----------------------------------------------------------------\n")

file.write(f"Longitude : {lon} || Latitude : {lat} \n")
file.write("Current temperature is : {:.1f} Deg C\n".format(temp))
file.write(f"Current weather Description : {weather} \n")
file.write(f"Current Humidity : {humid} % \n")
file.write(f"Current wind speed : {wind_speed} kmph\n")

file.write("-----------------------------------------------------------------\n")
file.write(f"Complete Link : {complete_api_link}\n")
file.write("-----------------------------------------------------------------\n")
file.write("\n")

file.close()