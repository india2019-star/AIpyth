import pyttsx3
import datetime
import os
import speech_recognition as sr
import wikipedia
import webbrowser
import numpy as np


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speaking(audio):
    engine.say(audio)
    engine.runAndWait()
def text():
    speaking("Hi, i am your assistant  speaking, ")
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour <= 12:
        speaking("Good morning")
    elif hour > 12 and hour < 18:
        speaking("Good afternoon")
    elif hour >= 18 and hour <20:
        speaking("Good evening")
    else:
        speaking("Good night")

def takequery():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1.3
        #r.energy_threshold = 300
        audio = r.listen(source)
        try:
            print("RECOGNIZING.....")
            query = r.recognize_google(audio,language = "en-in")
            print(f"user said {query}\n")
        except Exception as e:
            speaking("Sorry, could not get it sir")
            speaking("please try again") 
            return "None"
            
    return query
       
text()
while(1):     
    
    qu = takequery().lower()
    if "dismiss" in qu:
        speaking("thank you sir have a nice day")
        exit(0)
    elif "time" in qu:
        str1 = datetime.datetime.now().strftime("%H:%M:%S")
        speaking(f'sir, the time is {str1}')
    elif "wikipedia" in qu:
        speaking("searching for wikipedia")
        results = wikipedia.summary(qu,sentences = 5)
        print(results)
        speaking("according to wikipedia,")
        speaking(results)
    elif "google" in qu:
        speaking("opening google")
        dir = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(dir)
    elif "location" in qu:
        speaking("opening google maps")
        webbrowser.open("https://www.google.com/maps/@22.6257891,88.3543144,17.56z")
        
    elif "youtube" in qu:
        speaking("opening youtube")
        webbrowser.open("youtube.com")
    elif "how are you" in qu:
        speaking("i am fine sir")
        speaking("what can i do for you")
    elif "weather updates" in qu:
        speaking("weather updates coming up")
        webbrowser.open("https://weather.com/en-IN/weather/today/l/22.62,88.35?par=google&temp=c")
    elif "gender" in qu:
        speaking("my gender is male")
        
    elif "rediffmail" in qu:
        speaking("opening rediffmail")
        webbrowser.open("rediffmail.com")
    elif "command prompt" in qu:
        direc = "C:\\Users\Raj\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools"
        speaking("opening command prompt")
        os.startfile(os.path.join(direc))
    elif "play games online" in qu:
        speaking("opening games")
        webbrowser.open("https://www.google.com/search?sxsrf=ACYBGNQcgseaLj77xJcHsDoeLBrfmmm68Q%3A1569736073168&ei=iUWQXav1CYnxvgSG9ra4Dg&q=small+games+play+online&oq=small+games+play+online&gs_l=psy-ab.3..0j0i22i30l7.2847.6028..7362...0.2..0.231.2535.0j2j10......0....1..gws-wiz.......0i71j0i67j0i20i263.1jnkAgkABYg&ved=0ahUKEwjr3aDIqvXkAhWJuI8KHQa7DecQ4dUDCAs&uact=5")
    elif "jokes" in qu:
        speaking("opening jokes")
        webbrowser.open("https://www.santabanta.com/jokes/")
    elif "play music" in qu:
        direc2 = "C:\\Users\\Raj\\Downloads\\music"
        listing = os.listdir(direc2)
        i = np.random.randint(low = 0,high = (len(listing)-1))
        os.startfile(os.path.join(direc2,listing[i]))
    elif "open visual code" in qu:
        dir = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
        os.startfile(dir)
    else:
         
        try:
            results1 = wikipedia.summary(qu,sentences = 2)
            print(results1)
            speaking(results1)

        except Exception as e:
            print("sorry, results not found")

        


        
    
     
    


             

       