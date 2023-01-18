"""
You’re working on a search engine. Watch your back Google!

The given code takes a text and a word as input and passes them to a function called search().

The search() function should return "Word found" if the word is present in the text,
or "Word not found", if it’s not.

Sample Input;
"This is awesome"
"awesome"

Sample Output;
Word found
"""


def search():
    if word in text:
        return f"Word {word} found"
    else:
        return f"Word {word} not found"


text = input("Paste body of text here ")
word = input("Type the word you're looking for here ")

print(search())
