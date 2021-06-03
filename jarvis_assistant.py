import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


# defining the engine function
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')   # fetches the available voices in this device
engine.setProperty('voice', voices[1].id)  # we are going to use the microsoft Zira as our assistant's voice
# print(voices[1].id)


# defining the speak function\
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# defining wishMe function
def wishMe():
    hour = int(datetime.datetime.now().hour)

    # running the loop function for whishing

    if 0<=hour>12:
        print("Good Morning")
        speak("Good Morning")

    elif 12<=hour>18:
        print("Good Afternoon")
        speak("Good Afternoon")

    else:
        print("Good Evening")
        speak("Good Evening")

    speak("I am your personal assistant so tell me how can i help you")

# defing the function to take all the commands

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...........")
        r.pause_threshold = 1
        audio = r.listen(source)

    # try and except will be better as it will not throw the error to stop the program
    try:
        print("Recognising the text..............")
        query = r.recognize_google(audio, language='en-in')  # google is beeteer fo audio enhancements
        print(f"You Said: {query}/n")

    except Exception as e:
        # print(e)
        print("Say again please: ")
        return "None"

    return query

#now let's create the sendMail function for sending emails
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) # 587 is the port no.
    server.ehlo()
    server.starttls()
    server.login('enteryouremail@gmail.com', 'enter your password')
    server.sendmail('enteryouremail@gmail.com', to, content)
    server.close()

# defing the main funtion unde which all our defined functions will work

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'hello' in query:
            print("heey bro")
            speak("heey bro")

        elif 'how are you' in query:
            print("i am fine bro")
            speak("i am fine bro")

        elif 'wikipedia' in query:
            speak("Seraching wikipedia........")
            query = query.replace("wikipedia", " ")
            # semtences are use to print or speak the jno of line that the user wants
            results = wikipedia.summary(query, sentences = 1)
            speak("According to wikipedia.........")
            print(results)
            speak(results)

        elif 'google'in query:
            speak("opening google")
            webbrowser.open("google.com")

        elif 'youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'play song' in query:
            music_directory = "C:/Users/LITU_LISA_SAI/Documents/music_directory"
            songs = os.listdir(music_directory)
            print(songs)
            os.startfile(os.path.join(music_directory, songs[0]))

        elif 'show me time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"the time is {strTime}")

        elif 'thank you' in query:
            print("welcome")
            speak("you are welcome")

        elif 'open mail' in query:
            speak("opening mail")
            webbrowser.open("you email link")

        elif 'email me' in query:
            try:
                speak("enter the text")
                content = takeCommand()
                to = "your email"
                sendEmail(to, content)
                speak("your email has been sent")

            except Exception as e:
                print(e)
                speak("Sorry could'nt transfer your mail")

        elif 'exit' in query:
            print("bye bye")
            speak("bye bye")
            exit()

# SO OUR PROJECT JARVIS IS COMPLETE NOW SO LET'S TEST IT OHK