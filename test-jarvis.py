import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        #links to websites

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open spotify' in query:
            webbrowser.open("spotify.com")   

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open chatgpt' in query:
            webbrowser.open("chatgpt.com")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'open discord' in query:
            webbrowser.open("discord.com")

        #music play

        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        #tell the time now

        elif 'what is the time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        #open apps installed on pc

        elif 'open code' in query:
            codePath = "C:\\Users\\Hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open emulator' in query:
            codePath = "C:\\Program Files\\BlueStacks_nxt\\HD-Player.exe"
            os.startfile(codePath)

        elif 'open browser' in query:
            codePath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(codePath)

        #open windows app form system 32

        elif 'open cmd' in query:
            codePath = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(codePath)

        elif 'open notepad' in query:
            codePath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(codePath)

        elif 'open task manager' in query:
            codePath = "C:\\Windows\\System32\\taskmgr.exe"
            os.startfile(codePath)

        #open windows apps

        elif 'open this pc' in query:
            codePath = "C:\\Windows\\explorer.exe"
            os.startfile(codePath)

        #end command
        elif 'see you later' in query:
            codePath = "C:\\Windows\\System32\\notepa.exe"
            os.startfile(codePath)

        elif 'email to my phone' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "dushyantrajotia@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")    
        else:
            print("No query matched")