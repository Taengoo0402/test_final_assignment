#deel 1
def standaardtarief(km):
    if km <=0:
        prijs = 0
    else:
        if km >50:
            prijs = 15 + 0.60 * (km)
        else:
            prijs = 0.80 * (km)
    return prijs

#deel 2
def ritprijs (leeftijd, weekendrit, afstandKM):
    prijs= standaardtarief(afstandKM)
    RitPrijs= prijs
    if not weekendrit:
        if leeftijd <12 or leeftijd >=65:
            RitPrijs = prijs * 0.70

    if weekendrit:
        if leeftijd <12 or leeftijd >=65:
            RitPrijs= prijs * 0.65
        else:
            RitPrijs= prijs * 0.60
    return RitPrijs

leeftijd= eval(input('Wat is je leeftijd?\n'))
weekendrit= input('Reis je in het weekend?\n')
if weekendrit == 'Ja':
    weekendrit = True
else:
    weekendrit = False
afstandKM= eval(input('Hoever reis je?\n'))
print(ritprijs(leeftijd, weekendrit, afstandKM))























