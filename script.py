import enchant
import random



letters = "uqtianc"
constant = "u"

correctWords = []

isEnglish = enchant.Dict("en_US")


print("finding words...")
def findWord():    
    wordSize = random.randint(4,10) 
    word = "".join(random.choices(letters, k=wordSize))
    if constant in word:
        if isEnglish.check(word):
            if word not in correctWords:
                correctWords.append(word)

    

for i in range(0, 1000000):

    findWord()
print(correctWords)
