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

from pprint import pprint

pprint('Vitejte v nasem Textovem analyzatoru SUPERTEXT2023')
pprint(separator)

regUsers = dict(zip(users, passwords))

userName = input('Nejdrive prosim zadejte Vase uzivatelske jmeno: ')

if userName in regUsers:
    userPassword = input('Vas uzivatel existuje. Pokracujte zadanim Vaseho hesla: ')
    
    if userName in regUsers:
        if regUsers[userName] == userPassword:
            pprint('Vitejte v nasi aplikaci, ' + str.title(userName))
            pprint(separator2)
            chosenText = int(input('Nabizime tri texty k analyze. Vyberte cislo od 1 do 3: '))
            if chosenText >= 1 and chosenText <= 3:
                textToAnalyse = TEXTS[chosenText - 1] 
                #pprint(textToAnalyse)
                        
                cleanedWords = []
                digits = []
                uppercase = []
                title = []
                lowercase = []
                        
                for slovo in textToAnalyse.split():
                    cleanWord = slovo.strip(".,!?:;")             
                    cleanedWords.append(cleanWord)
                totalWords = len(cleanedWords)
                
                for typSlova in textToAnalyse.split():
                    cleanWord = typSlova.strip(".,!?:;")
                    if typSlova.isdigit():
                        digits.append(cleanWord)
                    elif typSlova.isupper():
                        uppercase.append(cleanWord)
                    elif typSlova.istitle():
                        title.append(cleanWord)
                    elif typSlova.islower():
                        lowercase.append(cleanWord)      
                    else:
                        pass
                countNumbers = len(digits)
                countUppers = len(uppercase)
                countTitles = len(title)
                countlowerCases = len(lowercase)

                pprint(f"""
                {separator2} Pocet cisel v textu je {countNumbers}.
                Pocet slov s velkym pocatecnim pismenem je {countTitles}.
                Pocet slov s pocatecnim malym pismenem je {countlowerCases}.
                Pocet slov s velkymi pismeny je {countUppers}.{separator2}
                """)   
                #pprint(countUppers)
                #pprint(countTitles)
                #pprint(lowercase)                
                #pprint(lowercase)
                #pprint(uppercase)



                pprint(totalWords)
                #pprint(cleanedWords)
                        
                countWords = {}
                for slovo in cleanedWords:
                    if slovo not in countWords:
                        countWords[slovo] = 1
                    else:
                        countWords[slovo] = countWords[slovo] + 1
                        
                #pprint(countWords)
              
                countValues = sorted(list(countWords.values()), reverse=True)[0:5]
                pprint(countValues)
                        
                topFive = list()

                for count in countWords:
                    if countWords[count] in countValues:
                        countValues.remove(countWords[count])
                        topFive.append((countWords[count], count))
                pprint(topFive)
                        
                #topFive = sorted(countWords, key=countWords.get, reverse=True)[0: 5]

                separator3 = "+--+------------+--+"
                
                for index, par in enumerate(sorted(topFive, reverse=True), 1):
                    print(separator3, f"|{index}.|{par[1]: ^10}|{par[0]}x|", separator3, sep="\n")
                
                

                    
            else:
                pprint('Je nam lito. Muzete vkladat pouze cislice 1, 2 nebo 3. Program ukoncen.')
                pprint(separator2)
        else:
            pprint('Je nam lito. Vase heslo neni spravne. Program ukoncen.')
else:
    pprint('Je nam lito. Zadany uzivatel neexistuje. Pristup zamitnut')

