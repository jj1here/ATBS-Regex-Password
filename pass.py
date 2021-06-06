import re

text= "Abc12dasa!"

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



