import pyttsx3  #pip install pyttsx3
import speech_recognition as sr     #pip install speechRecognition
import datetime
import wikipedia    #pip install wikipedia
import webbrowser
import os
import smtplib
import wolframalpha     #pip install wolframalpha
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)  #prints the voice info and name of the voice (zira)
engine.setProperty('voice', voices[0].id)

client = wolframalpha.Client('api key')


def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 2 and hour < 12:
        speak("Good Morning !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !")

    elif hour >= 18 and hour < 20:
        speak("Good Evening!")

    else:
        speak("Good Night !")
    speak("I am Hailey, a virtual assistant at your service!")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your email id', 'your password')
    server.sendmail('your email id', to, content)
    server.close()

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 600
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except sr.UnknownValueError:
        speak('Sorry  didn\'t get that! Try typing that again')
        query = str(input('Command: '))
    return query

if __name__ == "__main__":
    wishMe()
    while True:

        #query = (str(input('Command: '))).lower()

        query = takeCommand().lower()

        if 'hello' in query or 'hey' in query or 'activate' in query:
            speak("Hello!, im Hailey at your service")

        elif 'who are you' in query or 'what is your name' in query:
            speak("Hi, I'm Hailey, the Virtual Assistant. ")

        elif 'who made you' in query:
            speak("I was made by team Blitz.")
       
        elif 'why were you made' in query or 'what purpouse do you serve' in query:
            speak("I was made to serve corporation with my skills of assistance for a better tomorrow of the mankind.")

        elif 'how old are you' in query or 'what is your age' in query:
            speak("I am just an infant! I have not yet completed 1 year.")

        elif 'i like you' in query:
            speak("Thats great! I like you too...")

        elif 'thank' in query:
            speak("No problem! Any time")

        elif "what are you doing" in query or 'what\'s going on' in query:
            stMsgs = ['Just doing my thing!', 'Time pass! What are you doing?','I am nice and full of energy for your querries!']
            speak(random.choice(stMsgs))

        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine! Thanks for asking.','Nice! How are you?', 'I am nice and full of energy!']
            speak(random.choice(stMsgs))

        elif 'you are good' in query or 'your good' in query:
            speak("Oh No! Dont praise me that much")

        elif 'open youtube' in query:
            speak("Opening Youtube!")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google!")
            webbrowser.open("google.com")

        elif 'open gmail' in query:
            speak("Opening G-mail!")
            webbrowser.open('www.gmail.com')

        elif 'open stack overflow' in query:
            speak("Opening stack-over-flow!")
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f",right now the time is {strTime}")

        elif 'open game loop' in query:
            codePath = "E:\\program files\\txgameassistant\\appmarket\\AppMarket.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            speak('Who is the recipient? ')
            recipient = (str(input('Command: '))).lower()
            if recipient:
                try:
                    speak('What should I say? ')
                    content = takeCommand()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("your email id", 'your password')
                    server.sendmail('youremail id', recipient, content)
                    server.close()
                    speak('Email sent!')
                except:
                    speak('Sorry ! I am unable to send your message at this moment!')

        elif 'shutdown' in query or 'bye-bye' in query or 'get lost' in query or 'stop' in query or 'shut down' in query or 'quit' in query or 'exit' in query:
            hour = int(datetime.datetime.now().hour)
            if hour >= 2 and hour < 18:
                speak("Have a nice day!Hope  to see you soon!")
            else:
                speak("Good night . Sweet dreams.")
            speak("Shutting Down...")
            quit()

        # Logic for executing tasks based on query
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Searching WOLFRAM-ALPHA...')
                    speak('According to WOLFRAM-ALPHA...')
                    speak(results)
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Searching Wikipedia...')
                    speak('According to Wikipedia...')
                    speak(results)
            except:
                webbrowser.open('www.google.com')

        anMsgs = ['Is there anything-else i can help you with!?', 'I am glad i could help you! So! Anything-else?.', 'Do you need anything-else?',
                  'Can i help you with anything-else?', 'Shooot at me if u have to know more?', 'If nothing more ! Say bye-bye !', 'You want me to search anything more?']
        speak(random.choice(anMsgs))
        # Logic for executing tasks based on query
        #if 'wikipedia' in query:
        #    speak('Searching Wikipedia...')
        #    query = query.replace("wikipedia", "")
        #    results = wikipedia.summary(query, sentences=2)
        #    speak("According to Wikipedia")
        #    print(results)
        #    speak(results)
