from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sent_tokenize

def StartSentiment(inp = "Input.txt", out = "SentimentOutput.txt"):
    Text = open(inp, "r").read().lower()
                                                       
    open(out, "w")
    Analyzer = SentimentIntensityAnalyzer()
    Analyzed = Analyzer.polarity_scores(Text)
    SentimentOutput = open(out, "a")                      
    SentimentOutput.write("General Summary: " + str(Analyzed) + "\n\n")
    
    Text = sent_tokenize(Text)
    Analyzed1 = {}
    for i in range(len(Text)):
        Analyzed1[Text[i]] = Analyzer.polarity_scores(Text[i])
        
    SentimentOutput = open(out, "a")
    for key in Analyzed1:
        SentimentOutput.write(str(key) + str(Analyzed1[key]) + "\n\n")

