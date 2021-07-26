# NLP
This is a command line project and an introduction to Natural Language Processing. Project takes the speech input in German and translates into English. Than it finds the certain keyword/keywords that user demands, finds the frequency of each word and makes a sentiment analysis.

If you already have a file that is written in German, without taking an input you can translate it into English and select those functions that are listed above.

If you already have a translated file, without translation or getting input, you can choose any of those functions listed above.

You can choose any of the functions to process by using the prompt.

## Main
This is where the whole code runs from. As I said this is a command line project. For VS Code if you type python **Main**.**py** **-h**  than the instructions will show up. 

## GetInput
This is a speech to text code. It takes the speech in German, and then translates it into English and writes it to the Input.txt file. 

## Translate
If you have a file which is written in German, this translates that file and writes the English version to Input.txt file.

## WordCounter
After the file is translated, or if it was English from the beginning, Input.txt file gets separated into words. After this separation, the stop words such as "the", "he", "she", "it", "a", "an" are taken off from the text. Than the code reads the file and writes the occurrences of each word through the text. This is for finding the frequencies. 

## KeyWord
It is for finding the keywords that the user looks for. User enters the amount of keywords that are looking for and code finds the frequency, and the sentences that the keyword occurred. These sentences and the amount of occurrence gets written into Output.txt file. This file appends itself. If the user wants to crush the file, Erase() function can be called.

## Sentiment
This makes a sentiment analysis to the Input.txt file and calculates the positivity or negativity of each sentence through the text and it gives a summary of the whole text's sentimental values. 

There are [four values](https://predictivehacks.com/how-to-run-sentiment-analysis-in-python-using-vader/) in total. 
* Neg stands for negative 0 < Neg < 1
* Neu stands for neutral 0 < Neu < 1 
* Pos stands for positive 0 < Pos < 1
* Compound, -1 < Compound < 1

It can be developed as finding the negative correlated sentences which gives us the unpleasant situations about the process. This can be either done by the Google Cloud Platform. For creating our own sentiment analysis, first we need to collect the data. These are the packages already has those data in it and already processed these data.

**P.S.:** I am not sure with the commercial usages of these packages that I used. They were on the internet but I couldn't find any commercial usage approvement.
* [nltk](https://github.com/nltk/nltk/blob/develop/LICENSE.txt) Allowed for commercial use
* [argparse](https://pypi.org/project/argparse/) Licensed under the Python License
* [speech_recognition](https://github.com/Uberi/speech_recognition/blob/master/LICENSE.txt) Licensed under BSD License 
* [googletrans](https://github.com/ssut/py-googletrans/blob/master/LICENSE) Allowed for commercial use
* [json](https://docs.python.org/3/library/json.html), [licence](https://pypi.org/project/jsonlib/) General Public Licence
* [re](https://docs.python.org/3/library/re.html)  Licensed under Apache License
* [py_googletrans](https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group) googletrans module was defective in me so I downloaded it from the link in the entry.
* [BSD_License](https://en.wikipedia.org/wiki/BSD_licenses#:~:text=Commercial%20license%20compatibility,-The%20FreeBSD%20project&text=The%20BSD%20License%20allows%20proprietary,usual%20commercial%20usages%20under%20them.)
* [Apache_License](https://www.whitesourcesoftware.com/resources/blog/top-10-apache-license-questions-answered/#:~:text=You%20can%20use%20any%20Apache,your%20product%20or%20its%20documentation.)

