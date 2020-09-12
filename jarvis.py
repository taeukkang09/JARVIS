import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
import datetime
import calendar
import random
import re
import webbrowser
import urllib.request  # used to make requests
import urllib.parse  # used to parse values into the url


# Plays sound from speakers by using gTTS module to convert text to speech.
def speak(audio):
    # gTTS function returns a .mp3 file with the Google voice saying whatever we pass in (audio)
    tts = gTTS(text=audio, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)


# Get user input and convert into text using speech_recognition module.
def listen():
    r = sr.Recognizer()  # Initialize the recognizer object

    with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio).lower()
            print('You said: ' + command + '\n')
        except sr.UnknownValueError:
            print('Your last command couldn\'t be heard')
            command = listen()

    return command


def getDate():

    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day
    month_names = ['January', 'February', 'March', 'April', 'May',
                   'June', 'July', 'August', 'September', 'October', 'November',
                   'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th',
                      '7th', '8th', '9th', '10th', '11th', '12th',
                      '13th', '14th', '15th', '16th', '17th',
                      '18th', '19th', '20th', '21st', '22nd',
                      '23rd', '24th', '25th', '26th', '27th',
                      '28th', '29th', '30th', '31st']

    return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + '.'


def getTime():
    now = datetime.datetime.now()
    meridiem = ''
    if now.hour >= 12:
        meridiem = 'p.m'
        hour = now.hour - 12
    else:
        meridiem = 'a.m'
        hour = now.hour
    # Convert minute into a proper string
    if now.minute < 10:
        minute = '0'+str(now.minute)
    else:
        minute = str(now.minute)
    return 'Currently, it is ' + str(hour) + ': '+minute+' '+meridiem+' .'


while True:
    command = listen()

    if 'hello' in command:
        speak('Hello Mr.Kang! My name is Jarvis, your virtual assistant. How may I help you sir?')
    elif 'time' in command:
        speak(getTime())
    elif 'date' in command:
        speak(getDate())
    elif 'youtube' in command:
        speak('Yes sir!')
        reg_ex = re.search('youtube (.+)', command)
        if reg_ex:
            domain = command.split("youtube", 1)[1]
            query_string = urllib.parse.urlencode({"search_query": domain})
            html_content = urllib.request.urlopen(
                "http://www.youtube.com/results?" + query_string)
            # finds all links in search result
            search_results = re.findall(
                r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            webbrowser.open(
                "http://www.youtube.com/watch?v={}".format(search_results[0]))
            pass
    elif 'quit' in command:
        speak("Goodbye sir.")
        break
    else:
        speak("I'm sorry, could you repeat that sir?")
