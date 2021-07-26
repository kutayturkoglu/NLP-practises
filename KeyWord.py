from nltk import sent_tokenize

def Erase(out = "Output.txt"):
    open(out, "w").close()

def Keyword(inp = "Input.txt", out = "Output.txt"): 
    Input = open(inp, "r").read().lower()
    Output = open(out, "a")
    
    Text = sent_tokenize(Input)
    
    n = int(input("Enter the amount of keyword that you are looking for: "))
    KeyWord = []
    for i in range(n): KeyWord.append(input("Enter the keyword: "))
    
    for i in KeyWord:
        Count = Input.count(i)
        Output.write("\nThe word " + i.upper() + " has occured " + str(Count) + " time(s).\n")
        for j in Text:
            if(i in j):
                Output.write('"' + j + '"' + "\n")               
      

