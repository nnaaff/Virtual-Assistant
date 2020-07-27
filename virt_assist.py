import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests

print("Loading Adam, your virtual personal assistant.")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hi Nafisa, Good Morning!")
        print("Hi Nafisa, Good Morning!")
    elif hour >= 12 and hour < 17:
        speak("Hi Nafisa, Good Afternoon!")
        print("Hi Nafisa, Good Afternoon!")
    else:
        speak("Hi Nafisa, Good Evening")
        print("Hi Nafisa, Good Evening")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:   # EXC
        print("Adam is listening...")
        audio = r.listen(source)   # EXC

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"Nafisa said: {statement}\n")

        except Exception as e:
            speak("I'm sorry, could you please repeat that?")
            print("I'm sorry, could you please repeat that?")
            return "None"
        return statement

speak("I'm Adam, your virtual personal assistant.")
wishMe()

if __name__=='__main__':

    while True:
        speak("How may I help you?")
        statement = takeCommand().lower()   # EXC
        if statement == 0:
            continue

        if 'bye' in statement or 'good bye' in statement or 'stop' in statement:
            speak("Bye Nafisa!")
            print('Adam is shutting down. Goodbye!')
            break

        if 'time' in statement:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is: {time}.")
            
        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is now open.")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google Chrome is now open.")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail is now open.")
            time.sleep(5)

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences = 3)
            speak("According to Wikipedia, ")
            print(results)
            speak(results)

        elif 'open stackoverflow' in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Stackoverflow is now open.")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are a few headlines from the Times of India:')
            time.sleep(6)

        elif 'camera' in statement or 'click' in statement or 'take a photo' in statement:
            ec.capture(0, "robo camera", "img.jpg")

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            speak("I can answer your computational and geographical questions. What do you want to know?")
            question = takeCommand()
            app_id = ""  # enter your API Key
            client = wolframalpha.Client('')  # your API Key
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "weather" in statement:
            api_key=""  # your API key
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("What is the name of your city?")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak("The temperature in Kelvins is: " +
                      str(current_temperature) +
                      "\nThe percentage-Humidity is: " +
                      str(current_humidiy) +
                      "\nDescription:  " +
                      str(weather_description))
                print("The temperature in Kelvins is: " +
                      str(current_temperature) +
                      "\nThe percentage-Humidity is: " +
                      str(current_humidiy) +
                      "\nDescription:  " +
                      str(weather_description))

            else:
                speak("I'm sorry, I couldn't find your city.")

        elif 'who are you' in statement or 'what can you do' in statement:
            speak("I am Adam, Nafisa's virtual personal assistant. I can execute minor tasks like opening YouTube, Google Chrome, Gmail, Stackoverflow,"
                  " telling the current time, taking a photo, searching Wikipedia, telling the weather in different cities," 
                  " getting you the top headlines from the Times of India, and answering your computational or geographical questions!")

time.sleep(3)       
        
        




