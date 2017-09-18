#deel 1
def standaardtarief(km):
    if km<=0:
        prijs= 0
    else:
        if km>50:
            prijs= 15 + 0,60 * (km)
        else:
            prijs= 0,80 * (km)
    return (prijs)

#deel 2
def ritprijs (leeftijd, weekendrit, afstandKM):
    prijs= standaardtarief(afstandKM)
    if weekendrit == 'False':
        if leeftijd <12 or leeftijd >=65:
         ritprijs = prijs * 0,70

    if weekendrit == 'True':
        if leeftijd <12 or leeftijd >=65:
            ritprijs= prijs * 0,65
        else:
            ritprijs= prijs * 0,60

















