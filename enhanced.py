# Importing necessary libraries
import speech_recognition as sr  # For speech recognition
import pyttsx3  # For text-to-speech conversion
import datetime  # For handling date and time functions
import webbrowser  # For opening web pages
import os  # For interacting with the operating system
import random

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(audio):
    """Converts text to speech."""
    print("Jarvis:", audio)
    engine.say(audio)
    engine.runAndWait()

def greet_user():
    """Greets the user based on the current time of day."""
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis, your virtual assistant. How can I help you today?")

def take_command():
    """Listens for a command from the user and returns it as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Please say that again.")
        return "None"
    return query.lower()

def open_application(command):
    """Opens a specific application on the PC based on the user's command."""
    if 'open notepad' in command:
        speak("Opening Notepad")
        os.system("notepad")
    elif 'open command prompt' in command or 'open cmd' in command:
        speak("Opening Command Prompt")
        os.system("start cmd")
    elif 'open settings' in command:
        speak("Opening Settings")
        os.system("start ms-settings:")
    elif 'open microsoft store' in command or 'open store' in command:
        speak("Opening Microsoft Store")
        os.system("start ms-windows-store:")
    elif 'open calculator' in command:
        speak("Opening Calculator")
        os.system("calc")
    elif 'open paint' in command:
        speak("Opening Paint")
        os.system("mspaint")
    elif 'open file explorer' in command or 'open explorer' in command:
        speak("Opening File Explorer")
        os.system("explorer")
    elif 'open task manager' in command:
        speak("Opening Task Manager")
        os.system("taskmgr")
    else:
        speak("Sorry, I don't recognize that application command.")

def open_website(command):
    """Opens a website based on user's command."""
    if 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'open instagram' in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")
    elif 'open discord' in command:
        speak("Opening Discord")
        webbrowser.open("https://www.discord.com")
    elif 'open facebook' in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif 'open telegram' in command:
        speak("Opening Telegram")
        webbrowser.open("https://web.telegram.org")
    elif 'open amazon' in command:
        speak("Opening Amazon")
        webbrowser.open("https://www.amazon.com")
    elif 'open flipkart' in command:
        speak("Opening Flipkart")
        webbrowser.open("https://www.flipkart.com")
    elif 'open netflix' in command:
        speak("Opening Netflix")
        webbrowser.open("https://www.netflix.com")
    elif 'open amazon prime' in command:
        speak("Opening Amazon Prime")
        webbrowser.open("https://www.primevideo.com")
    elif 'open spotify' in command:
        speak("Opening Spotify")
        webbrowser.open("https://www.spotify.com")
    elif 'open steam' in command:
        speak("Opening Steam")
        webbrowser.open("https://store.steampowered.com")
    elif 'open google classroom' in command:
        speak("Opening Google Classroom")
        webbrowser.open("https://classroom.google.com")
    elif 'open google mail' in command or 'open gmail' in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")
    elif 'open chatgpt' in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chat.openai.com")
    else:
        speak("Sorry, I don't recognize that website command.")

def play_music():
    """Plays a random music file from a specified directory."""
    music_dir = 'C:\\Users\\Hp\\Music'
    songs = os.listdir(music_dir)
    if songs:
        song = random.choice(songs)
        os.startfile(os.path.join(music_dir, song))
        speak("Playing music")
    else:
        speak("No music files found in the directory.")

def get_time():
    """Tells the current time in hours and minutes."""
    time_now = datetime.datetime.now().strftime("%H:%M")
    speak(f"The time is {time_now}")

def main():
    """Main function to start the assistant and handle user commands."""
    greet_user()
    while True:
        query = take_command()

        if query == "None":
            continue

        if any(kw in query for kw in [
            'open youtube', 'open google', 'open stack overflow', 'open instagram',
            'open discord', 'open facebook', 'open amazon', 'open flipkart',
            'open spotify', 'open steam', 'open google classroom', 'open google mail', 
            'open gmail', 'open telegram', 'open netflix', 'open amazon prime', 'open chatgpt']):
            open_website(query)
        elif any(kw in query for kw in [
            'open notepad', 'open command prompt', 'open cmd', 'open settings',
            'open microsoft store', 'open store', 'open calculator', 'open paint', 
            'open file explorer', 'open explorer', 'open task manager']):
            open_application(query)
        elif 'play music' in query:
            play_music()
        elif 'the time' in query:
            get_time()
        elif any(kw in query for kw in ['exit', 'quit', 'see you', 'bye']):
            speak("Goodbye!")
            break

# Start the assistant
main()
