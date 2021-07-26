from Sentiment import StartSentiment
from WordCounter import WordCount
from Translate import Translate
from GetInput import GetInput
from KeyWord import Keyword
from KeyWord import Erase
import argparse

parser = argparse.ArgumentParser(
"""
To run the commands write Main.py 'operation' for the unique operation \n
Operations\n
-g, GetInput       Gets the input in German. Translates it to English and sends it to Input.py file.\n
-t, Translate      Translates the German file to English and writes it into Input.txt file\n
-k, Keyword        If there is already an Input.txt file this is for writing the specific Keywords and the occurrences of these words to Output.txt file.\n
-d, Delete         Output.txt file always appends. This is for cleaning the data in the Output.txt file.\n
-w, WordCounter    Finds the occurrences of each words and sort them descending except the stopwords.\n
-s, Sentiment      Finds the overall sentiment and sentence by sentence sentiment of the whole text.\n
-a, All            Takes voice input, finds the keywords, finds occurrences, and does the sentiment analysis.\n
To GetInput type 'python Main.py GetInput' to the console.
""")

parser.add_argument("operation")
args = parser.parse_args()

if(args.operation == "GetInput"):
    GetInput()

elif(args.operation == "Translate"):
    Translate()

elif(args.operation == "Keyword"):
    Keyword()

elif(args.operation == "Delete"):
    Erase()

elif(args.operation == "WordCounter"):
    WordCount()

elif(args.operation == "Sentiment"):
    StartSentiment()

elif(args.operation == "All"):
    GetInput()
    Keyword()
    Erase()
    WordCount()
    StartSentiment()
