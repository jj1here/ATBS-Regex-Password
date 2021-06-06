import re

def paswrdCheck(text) :

    upperRegex = re.compile(r'[A-Z]')
    lowerRegex = re.compile(r'[a-z]')
    digitRegex = re.compile(r'[0-9]')

    upper = upperRegex.search(text)
    lower = lowerRegex.search(text)
    digit = digitRegex.search(text)

    if len(text) > 8 and upper != None and lower != None and digit != None :
            print("Strong Password!")
    else:
        print("Weak Password!")

text= "Abc12dasa!"

paswrdCheck(text)



