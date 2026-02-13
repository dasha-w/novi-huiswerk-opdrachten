'''
Opgave 1
Beredeneer wat de antwoorden zijn van de volgende expressies
A. Gebruik logische operatoren om te controleren of x positief is en kleiner dan 10.
B. Maak een variabele x = 5 aan zet daaronder een print() functie met de vergelijking.
C. Doe dit daarna ook met x = -5
'''

x=5
print( 0 < x < 10)
x=-5
print( 0 < x < 10)
'''
Opgave 2
Geef aan wat het resultaat zou zijn van de volgende code:
A. print(False and 0 / 0)
B. print(True or 1 / 0)
'''

print(False and 0/0)
# false

print(True or 1/0)
#true

#------------------------------------------
'''Opgave 1:
Even of oneven nummer
Neem een nummer, bijvoorbeeld 42, en je wilt weten of het even of oneven is. 
Je gebruikt een eenvoudige check: als het nummer gedeeld door 2 geen rest heeft, dan is het even. Anders is het oneven. 
Dus, voor het nummer 42, zou je zeggen dat het "Even" is, omdat het zonder rest door 2 gedeeld kan worden.
Schrijf de vergelijking nu in Python code.
'''
x=42
even_or_uneven = "Even" if x %2 == 0 else "Oneven"
print(even_or_uneven)

'''
Opgave 2:
Begroeting op Basis van het Uur van de Dag
Stel je hebt een klok die aangeeft dat het 9 uur 's ochtends is (uur = 9). 
Afhankelijk van het tijdstip wil je een passende begroeting gebruiken: "Goedemorgen", "Goedemiddag", of "Goedenavond". 
Met een conditionele expressie kun je besluiten: als het uur minder dan 12 is, zeg "Goedemorgen"; als het minder dan 18 is, 
zeg "Goedemiddag"; en anders, zeg "Goedenavond". Voor 9 uur 's ochtends zou de gekozen begroeting "Goedemorgen" zijn. 
Tip: je kunt meerdere keren ‘else’ achterelkaar zetten.'''

uur = 9
begroeting = "Goedemorgen" if uur < 12 else "Goedemiddag" if uur < 18 else "Goedenavond"
print(begroeting)

#------------------------------
'''Opgave 1:
Schrijf een programma dat de gebruiker vraagt 2 getallen in te voeren en als resultaat de som en het product van die getallen toont. 
Schrijf ook een passende prompt voor de input() functie en een passende tekst voor de print() functie.
'''
#num1 = int(input("Voer een getal in: "))
#num2 = int(input("Voer nog een getal in: "))
#sum = num1 + num2
#multiply = num1 * num2
#print(f'Je hebt de getallen {num1} en {num2} ingevoer. De som van deze getallen is {sum} en het product {multiply}')

'''
Opgave 2:

Schrijf een programma dat de gebruiker vraagt 2 getallen in te voeren en als resultaat de grootste van die twee getallen toont. 
Schrijf ook een passende prompt voor de input() functie en een passende tekst voor de print() functie.
'''
num1 = int(input("Voer een getal in: "))
num2 = int(input("Voer nog een getal in: "))
grootste_getal = num1 if num1 > num2 else num2
print(f"Het grootste getal dat jij hebt ingevoerd is {grootste_getal}.")