import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import google.generativeai as genai
import pygame
import os

recognisior = sr.Recognizer()
engine = pyttsx3.init()
newsapi="db06203e6a6640709b142971b132c02f"
def aipower(command):
    genai.configure(api_key="AIzaSyCGx0rkrZ_1-JCFOcvDFUAM2q7BLe8sZ4E")

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(command)
    return (response.text)

def speak(text):
    engine.say(text)
    engine.runAndWait()


        
def pocessCommand(c):
    if "open google" in c.lower():
        speak("opening google sir")
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        speak("opening youtubr sir")
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        speak("opening instagram sir")
        webbrowser.open("https://instagram.com")
    elif "open facebook" in c.lower():
        speak("opening facebook sir")
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song= c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        speak(f"Playing {song} song sir")
        webbrowser.open(link)
    elif "news" in c.lower():
        url="https://newsapi.org/v2/top-headlines?country=us&apiKey=db06203e6a6640709b142971b132c02f"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()  # Convert the response to JSON format
            articles = data.get("articles", [])  # Get the list of articles

    # Loop through each article and print the headline
        for article in articles:
            speak(article['title'])  # Replace `print` with `speak` if you have a `speak` function defined
        else:
            print("Failed to retrieve news. Status code:", r.status_code)
    else:
        output=aipower(c)
        # speak(f"i will try to find your query about, {c}")
        noutput=output.replace("*","")
        speak("I got it")
        speak(noutput)




    
    



if __name__ == "__main__":
    speak("Initialize Friday")
    pygame.mixer.init()
    pygame.mixer.music.load("initia-[AudioTrimmer.com].mp3")
    pygame.mixer.music.play()
    
    #listen for the wake jarvis
    while(True):

        # obtain audio from the microphon

        # recognize speech using Sphinx
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening.....")
                audio = r.listen(source,timeout=4,phrase_time_limit=3)
            word = r.recognize_google(audio)
            # print(type(word))
            if(word.lower()=='friday'):
                speak('ya my king')
                #listen for command
                with sr.Microphone() as source:
                    print("friday active.....")
                    audio = r.listen(source,timeout=4,phrase_time_limit=3)
                    command = r.recognize_google(audio)

                    pocessCommand(command)
            
        except Exception as e:
            print("Error; {0}".format(e))
