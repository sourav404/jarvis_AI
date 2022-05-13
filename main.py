import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import win32gui, win32con
from youtubesearchpython import VideosSearch



wind = win32gui.GetForegroundWindow()

edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# print(voices)
# for male
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)
# Set Volume
engine.setProperty('volume', 1.0)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# resive commends 
def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")

        return "None"
    return query








# Wish me 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am jenni Sir. Please tell me how may I help you")



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query or 'what is' in query or 'who is' in query:
            print('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("sir,")
            print(results)
            speak(results)

        elif 'exit' in query:
            speak("Thank You sir good bye.")
            exit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I %M %p").replace('0', ' ')
            print("Time : "+strTime)

            speak(f"Sir, the time is {strTime}")

        elif 'open google' in query:
            speak('opening google.')
            webbrowser.get('edge').open('http://www.google.com')

        elif 'search' in query or 'on google' in query:
            query = query.replace("search", "")
            query = query.replace("google", "")
            webbrowser.get('edge').open('http://www.google.com/search?q='+query)
            speak('Searching.')

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.get('edge').open('http://www.youtube.com')

        elif 'my channel' in query or 'my youtube channel' in  query or 'youtube studio' in query:
            webbrowser.get('edge').open('https://studio.youtube.com/')
            speak('Sir, this is your Youtube channel Dashbord')

        elif 'open facebook' in query:
            speak('opening facebook')
            webbrowser.get('edge').open('http://www.facebook.com')

        elif 'open instagram' in query:
            speak('opening instagram')
            webbrowser.get('edge').open('http://www.instagram.com')

        elif 'open freelancer.com' in query or 'open freelancer' in query:
            speak('ok sir, i opening freelancer site')
            webbrowser.get('edge').open('http://www.freelancer.com')

        elif 'minimise' in query or 'window hide' in query:
            speak('ok sir')
            win32gui.ShowWindow(wind, win32con.SW_MINIMIZE)

        elif 'maximize' in query or 'window show' in query:
            speak('sure.')
            win32gui.ShowWindow(wind, win32con.SW_MAXIMIZE)

        elif 'play' in query or 'song' in query:
            query = query.replace("play", "")
            query = query.replace("song", "")
            query = query.replace("search", "")
            query = query.replace("youtube", "")
            query = query.replace("search", "")
            query = query.replace("on", "")
            videosSearch = VideosSearch(query, limit = 1)
            yt = videosSearch.result()['result'][0]['link']
            webbrowser.get('edge').open(yt)


