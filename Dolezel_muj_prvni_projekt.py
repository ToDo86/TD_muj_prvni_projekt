"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomas Dolezel
email: tomas.dolezel@sykorait.com
discord: TomasDo#3697
"""
##################################################################################################################################

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.
''']

users = ('bob', 'ann', 'mike', 'liz')
passwords = ('123', 'pass123', 'password123', 'pass123' )
separator = "=" * 50
separator2 = "-" * 50
#################################################################################################################################

print('Vitejte v nasem Textovem analyzatoru SUPERTEXT2023')
print(separator)

regUsers = dict(zip(users, passwords))

userName = input('Nejdrive prosim zadejte Vase uzivatelske jmeno: ')

if userName in regUsers:
    userPassword = input('Vas uzivatel existuje. Pokracujte zadanim Vaseho hesla: ')
    if regUsers['bob'] == userPassword:
        print('Vitejte v nasi aplikaci, ' + str.title(userName))
        print('Nabizime tri texty k analyze:' + str(TEXTS))
        chosenText = int(input('Vyberte cislo od 1 do 3: '))
        if chosenText >= 1 and chosenText <= 3:
            textToAnalyse = TEXTS[chosenText - 1] 
            #print(textToAnalyse)
            
            cleanedWords = []
            
            for slovo in textToAnalyse.split():
                cleanWord = slovo.strip(".,!?")
                cleanedWords.append(cleanWord.lower())
            #print(cleanedWords)
            
            countWords = {}
            for slovo in cleanedWords:
                if slovo not in countWords:
                    countWords[slovo] = 1
                else:
                    countWords[slovo] = countWords[slovo] + 1
            
            #print(countWords)
            
            countValues = sorted(list(countWords.values()), reverse=True)[0:5]
            print(countValues)
            
            topFive = list()

            for count in countWords:
                if countWords[count] in countValues:
                    countValues.remove(countWords[count])
                    topFive.append((countWords[count], count))
            print(topFive)
            
            topFive = sorted(countWords, key=countWords.get, reverse=True)[0: 5]
            

        else:
            print('Zadany znak nesplnuje podminky pro vyber. Program ukoncen.')
        print(separator2)
    elif regUsers['ann'] == userPassword:
        print('Vitejte v nasi aplikaci, ' + str.title(userName))
        print('Nabizime tri texty k analyze:' + str(TEXTS))
        print(separator2)
    elif regUsers['mike'] == userPassword:
        print('Vitejte v nasi aplikaci, ' + str.title(userName))
        print('Nabizime tri texty k analyze:' + str(TEXTS))
        print(separator2)
    elif regUsers['liz'] == userPassword:
        print('Vitejte v nasi aplikaci, ' + str.title(userName))
        print('Nabizime tri texty k analyze:' + str(TEXTS))
        print(separator2)
    else:
        print('Vase heslo je spatne. Pristup zamitnut')
else:
    print('Je nam lito. Zadany uzivatel neexistuje. Pristup zamitnut')

#print(reg_users)

