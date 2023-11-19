import pyttsx3                          #RISHAV   21BCS3378
import datetime                         #ASHWANI  21BCS1590
import speech_recognition as sr         #KRISHNA  21BCS2423
import webbrowser
import wikipedia
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)

def speak(audio):
       engine.say(audio)
       engine.runAndWait() 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>=12 and hour<18:
            speak("goodafternoon!")
    else:
            speak("good evening")
    speak("hello sir,i am super assistant. how can i help you ")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak voice is recognizing...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
            print("recognizing....")
            query = r.recognize_google(audio,language = 'en-in')
            print(f"user said :{query}\n")
    except Exception as e:

        print("say that again please...")
        return "None"  
    return query

if __name__ == "__main__":
    #speak("my name is super assistant")
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia...")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open blackboard' in query:
            webbrowser.open("cuchd.blackboard.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(strTime)
            
        elif 'open code' in query:
            codePath = "C:\\Users\\risha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open autocad' in query:
            autoPath = "C:\\Program Files\\Autodesk\\AutoCAD 2022\\acad.exe"
            os.startfile(autoPath)
            