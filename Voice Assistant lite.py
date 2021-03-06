import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

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
            if 'alexa' in command:
                command = command.replace('dani', '')
                # talk(command)
    except:
        pass
    return command

def run_dani():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play ', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'tell me a joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'thank you' or 'good bye' in command:
        exit()
    else:
        error_msg = "Sorry didn't catched that... Please repeat!"
        print(error_msg)
        talk(error_msg)

while True:
    run_dani()
