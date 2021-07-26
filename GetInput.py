import speech_recognition as sr
from googletrans import Translator

def GetInput(lan = "de-AT", dest = "en", lansource = "de"):

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak")
        audio = r.listen(source)
        text = (r.recognize_google(audio, language = lan))

    translator = Translator(service_urls=['translate.googleapis.com'])
    temp  = translator.translate(text, dest = "en", src = lansource)
    file = open("Input.txt", "w+")
    file.write(temp.text)
