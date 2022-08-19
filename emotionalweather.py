'''
made by Basic Code (me) aka AgentXMan
https://youtu.be/u5Pqa7X6SvI
'''

import requests
import json
import pyttsx3
import random
import speech_recognition as sr

def speak(TextToSay):
  engine = pyttsx3.init()
  voices = engine.getProperty("voices")

  engine.setProperty("rate", 150)

  engine.setProperty("voice", voices[1].id)
  engine.say(TextToSay)
  engine.runAndWait()

def audioRecognizer():
  r = sr.Recognizer()

  with sr.Microphone() as source:
    audio = r.listen(source)

    said = ""

    try:
      said = r.recognize_google(audio)

      print("-------")
      print(said)
      print("-------")

    except Exception as e:
      print("you didnt say anything, pls restart and say something ", e)

  return said

#chooses from this variety. will work on this to randomize even further
emotionalSentences = ["when you know it, why do you even ask? anyways heres the data", "You know whats better? Nevermind talking that, anyways heres the data", "why are you even asking me this when you have other things. But anyways heres the data", "stop tiring me by asking the weather. You wanna know so badly, here is the data", "why do you do this to me. Dont you have shame on asking so many weather questions. But you wont understand that robots are also techncally humans. So heres the data", "have mercy asking me these questions, also heres the data", "whats wrong with you?  Heres the data", "stop being so selfish. but what do you even know apart from giving orders. data is here", "do you even know what you are doing ? you are making me tired, robots also have emotions and get tired. data is here to get rid of you", "Stop, just stop asking me for the data. you want it so badly, just take it"] #add the sentences
# print(len(emotionalSentences))

apiKey = "your api key"

userInput = input("Enter city: ")
# speak("Tell your country of choice. its anyways what i am made for.")
# userInput = audioRecognizer()

responseWeatherData = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={userInput}&units=imperial&APPID={apiKey}")
# print(responseWeatherData)

content = responseWeatherData.json()
# print("--------------------\n", content)


if content["cod"] == 404:
  print("No city found")

else:
  #just formatting json in a better way
  with open("WeatherJson", "w") as f:
    json.dump(content, f, indent = 2)

  try:
    weather = content["weather"][0]["main"]
    temp = round(content["main"]["temp"])

  except:
    print("THAT ISNT EVEN A COUNTRY-")
    # speak("THAT ISNT EVEN A COUNTRY")

  fToC = round((5.0/9.0) * (temp - 32))


  # print(random.choice(emotionalSentences))
  print(f"The weather in {userInput} is {weather}")
  print(f"The temperature in {userInput} is {fToC} degrees celsius")

  #get random sentences from the emotional sentences

  # speak(random.choice(emotionalSentences))
  print(random.choice(emotionalSentences))

  # speak(f"The weather in {userInput} is {weather}")
  # speak(f"The temperature in {userInput} is {fToC} degrees celsius")
  # speak(f"farewell.")
  print("farewell")
