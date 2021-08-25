import json
from difflib import get_close_matches

elements = json.load(open("wordbook.json"))

def findmeaning(word):
    if word in elements:
        return elements[word]
    elif len(get_close_matches(word, elements.keys())) > 0:
        closematches = get_close_matches(word, elements.keys())[0]
        user_decision = input("Are you looking for % s instead? [Y/N] " % closematches)
    
    if user_decision == "Y":
        return elements[get_close_matches(word, elements.keys())[0]]
    elif user_decision == "N":
        return "I'm Sorry!!! The word you're looking for cannot be found."

word = input("Type any word here: ")
out = findmeaning(word.lower())

if type(out) == list:
    for i in out:
        print(i)

else:
    print(out)