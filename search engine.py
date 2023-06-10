import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        print(get_close_matches(w, data.keys())[0::], " if the word you are searching is there in the above list then type yes , if not type no ")
        yn = input()
        if yn == "yes":
            a = input("Enter the word:")
            if a in data:
                for i in data.keys():
                    if i == a :
                        x = data[i]
                        for j in x:
                            print(j)

            else:
                return "You gave external word"
        else:
            return "we didn't understand your entry"
    else:
        return "the word doesnt exist.please double check it"


word = input("enter word:")
output = translate(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
