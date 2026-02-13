# ==========================================
# Voorbeeld Opdracht
# Gegeven is een variabele 'leeftijd' met de waarde 25. Print de zin 'Mijn leeftijd is 25'
# ==========================================

leeftijd = 25
print('Mijn leeftijd is', leeftijd)  # Het resultaat is: Mijn leeftijd is 25

# ==========================================
# Opgave 1.
# Gegeven is een variabele 'naam' met de waarde 'Jan' en de variabele 'leeftijd' met de waarde 25. Print de zin 'Mijn naam is Jan en ik ben 25 jaar oud'. Verander daarna de leeftijd naar 30 en print de zin opnieuw.
#
# Verwachte uitkomst is: 'Mijn naam is Jan en ik ben 25 jaar oud' en 'Mijn naam is Jan en ik ben 30 jaar oud'
# ==========================================

naam = 'Jan'
leeftijd = 25

print(f'Mijn naam is {naam} en ik ben {leeftijd} jaar oud')
leeftijd += 5
print(f'Mijn naam is {naam} en ik ben {leeftijd} jaar oud')


# ==========================================
# Opgave 2.
# Gegeven zijn een aantal variabelen. Wat zijn de datatypes van de variabelen als je ze print met de type() method? Bedenk vooraf wat het datatype is en controleer daarna met de print functie of je het goed hebt.
# ==========================================

a = 5 / 5
print(type(a)) # float

b = '12'
print(type(b)) #str

c = 5 * 5
print(type(c)) #int

d = 'Python' * 4
print(type(d)) #str

# ==========================================
# Opgave 3.
# Variabele namen mag je zelf verzinnen, maar niet alle namen zijn toegestaan omdat ze al gebruikt worden door Python (keywords). Welke van de volgende variabele namen zijn toegestaan en welke niet?
# ==========================================


# And = 'something'
# while = 'something'
# Break = 'something'
# awaiting = 'something'

#while mag niet


# ==========================================
# Opgave 4.
# Schrijf een goede variabele naam voor onderstaande onderdelen. Denk aan de conventies voor Python variabelen.
#
# a.     Het totale aantal van het product bananen in een winkelmand
#
# b.     De minimale toegestane lengte voor een attractie in een pretpark
#
# c.     Het grootste getal in een rij met getallen
# ==========================================

#totaal_aantal_bananen_winkelmand
#minimale_lengte_attracite

# ==========================================
# Opgave 5.
# Gegeven is de variabele 'teller' met de waarde 10. Verhoog de waarde van de teller met 1. Gebruik de samengevoegde toekenning operator. Print de waarde van de teller. Herhaal dit proces maar verlaag de teller met 2. Print opnieuw de waarde van de teller.
#
# Verwachte uitkomst is: 11 en 9
# ==========================================

teller = 10
teller += 1
print(teller)
teller -= 2
print(teller)



# ==========================================
# Opgave 6.
# Gegeven zijn de onderstaande statements. Welke van de print statements zullen een foutmelding geven en waarom?
#
# a. print(int(‘1490.99’)
#
# b. print(float(12))
#
# c. print(int('1plus1'))
#
# d. print(str(25E10))
# ==========================================

#print(int(‘1490.99’)
#fout - kan geen int van floaty string maken

#print(float(12))
#ok

#print(int('1plus1'))
#fout - kan geen int van string maken

#print(str(25E10))
#ok

# ==========================================
# Opgave 7.
# Gegeven is de variabele getal_1 met waarde 3 en getal_2 met waarde 5. Schrijf de zin 'Het product van 3 en 5 is 15' door de variabelen te gebruiken in de zin. Pas een f-string toe.
# ==========================================

getal_1 = 3
getal_2 = 5

print(f'Het product van {getal_1} en {getal_2} is {getal_1 * getal_2}')
