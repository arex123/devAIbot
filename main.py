# ask dev(a automated robot) to play music or video on youtube and also you can ask him time

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()

engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'dev' in command:
                command = command.replace('dev', '')
                print(command)

    except Exception as e:
        print(f"I think you are at very noisy place,\nThis is the error in computer languge: {str(e)}")
    return command


def run_dev():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk(time)


run_dev()
