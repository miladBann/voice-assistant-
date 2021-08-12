from tkinter import *
import pyttsx3
import speech_recognition
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import websites
import weather


text = 0
response = 0
engine = pyttsx3.init()


def recognize():
    global text, response
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, 0.2)
        audio = recognizer.listen(mic)

        text = recognizer.recognize_google(audio)
        text = text.lower()
        response = text
        print(f'recognized:  {text}')


def end_chat():
    engine.say("ok bye")
    engine.runAndWait()


def ask_to_help():
    ask_to_help = ["wanna know anything else?",
                   "can i help you with anything else?", "need another thing?"]
    final_speech = random.choice(ask_to_help)
    engine.say(final_speech)
    engine.runAndWait()


def search_the_internet():
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get("https://www.google.com/")

    search_bar = driver.find_element_by_xpath(
        "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")

    search_bar.click()

    search_for = response.split("search for")[1]

    search_bar.send_keys(search_for)

    search_bar.send_keys(Keys.ENTER)


def use_selenium(website):
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(website)


def continue_chat():
    engine.say("what else do you need?")
    engine.runAndWait()


######################################chat section#################################################


def start_con():
    engine.say("how can i help you?")
    engine.runAndWait()
    chat()


def chat():
    recognize()

    if "weather" in response:
        engine.say("checking the weather")
        engine.runAndWait()
        weather.get_weather_now()
        ask_to_help()
        recognize()
        if "no" in response:
            end_chat()
        elif "yes" in response:
            continue_chat()
            chat()

    elif "open google" in response:
        engine.say("ok bitch, opening google")
        engine.runAndWait()
        use_selenium(websites.web["google"])
        ask_to_help()
        recognize()
        if "no" in response:
            end_chat()
        elif "yes" in response:
            continue_chat()
            chat()

    elif "open youtube" in response:
        engine.say("youtube it is then..")
        engine.runAndWait()
        use_selenium(websites.web["youtube"])
        ask_to_help()
        recognize()
        if "no" in response:
            end_chat()
        elif "yes" in response:
            continue_chat()

    elif "open p******" in response:
        engine.say(
            "oh look who's a horny slut, opening pornhub... just don't cum on the computer")
        engine.runAndWait()
        use_selenium(websites.web["p******"])
        ask_to_help()
        recognize()
        if "no" in response:
            end_chat()
        elif "yes" in response:
            continue_chat()

    elif "search for" in response:
        say = response.split("search for")[1]
        engine.say(f"searching for {say}")
        search_the_internet()
        ask_to_help()
        recognize()
        if "no" in response:
            end_chat()
        elif "yes" in response:
            continue_chat()

##############################user interface#####################################


window = Tk()
window.title("Milo's Voice Assistant")
window.minsize(width=600, height=400)

title_label = Label(text="Talk to me Ya Ward", font=("Arial", 20, "bold"))
title_label.place(x=180, y=20)

listen_label = Label(text="listening...", font=("Arial", 15, "bold"))
listen_label.place(x=280, y=160)

talk = Button(text="Start Conversation", command=start_con)
end = Button(text="End Conversation", command=end_chat)

talk.place(x=180, y=270)
end.place(x=350, y=270)

window.mainloop()
