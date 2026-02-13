# ==========================================
# Voorbeeld Opdracht
# Schrijf de notatie van een 10 miljoen. Gebruik de ‘leesbaarheid methode’ van Python.
# print het getal.
# ==========================================

print(10_000_000)  # Het resultaat is: 10000000


# ==========================================
# Opgave 1:
# Welk getal is goed geschreven volgens de ‘leesbaarheid methode’
# print het getal.

#     100_00.000_001
#     1_000.00_001
#     1_000_000.000_1
# ==========================================
print(1_000_000.000_1)


# ==========================================
# Opgave 2:
# Hoe schrijf je de volgende getallen uit in de wetenschappelijke notatie van Python?
# print de getallen.

#     -12.000.000
#     0.13 met drie extra nullen (0.00013)
#     64.000.000.000
# ==========================================

print(-12e6)
print(0.13e-3)
print(64e9)


# ==========================================
# Opgave 3:
# Schrijf 5 miljoen uit. Hoe maak je daar met behulp van de wetenschappelijke notatie 0.05 van?
# ==========================================

print(5_000_000e-8)

# ==========================================
# Opgave 4:
# Wat is het antwoord? Probeer vooraf te bedenken of het antwoord een integer of een float is. Check je antwoord door een print uit te voeren.

# a. 11 * 3
# b. 7.5 – 1.5
# c. 3 + 4.0
# d. 15 / 5
# ==========================================

print(11*3) #int
print(7.5-1.5) #float
print(3+4.0) #float
print(15/5) #float

# ==========================================
# Opgave 5:
# Wat is het antwoord? Probeer vooraf te bedenken of het antwoord een integer of een float is. Check je antwoord door een print uit te voeren.
# a. 18 // 4
# b. 15.5 // 4
# c. 10 % 4
# d. 9 % 4.5
# ==========================================

print('----------------')
print(18//4) #int
print(15.5//4) #float
print(10%4) #int
print(9%4.5) #float

# ==========================================
# Opgave 6:
# Hieronder staan een aantal expressies. Schrijf voor jezelf in een comment wat de volgorde is en reken het antwoord uit. Check dan met een print statement of je hetzelfde antwoord krijgt

#  A   8 + 2 * 3
#  B   (8 + 2) * 3
#  C   2 ** 3 ** 2
#  D   (2 ** 3) ** 2
#  E   100 - 5 ** 2 / 5 * 2
# ==========================================

print(8+2*3) #2*3 = 6+8 = 14
print((8+2)*3) #8+2=10 *3 =30
print( 2** 3 **2) # 3ˆ2 = 9, 2ˆ9 =512
print((2**3)**2) # 2ˆ3 = 8, 8ˆ2 = 64
print(100-5 **2 /5 *2) # 5ˆ2 = 25, /5= 5 *2 =10. 100-10 = 90

# ==========================================
# Opgave 7:
# Zet de volgende tekst om naar een Python string. Let op speciale tekens en spaties.
# Tip: Herhalende woorden kun je met een operator vaker printen
# Check het resultaat met een print statement

# A: Dit is de vorm van een dak / \
# B: ‘quotes’ ‘quotes’ ‘quotes’ ‘quotes’ spamspamspam
# C: Python’s syntax is “eenvoudig”
# ==========================================

print('Dit is de vorm van een dak / \\')
print("'quotes'"*4,"spam"*3)
print('''Python's syntax is "eenvoudig"''')
