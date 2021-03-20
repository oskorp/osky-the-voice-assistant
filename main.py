import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import pyaudio
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Hey Omkar!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Hello sir")

    speak("I'm osky")
    speak("Please tell me how may i help you ?")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please.....")
        return "None"
    return  query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('omkarkhandalkar846@gmail.com', 'Rakmo!@#123')
    server.sendmail('omkarkhandalkar846@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=1)
            speak('According to wikipedia')
            speak(results)
            print(results)



        elif 'open college website' in query:
            webbrowser.open("mydy.dypatil.edu")

        elif 'start youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open Linkedin' in query:
            webbrowser.open("Linkedin.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open dashboard' in query:
            webbrowser.open("http://mydy.dypatil.edu/rait/my/")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"Sir, the time is {strTime}")



        elif 'email to omkar' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "omkarkhandalkar846@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")


            
            



