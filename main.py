# importing the prequistes
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import eel
# setting up eel
eel.init("web")

# initializing voice engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")


# assigning global variables per user requirement
userName = ""
assistantName =""
salutation = ""
browser_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

def setup():
    global userName
    global assistantName
    global salutation
    fileObj= open("setup.txt","r")
    config_ = fileObj.read()
    # print(config_)
    config1 = config_.split(",")
    # print(config1)
    userName = config1[0]
    assistantName = config1[1]
    engine.setProperty("voice", voices[int(config1[2])].id)
    salutation = config1[3]
    engine.setProperty("rate", config1[4])
    eel.nameSetter(userName, assistantName)
    fileObj.close()

# defining primary speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# defining secondary functions
def wish():
    hour =int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak(f"Good morning ,{salutation}")
    elif hour >= 12 and hour <= 18:
        speak(f"Good afternoon ,{salutation}")
    elif hour >= 18 and hour <= 24:
        speak(f"Good evening,{salutation}")

    speak(f"I am {assistantName}. How can I help you today")

def listen():
    # taking input from microphone
    input_voice = sr.Recognizer()
    with sr.Microphone() as source:
        input_voice.adjust_for_ambient_noise(source)
        eel.currentStatus("listening..")
        # print("listening..")
        input_voice.pause_threshold = 0.8
        # input_voice.energy_threshold = 800
        audio = input_voice.listen(source)
        # print("listening done")
        eel.currentStatus("listening done..")
        

    try:
        eel.currentStatus("recognizing..")
        query = input_voice.recognize_google(audio, language='en-in')
        eel.currentStatus(f"{query}")
        eel.currentStatus("Ready")

    except Exception as e:
        print(e)
        # print("Didnt recognize that , please say that again")

        return "None"
    return query

@eel.expose
def starter():
    setup()
    wish()

@eel.expose
def opener():

    os.startfile("setup.py")

# main function
@eel.expose
def assistant():

    query = listen()
    query = query.lower()
    #query processing
    if "wikipedia" in query:
        query = query.replace("wikipedia", "")
        speak(f"Searching {query}")
        result = wikipedia.summary(query, sentences=3)
        speak(f"According to wiki ")
        speak(result)

    elif ".com" in query:
        query = query.replace("open", "")
        query = query.strip()
        speak(f"Opening {query}")
        webbrowser.get(browser_path).open(f"{query}")
    elif "play" in query:
        try:
            music_path = f"{os.getcwd()}\\music"
            query1=query.replace("play", "")
            query1 = f"{query1.strip()}.mp4"
            os.startfile(os.path.join(music_path,query1))
            speak(f"playing {query1}")
        except Exception as e:
            music_path = f"{os.getcwd()}\\music"
            query = query.replace("play", "")
            query = f"{query.strip()}.mp3"
            os.startfile(os.path.join(music_path, query))
            speak(f"playing {query}")

    elif "shutdown" in query:
        speak("Shutting down your system, Have a nice day!")
        os.system("shutdown /s /t 1")



    elif "restart" in query or "reboot" in query:
         speak("Rebooting your System")
         os.system("shutdown /r /t 10")

    elif "open" in query:
        try:
            appPath = f"C:\\Users\\{os.getlogin()}\\OneDrive\\Desktop"
            query = query.replace("open", "")
            query = query.strip()
            # print(os.path.join(appPath,f"{query}.lnk"))
            os.startfile(os.path.join(appPath,f"{query}.lnk"))
            speak(f"opening {query}")
        except Exception as e:
            appPath = f"C:\\Users\\Public\\Desktop"
            query = query.replace("open", "")
            query = query.strip()
            # print(os.path.join(appPath, f"{query}.lnk"))
            os.startfile(os.path.join(appPath, f"{query}.lnk"))
            speak(f"opening {query}")

    elif "time" in query:
        speak(datetime.datetime.now().strftime('%I:%M:%p'))

    elif "day" in query or "date" in query:
        now = datetime.datetime.now()
        speak(now.strftime("%d:%B:%Y"))
    elif "exit" in query or "quit" in query:
        speak("Exiting Now , Thank you and have a nice day")
        eel.closeWin()
        exit()
    elif "in youtube" in query  :
        query = query.replace("in youtube", "")
        query = query.replace("search", "")
        # query = query.strip()
        speak(f"Searching {query} in youtube")
        query = query.replace(" ", "+")
        youTube = "https://www.youtube.com/results?search_query="
        
        webbrowser.get(browser_path).open(youTube+query)

    elif "on youtube" in query  :  #not a good way to distinguish between in and or , will fix it later
        query = query.replace("on youtube", "")
        query = query.replace("search", "")
        speak(f"Searching {query} on youtube")
        # query = query.strip()
        query = query.replace(" ", "+")
        youTube = "https://www.youtube.com/results?search_query="
        # speak(f"Searching {query} in youtube")
        webbrowser.get(browser_path).open(youTube+query)
    elif "system sleep" in query:
        speak(f"Good night {salutation}")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif "none" in query:
        eel.currentStatus("Error, Try Again")
        speak("Sorry I did'nt recognized what you've said ,please try again and if the error persists contact Mr. Dev at devsinghparihar10@gmail.com")
    else:

        query= query.replace(" ", "+")
        google = "https://www.google.com/search?q="
        webbrowser.open(google+query)
        speak("Sorry I didn't understand , But here are the results from the web")



# firing eel
if __name__ == '__main__':
    starter()
    eel.start("index.html")

"""Things left to do
1 add voice to every function ,done
2 add music .mp3 compaitability to play, done 
3 fix browser path issues  ,collison
4 bind with gui ,collision enchancement required 
5 add - who are you , what can you do , i love you , chatbox , pending for 4.x
6 pywhatkit for email and whatsapp functionality
7 add google search (search in google )"""
