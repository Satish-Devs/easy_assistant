import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice','english-north' )


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ''

    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            command = command.lower()
            print("You :"+command)
            if 'xavier' in command:
                command = command.replace('xavier','')
                print(command)
       
        

    except Exception as e:
        print(e)
    
    return command

   

def run_xavier():
    command = take_command()
    if 'type and play' in command:
        command = input()
        pywhatkit.playonyt(command)
        talk('playing '+command)

    elif 'play' in command:
        song = command.replace('play','')
        talk('playing ' +song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    
    elif 'date' in command:
        talk('Sorry, I have a headache')
    
    elif 'are you single' in command:
        talk('Iam in a relationship with wifi')
    
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    
    

    elif(command==' stop'):
        sys.exit(0)

    elif(len(command)>0):
        talk('Please say the command again...')
    
    
    
   


while True:
    run_xavier()