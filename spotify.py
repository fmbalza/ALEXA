from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import webbrowser as web
import pyautogui
from time import sleep
import speech_recognition as sr
import pyttsx3, pywhatkit


listener= sr.Recognizer()
engine  =pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():

    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            pc = listener.listen(source)
            rec= listener.recognize_google(pc, language='es-ES')
            rec = rec.lower(0)
    except:
        pass   

    return rec


cli_id = 'f36d715bd898423fb37c7aa878023b3e'
cli_scrt= '84643ddb657f46fbb07c33a049276f72'
flag = 0


author = ''
song = ''


def listenSong():
    global song
    talk("¿Que canción desea reproducir?")
    rec = listen()
    if "" in rec:
        song = rec.upper()
        empezar()
    else:
        pass

def empezar():
    global flag
    global song

    if len(author) > 0:
        # authenticate
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(cli_id, cli_scrt))
        result = sp.search(author)

        for i in range(0, len(result["tracks"]["items"])):
            # songs by artist
            name_song = result["tracks"]["items"][i]["name"].upper()

            if song in name_song:
                flag = 1
                web.open(result["tracks"]["items"][i]["uri"])
                sleep(5)
                pyautogui.press("enter")
                break



    if flag == 0:
        song = song.replace(" ", "%20")
        web.open(f'spotify:search:{song}')
        sleep(5)
        for i in range (8):
            pyautogui.press("tab")
        pyautogui.press("enter")


listenSong()




