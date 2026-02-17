### Laat python 2 getallen optellen en het resultaat printen
#  5 + 3 = 8

print('5 + 3 =',5+3)


### Laat python 2 getallen vermenigvuldigen en het resultaat printen
#  3 * 4 = 12
print(3*4)

### Geef nu het resultaat weer in een string. waar de getallen en het resultaat in staan.


### Laat python de wortel van een getal berekenen en het resultaat printen
# De wortel van 16 is 4
# Tip gebruik ** om de wortel te berekenen
print(16**0.5)
### Laat python de rest van een deling berekenen en het resultaat printen
#  De rest van 10 / 3 is 1
print(10%3)

### Maak een calculator die 2 getallen optelt, aftrekt, vermenigvuldigd en deelt
# Gebruik hiervoor input om de getallen te vragen
# Voer getal 1 in: 5
# Voer getal 2 in: 3
# 5 + 3 = 8
# 5 - 3 = 2
# 5 * 3 = 15
# 5 / 3 = 1.6666666666666667

#niet helemaal af, maar je snapt
getal1= int(input("getal 1:"))
getal2=int(input("getal 2:"))

print(f'{getal1} + {getal2} = {getal1 + getal2}\n'
      f'{getal1} - {getal2} = {getal1 - getal2}\n'
      f'{getal1} * {getal2} = {getal1 * getal2}\n'
      f'{getal1} / {getal2} = {getal1 / getal2}\n')
