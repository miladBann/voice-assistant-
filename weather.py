import requests
import pyttsx3


def get_weather_now():
    engine = pyttsx3.init()
    api_key = "ec5700c59e5d4f228ab224413210108"

    response = requests.get(
        "http://api.weatherapi.com/v1/current.json?key=ec5700c59e5d4f228ab224413210108&q=Jerusalem&aqi=no").json()

    current_weather = response["current"]["temp_c"]
    engine.say(f"its currently {current_weather} celcius outside")
    engine.runAndWait()
