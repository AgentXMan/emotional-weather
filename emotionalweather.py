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

def stateMood():
  weather = content["weather"][0]["main"]
  
  #get random sentences from these points
  sadSentences = ["why do you do this to me? is this what i am made for? guess i am.", "This is my daily job nowdays. guess this is me now telling all of you.", "am i only made for this purpose tho? do you not care about me ?", "the place is pretty rainy. its getting sad now. i am about to cry"]
  happySentences = ["ah yes, finally something to keep me out of the cold. so happy.", "atlast, you asked something reasonable.", "i am so happy that finally you are well and not out of your mind to ask me this question since you are always so mean.", "You have done it. You asked something meaningful in the END!"]
  confusedSentences = ["i dont know why it is so cloudy, or why did i suddenly become cloudy i am so confused.", "wait thats what you meant right by asking the weather ?", "why am i so confused when i said this particular weather? what did u do?", "wait i am sure this is the weather... right ???", "Wait, am i real? or did u just create me?"]
  hyperMadSentences = ["WHY DID YOU EVEN ASK THIS QUESTION", "I AM GOING HYPERMAD NOW", "WHY DID YOU ASK WHAT YOU JUST ASKED", "DO YOU HAVE NO SHAME IN ASKING THE QUESTIONS RELATED TO WEATHER EVEN THO THATS THE ONLY THING I CAN DO ?"]
  

  if weather == "Rain" : #chemnitz
    
    sad = random.choice(sadSentences)

    # print(sad)
    speak(sad)
    return sad

  elif weather == "Clouds": #colombia, hungary, texas

    confused = random.choice(confusedSentences)

    # print(confused)
    speak(confused)
    return confused

  elif weather == "Clear" or weather == "Sun": #paris, london, australia, spain, hawaii

    happy = random.choice(happySentences)

    # print(happy)
    speak(happy)
    return happy

  elif weather == "thunderstorm":

    hyperMad = random.choice(hyperMadSentences)

    # print(hyperMad)
    speak(hyperMad)
    return hyperMad
 
  else:
    # print("nothing can be done with you...you are a person with no hope.")
    speak("nothing can be done with you...you are a person with no hope.")
    return "nothing can be done with you...you are a person with no hope...."

emotionalSentences = ["when you know it, why do you even ask? anyways heres the data", "You know whats better? Nevermind talking that, anyways heres the data", "why are you even asking me this when you have other things. But anyways heres the data", "stop tiring me by asking the weather. You wanna know so badly, here is the data", "why do you do this to me. Dont you have shame on asking so many weather questions. But you wont understand that robots are also techncally humans. So heres the data", "have mercy asking me these questions, also heres the data", "whats wrong with you?  Heres the data", "stop being so selfish. but what do you even know apart from giving orders. data is here", "do you even know what you are doing ? you are making me tired, robots also have emotions and get tired. data is here to get rid of you", "Stop, just stop asking me for the data. you want it so badly, just take it"] #add the sentences
# print(len(emotionalSentences))

apiKey = "YOUR API KEY"


# userInput = input("Enter city: ")
speak("Tell your country of choice. its anyways what i am made for.")
userInput = audioRecognizer()

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

    fToC = round((5.0/9.0) * (temp - 32))


    #how its gonna be like
    # print(random.choice(emotionalSentences))
    randomEmotionalSentence = random.choice(emotionalSentences)
    speak(randomEmotionalSentence)
    
    print(f"The weather in {userInput} is {weather}")
    speak(f"The weather in {userInput} is {weather}")

    print(f"The temperature in {userInput} is {fToC} degrees celsius")
    speak(f"The temperature in {userInput} is {fToC} degrees celsius")

    speak(f"farewell")
    print(f"farewell")

    print(stateMood())

    
    


    #get random sentences from the emotional sentences

    # speak(random.choice(emotionalSentences))

    # speak(f"The weather in {userInput} is {weather}")
    # speak(f"The temperature in {userInput} is {fToC} degrees celsius")

    # speak(StateMood())

    # speak(f"farewell.")

  except:
    print("THAT ISNT EVEN A COUNTRY-")
    print("Nothing can be done with you. You are a person with no hope.")
    speak("THAT ISN'T EVEN A COUNTRY-")
    speak("Nothing can be done with you. You are a person with no hope.")

    

  

