import enchant
import random



letters = "uqtianc"
constant = "u"
minLength = 4
maxLength = 10


correctWords = []

isEnglish = enchant.Dict("en_US")


print("finding words...")
def findWord():    
    wordSize = random.randint(minLength,maxLength) 
    word = "".join(random.choices(letters, k=wordSize))
    if constant in word:
        if isEnglish.check(word):
            if word not in correctWords:
                correctWords.append(word)

    

for i in range(0, 1000000):

    findWord()
print(correctWords)
