
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            data = recognizer.recognize_google(audio)
            print("Recognized:", data)
            return data
        except sr.UnknownValueError:
            print("Not understanding...")
            return ""

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 200)
    engine.say(x)
    engine.runAndWait()

speechtx("Hello")

if __name__ == '__main__':
    while True:
        data1 = sptext().lower()
        if "hello" in data1:
            speechtx("Hello, how can I assist you?")
        elif "your name" in data1:
            name = "My name is Assistant do your Own work !!!!!!"
            speechtx(name)
        elif 'time' in data1:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speechtx("Current time is " + time)
        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/")
        elif 'google' in data1:
            webbrowser.open("https://www.google.com")

        elif 'joke' in data1:
            joke1 = pyjokes.get_joke(language="en")
            print("Joke:", joke1)
            speechtx(joke1)
        elif "exit" in data1:
            speechtx("Thank you")
            break
        else:
            print("Thanks.........")