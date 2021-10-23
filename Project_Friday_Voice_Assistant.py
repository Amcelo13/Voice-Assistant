import pyttsx3   #Module for text-to-speech conversion 
import speech_recognition as sr
import datetime
import wikipedia      #To get wikipedia ans 
import webbrowser     #To open a website in browser
import os
import smtplib        #To send gmails
import pywhatkit      #To send whatsapp text
                          # Voice Setting of the JARVIS
engine = pyttsx3.init('sapi5')           #This sapi5 is for initialising Mic. windows to load voice present in it.
voices  = engine.getProperty('voices')   #This is to get the available voices in OS o 
print(voices[0].id ,voices[1].id)
engine.setProperty('voice', voices[0].id)   #Setting one of the available voices from the windows say ->Male one that is first voice at index voices[0].id


def speak(audio):       
    """Function for output of Jarvis voice"""
    engine.say(audio)    
    engine.runAndWait()  #Without this command, speech will not be audible to us.

def wishme():
    print('<----------------------------------WELCOME BOSS------------------------------>')    
    hour = int(input(datetime.datetime.now().hour))     #We get hour(0 -24) in int typecasted
    if hour >= 0 and hour < 12:
        speak('Morning Bruh')
    elif hour >=12 and hour <18:
        speak('Afternoon Buddy') 
    else:
        speak('Good evening bruh!')
    speak('I am Jarvis ! Please tell what I can do for you')

def takeCommand():
    """It takes mic voice as input from the user and returns a string """

    r = sr.Recognizer()     #It is helpful for the recognition of input voice of the user
    with sr.Microphone() as source:
        print('Listening....!')
        r.pause_threshold = 1      #Means it takes 1 sec of non-speaking audio before a phrase is considered complete.
        audio = r.listen(source)    #It will listen user's voice and stores the voices in variable named 'audio'
    try:
        print('Recognizing...!')
        query = r.recognize_google(audio, language='en-us')     #It will store the string converted(by google_recognizer) ,from voice variable->'audio'
        print('User said :', query ,'\n')

    except Exception as e:
        # print(e)
        print('Say that again.........!')
        return "None"    

    return query   

def send_Email(recipient_ ,content):
    server = smtplib.SMTP('smtp.gmail.com' ,587)
    server.ehlo()
    server.starttls()
    server.login('tchetan308@gmail.com' ,'abcd_your_pass')
    server.sendmail('tchetan308@gmail.com' , recipient_ ,content)
    server.close()

if __name__ == '__main__':
    # speak('Chetelise is from ,California, USA')

    wishme()
    while(True):          #So that it will keep listening again and again until we tell it to stop..
        #query is a voice input by the user
       query = takeCommand().lower()    #Calling the takeCommand/listening function with lower caps so the commands/if else statemnents we can match with lowercase.

       if 'wikipedia' in query:       #Means if we spoke as a input has wikipedia in it then if statement starts
           print('Searching Wikipedia........!')
           query = query.replace("wikipedia", "")          #Replacing/removing wikipedia in the query we said in mic to none so that it can search for topic without including word wikipedia in it
           results = wikipedia.summary(query ,sentences = 1)
           speak('According to Wikipedia ')
           print(results)
           speak(results)

       elif 'open youtube' in query:
            speak('Opening Youtube')
            webbrowser.open("youtube.com")

       elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open("google.com")
               
       elif 'open stackoverflow' in query:
            speak('Opening Stackoverflow')
            webbrowser.open("stackoverflow.com")

       elif 'play music' in query:
            music_dir = 'D:\\Video'
            musics = os.listdir(music_dir)  #It prints the list of files/music in this directory
            print(musics)   
            os.startfile(os.path.join(music_dir ,musics[0]))    #This line will start/open the first file/song in the list musics

       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")      #This will store the current time in hrs:min:sec as a string in strTime
           speak(f'Sir the time is : {strTime}')

       elif 'open telegram' in query:
            tel_path = '"C:\\Users\\lenovo\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"'
            speak('Opening the Telegram')
            os.startfile(tel_path)    #Directly as tel_path is a target link

       elif 'email to chetan' in query:
           try:
               speak('What should I say ?')
               content = takeCommand()
               recipient_ = 'tchetan308@gmail.com'
               send_Email(recipient_ ,content)
               speak('The email has been sent')
           except Exception as e:
               print(e)
               speak('Sorry Sir! I am unable to send it right now!')   

       elif 'whatsapp to sanchit' in query:
               print('What should i text')
               speak('What should I text')
               text_to_send = takeCommand().lower()
               print('Sending the Message!')
               speak('Sending the message')
               txt_recipient = '+911233333333'
               pywhatkit.sendwhatmsg(txt_recipient , text_to_send, 14 , 31) #Last two arg are hrs,min
               speak('Message will be sent!')

       elif 'change your voice' in query:
              engine.setProperty('voice' ,voices[1].id)
              print('Voice changed successfully')
              speak('This is the new voice!')

       elif 'quit' in query:
           speak('Bye Sir! See you next time')
           exit()      