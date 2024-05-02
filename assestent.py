                #############################################################################

import speech_recognition as sr
import win32com.client
import webbrowser

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(text):
    speaker.Speak(f"say{text}")

def takeCommand():
    r= sr.Recognizer() #it is a class
    with sr.Microphone() as source:  #Microphone is class too
       # r.pause_threshold = 1   #it is for how much it is listning
        audio = r.listen(source)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio,language="en-in")
            print(f"User said:{query}")
            return query
        except Exception as e:
            return "Some error occured"

if __name__ =='__main__':
    print('Assistant')
    say("Hello how may i help you")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube","https://youtube.com"],["google","https://google.com"],
                ["wikipedia","https://wikipedia.com"],["Clock","https://www.timeanddate.com/worldclock/"],
                ["music","https://open.spotify.com/?"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                 say(f"Opening{site[0]}...")
            if f"play {site[0]}".lower() in query.lower():
                 say(f"Opening{site[0]} ...")
                 webbrowser.open(site[1])
