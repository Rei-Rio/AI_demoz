import pyttsx3
import datetime
import time
import speech_recognition as sr
import webbrowser as wb
import os
import wikipedia
from testcam import Cam

ai = pyttsx3.init()
voices = ai.getProperty('voices')
ai.setProperty('voice', voices[1].id)
rate = ai.getProperty('rate')   # getting details of current speaking rate
ai.setProperty('rate', 175)     # setting up new voice rate


def speak(audio):
    print('A.I: ' + audio)
    ai.say(audio)
    ai.runAndWait()


def getTime():
    Time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    speak(f"It is: {Time}")


# def wikipedia():
#     print(wikipedia.summary(query, sentences=2))
#     ai.say(wikipedia.summary(query, sentences=2))
#     ai.runAndWait()


def welcome():

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning My Lord!")
        speak("I just wake up!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon My Lord!")
    elif hour >= 18 and hour < 24:
        speak("Good Evening My Lord!")
    speak("How can I help you??")


def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        # c.adjust_for_ambient_noise(source)
        c.energy_threshold = 50
        c.dynamic_energy_threshold = False
        c.pause_threshold = 2
        audio = c.record(source, duration=5)

    try:
        your_line = c.recognize_google(audio, language='en-EN')
        print("N.E.E.T: " + your_line)
    except sr.UnknownValueError:
        print('I don\'t get it! Try typing the command!')
        your_line = str(input('Your order is: '))
    return your_line
    # c = sr.Recognizer()
    # with sr.Microphone() as mic:
    #     print("Robot: Im listening...")
    #     audio = c.listen(mic)
    #
    # try:
    #     your_line = c.recongnize_google(audio, language='vi-VN')
    #     print(wikipedia.summary(your_line, sentences=2))
    #     robot = pyttsx3.init()
    #     robot.say(wikipedia.summary(your_line, sentences=2))
    #     robot.runAndWait()
    # except:
    #     your_line = ""
    #
    # print("you: " + your_line)

if __name__ == "__main__":
    welcome()

    while True:
        query = command()
        # All the command will store in lower case for easy recognition
        if "google" in query:
            speak("What should I search now?")
            search = command().lower()
            url = f"https://google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')

        elif "youtube" in query:
            speak("What should I search now?")
            search = command().lower()
            url = f"https://youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "open video" in query:
            meme = r"C:\Users\Admin\Desktop\test\Fast.mp4"
            os.startfile(meme)
        elif 'time' in query:
            getTime()
        elif 'open camera' in query:
            camera = Cam()
        elif 'Wikipedia' in query:
            speak("What should I search now?")
            search = command().lower()
            print(wikipedia.summary(search, sentences=2))
            ai.say(wikipedia.summary(search, sentences=2))
            ai.runAndWait()
        elif "sleep" in query:
            speak("Finally i can sleep...Good bye My Lord")
            quit()








