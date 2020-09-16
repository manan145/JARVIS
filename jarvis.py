import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening')
        
    speak('Hello sir! How may I help you?')    
    
def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print('Recognizing...')
        query = r.recognize_google(audio)
        print("User said : ",query)
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"  
    return query   
    

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('mananjagani145@gmail.com','gqxiivhozwrlibnp')
    server.sendmail('mananjagani145@gmail.com',to, content)
    server.quit()
    
if __name__ == "__main__":
    
    d = {
        'charvi' : 'jaganicharvi@gmail.com',
        'manan' : '201901295@daiict.ac.in',
        'ayush' : '2512ayush@gmail.com',
        'dad' : 'jaganiashwin@gmail.com'
    }
    
    wishMe()
    while True:
        query = takeCommand().lower()
    
        # logic for executing tasks
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S:")
            speak(f"sir, the time is {strTime}")
            
        elif 'open code' in query:
            codePath = "C:\\Users\\manan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
        elif 'send email' in query:
            try:
                speak("To whom do you want to send an email")
                name = takeCommand().lower()
                to = d[name]
                speak("What should i say?")
                content = takeCommand()
                sendEmail(to, content)
                speak(f"Email has been sent to {name}!")
            except Exception as e:
                print(e)
                speak('Sorry sir i am unable to send this email')
                
                
            