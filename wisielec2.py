import random
HANGMAN = ("""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")


WORDS = ["GRACZ", "ZIOM", "MARTIN", "DUPEK", "NADZIEJA", "TRAKTORZYSTA"]
lossowe_slowo = random.choice(WORDS)
slowo = "-"*len(lossowe_slowo)
zycie = 0
uzyte_litery = []
while len(HANGMAN) > zycie and lossowe_slowo != slowo:
    print(uzyte_litery)
    print(slowo)
    szansa = input("Podaj litere: ")
    szansa = szansa.upper()
    while True:
        if szansa in uzyte_litery:
            print("Ta litera juz byla wykorzystana ")
            szansa = input("Podaj litere: ")
            szansa = szansa.upper()
        else:
            break
    uzyte_litery.append(szansa)
    if szansa in lossowe_slowo:
        print("Litera znajduje sie w slowie: ")
        new = ''
        for i in range(len(lossowe_slowo)):
            if lossowe_slowo[i] == szansa:
                new +=szansa
            else:
                new +=slowo[i]
        slowo = new
    else:
        print("Litera nie znajduje sie w slowie")
        print(HANGMAN[zycie])
        zycie +=1
if slowo == lossowe_slowo:
    print("Gratulacje wygrales")
else:
    print(f"niestety przegrales slowo to {lossowe_slowo}")
