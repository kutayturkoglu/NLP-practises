from nltk.tokenize import word_tokenize
import nltk
import json
import re

def WordCount(language = "english", inp = "Input.txt", out = "WordCounts.txt"):
    
    Input = open(inp, "r").read().lower()
    Text = word_tokenize(Input)
    
    stopwords = nltk.corpus.stopwords.words(language)   
    Text = [word for word in Text if word not in stopwords]

    for i in range(len(Text)):    
        Text[i] = re.sub("[^A-Za-z]","",Text[i])
    
    Counter = {}
    for word in Text:
        if word == "": continue
        elif word in Counter: Counter[word] += 1
        else: Counter[word] = 1
    CommonWords = {k:v for k, v in sorted(Counter.items(), key = lambda item: item[1], reverse = True)}

    with open(out, "w") as file:
        file.write(json.dumps(CommonWords))

