import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

# Use gTTS to convert text input(audio) into speech


def speak(audio):
    tts = gTTS(text=audio, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)


speak("Hello, my name is Jarvis, your virtual assistant. How may I help you sir?")

# def listen():
#     r = sr.Recognizer()  # Initialize the recognizer

#     with sr.Microphone as source:
#         print("JARVIS is ready...")
#         # Pauses for 1 second to allow recognizer to adjust to background noise
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         command = r.recognize_google(audio).lower()
#         print('You said: ' + command + '\n')

#     except sr.UnknownValueError:
#         print('Your last command couldn\'t be heard')
#         command = listen()

#     return command


# def jarvis(command):
#     errors = [
#         "I don\'t know what you mean!",
#         "Excuse me?",
#         "Can you repeat it please?",
#     ]

#     if 'Hello' in command:
#         speak('Hello! I am TARS. How can I help you?')

#     else:
#         error = random.choice(errors)
#         speak(error)


# speak('TARS is ready!')


# while True:
#     jarvis(listen())
