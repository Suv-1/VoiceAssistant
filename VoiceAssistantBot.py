import os
import sys

import pyttsx3 as py
import datetime
import speech_recognition as sr
import webbrowser
import pyaudio
from googlesearch import search
from pathlib import Path

engine = py.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 3 <= hour < 12:
        speak("Good Morning Sir ! ")
    elif 12 <= hour < 18:
        speak("Good Afternoon Sir !")
    elif 18 <= hour < 21:
        speak("Good Evening Sir !")
    else:
        speak("Hello Sir ! ")
    speak("I am Jarvis. Please tell me how can I help you.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)
    try:
        print("Recognising...")
        speak("Recognising")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")
    except Exception as e:
        print("Could you please repeat again ?")
        speak("Could you please repeat again ?")
        return "None"
    return query


home_dir = str(Path.home())
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
        elif 'overflow' in query:
            speak("Opening Stack overflow")
            webbrowser.open("stackoverflow.com")
        elif 'google search' in query:
            speak("Searching in google")
            query = query.replace("google search", "")
            speak("Here are the top search results from google")
            for j in (search(query, tld="co.in", num=10, stop=10, pause=2)):
                print(j)
        elif 'what time' in query:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current time is: ", current_time)
            speak("Current time is")
            speak(current_time)
        elif 'date' in query:
            date = datetime.date.today()
            print("Today is :", date)
            speak("Today is")
            speak(date)
        elif 'tell me about you' in query:
            print("My name is Jarvis and I am your voice assistant. I am here for your help.")
            speak("My name is Jarvis and I am your voice assistant. I am here for your help.")

        elif 'open outlook' in query:
            outlook_path = home_dir + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Outlook.lnk"
            speak("Opening outlook")
            os.startfile(outlook_path)
        elif 'open teams' in query:
            teams_path = home_dir + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams (work or school).lnk"
            speak("Opening teams")
            os.startfile(teams_path)
        elif 'jarvis quit' in query:
            speak("Thanks for your time Sir, have a good day. Signing off...")
            sys.exit()
