from flask import Flask, render_template
import requests
import json
import speech_recognition as sr
import pyttsx3
import gtts
from playsound import playsound
import os
import glob 
 


listener = sr. Recognizer()
#to adjust microphone sensitivity
listener.energy_threshold = 4000
listener.dynamic_energy_threshold = True
engine = pyttsx3.init()


def talk(text,id):
    if id == 15:
        print("repeat yourself")
    tts = gtts.gTTS(text)
    tts.save(f"./oro/t-hello{str(id)}.mp3")
    playsound(f"./oro/t-hello{str(id)}.mp3")
    


def take_command():
    try:
        print("entered.df")
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("listening...")
            playsound("listening.mp3")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "Daniel" in command:
                command = command.replace("bibot","")
                print(command)
        print("entered")
        return(command)
    except Exception as e:
        print(e)
        pass

book = ""
verse = ""
url = "http://getbible.net/json?passage="
# added for python applications
end = "&raw=true"



def specific_bible(globalArr):
    command = take_command()
    print(command)
    if "hello" in command:
        globalArr.append("User:"+command)
        talk("Hi! I’m bibot, a bible bot designed to cater to your biblical needs.",2)
        globalArr.append("Hi! I’m bibot, a bible bot designed to cater to your biblical needs.")
        print("Hi! I’m bibot, a bible bot designed to cater to your biblical needs.")

    global book
    try:
        talk("WHAT BOOK IN THE BIBLE ARE YOU LOOKING FOR? ",3)
        globalArr.append("Bi-Bot:"+"what book in the bible are you looking for")
        print("what book in the bible are you looking for")
        book= take_command().lower()
        print(book)
        globalArr.append("user:"+book)
       
        talk("WHAT CHAPTER ARE YOU LOOKING FOR? ",4)
        globalArr.append("Bi-Bot:"+"WHAT CHAPTER ARE YOU LOOKING FOR? :")
        print("WHAT CHAPTER ARE YOU LOOKING FOR? :")
        chapter= take_command().lower()
        print(chapter)
        globalArr.append("user:"+chapter)
        

        talk("WHAT VERSE ARE YOU LOOKING FOR? ",5)
        globalArr.append("Bi-Bot:"+"WHAT VERSE ARE YOU LOOKING FOR? ")
        print("WHAT VERSE ARE YOU LOOKING FOR? ")
        verse= take_command().lower()
        print(verse)
        globalArr.append("user:"+verse)

        talk("You asked for: "+book+" chapter: "+chapter+" verse: "+verse,75)
        globalArr.append("You asked for: "+book+" chapter: "+chapter+" verse: "+verse)

        url_response = url + book + chapter + ":" + verse +end + "&version=kjv"
        response = requests.get(url_response).json()
        verse_upper = response["book"][0]["chapter"]
        verse_lower = verse_upper[verse]["verse"]
        print(verse_lower)
        globalArr.append(verse_lower)
        talk(verse_lower,6)
        return 1234
        
    except KeyError:
        talk("I THINK YOU SPELLED THE WRONG BOOK,LET'S TRY THIS AGAIN",7)
        print("I THINK YOU SPELLED THE WRONG BOOK, LET'S TRY THIS AGAIN")
    except json.decoder.JSONDecodeError:
        talk("There's not that many chapters in" + book + ".",8)
        print("There's not that many chapters in " + book + ".")


def auto():
    conversation_length = 5
    globalHistory = []
    while conversation_length != 1234:
        try:
            files = glob.glob('./oro/*') 
            for f in files: 
                os.remove(f)
            print("conversation_length is remaining ", conversation_length)
            # Run_Troy(globalHistory)
            conversation_length= specific_bible(globalHistory)
            # conversation_length -=1
            print(conversation_length)
        except Exception as e:
            print(e,'this is the error')
        # print("conversation_length is remaining ", conversation_length)
        # # Run_Troy(globalHistory)
        # specific_bible(globalHistory)
        # conversation_length -=1
    return globalHistory

# auto()


