from googletrans import Translator

def Translate():
    file = input("Please enter the name of the file that you want to translate: ")
    text = open(file, "r").read()
    translator = Translator(service_urls=['translate.googleapis.com'])
    temp  = translator.translate(text, dest = "en", src = "de")
    file = open("Input.txt", "w+")
    file.write(temp.text)
