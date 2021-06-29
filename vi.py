import pyttsx3  #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia   #pip install wikipedia
import webbrowser
import os
import smtplib   
from  requests import  get 
import  pywhatkit as kit    #pip install pywhatkit
import pyautogui    #pip install PyAutoGUI
import requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
import psutil   #pip install psutil
import speedtest  #pip install speedtest-cli




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Zara Mam. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('anujasawant154@gmail.com','anuja@1234')
    server.sendmail('anujasawant154@gmail.com',to,content)
    server.close()

def news():
    main_url="https://newsapi.org/v2/everything?q=tesla&from=2021-02-28&sortBy=publishedAt&apiKey=19c349064ccf46e89dd49f4782d36439"
    main_page=requests.get(main_url).json()
    articles=main_page["articles"]
    head=[]
    day=["first","second","third","fourth","fifth","sixth","seventh","eight","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        print(f"todays {day[i]} news is :{head[i]}")
        speak(f"todays {day[i]} news is: {head[i]}")



if __name__ == "__main__":

    wishMe()

    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # To open youtube.
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        # To open google.
        elif 'open google' in query:
            speak("Mam, what should i search on google")
            cm=takeCommand().lower()
            webbrowser.open(f"{cm}")

        # Open the notepad.
        elif 'open notepad' in query:
            path="C:\\Windows\\system32\\notepad.exe"
            os.startfile(path)

        # to get the current time.
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Mam, the time is {strTime}")

        
        # send email.
        elif 'email to anuja' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "anujasawant387@gmail.com" 
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry But I am not able to send this email")    

        # to find an ip address.
        elif  'ip address' in query:
            ip=get('https://api.ipify.org').text
            speak(f"Your IP address is{ip}")
            print(ip)

        # to exit.
        elif 'exit' in query:
            ex_exit='See you soon. Bye'
            speak(ex_exit)
            exit()
        
        # send whatsup message.
        elif 'send message' in query:
            kit.sendwhatmsg("+917045874484","hello! i am Programmer.",8,32)
            speak("message has been send.")
        
        # play songs on youtube.
        elif 'play songs on youtube' in query:
            kit.playonyt("see you again")

        # To get daily news.

        elif 'tell me news' in query:
            speak("Please wait mam, fetching the latest news")
            news()

        # To switch window

        elif 'switch window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        #To find the location. 

        elif 'where i am' in query or "where we are" in query:
            speak("wait mam,let me check")
            try:
                ipAdd=requests.get('https://api.ipify.org').text
                print(ipAdd)
                url='https://get.io/v1/ip/geo/'+ipAdd+'.json'
                geo_requests=requests.get(url)
                geo_data=geo_requests.json()
                city=geo_data['city']
                state=geo_data['state']
                country=geo_data['country']
                speak(f"Mam i am not sure, but i think we are in {state} state of {city} city in  {country} country")
            except Exception as e:
                speak("Sorry mam, Due to network issue i am not able to find.")  
                pass      

        # To check instagram profile

        elif 'instagram profile' in query:
            speak("Mam please enter the username correctly. ")
            name=input("Enter username:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak("Mam, here is profile of user {name}")
            condition=takeCommand().lower()


        

        # To take screenshot

        elif 'take screenshot' in query:
            speak("Mam , tell me the name name for screenshot file")
            name=takeCommand().lower()
            speak("please mam hold the screen for few seconds, i am taking screenshot")
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("mam , i have taken screenshot saved in our main folder")

        # To check the weather condition

        elif 'temperature' in query:
            weather="temperature in mumbai"
            url=f"https://www.google.com/search?q={weather}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text
            speak(f"current {weather}  is {temp}")
            print(f"current {weather} is {temp}")

        # To check battery percentage 

        elif 'how much battery' in query:
            battery=psutil.sensors_battery()
            percentage=battery.percent
            speak(f"Mam our system have {percentage} percent battery.")
            if percentage>=75:
                speak("we have enough battery to continue our work")
            elif percentage>40 and percentage<=75:
                speak("we should connect our system to charging point to charge our battery.")
            elif percentage<=15 and percentage<=30:
                speak("we don't have enough battery , please connect to charge")
            elif percentage<=15:
                speak("we have very low battery, please connect charging system will shutdown soon.")

        # To check internet speeed.
        
        elif 'internet speed' in query:
            st=speedtest.Speedtest()
            d1=st.download()
            up=st.upload()
            speak(f"Mam we have {d1} bit per second downloading speed and {up} bit per second uploading speed.")





        
            


        


