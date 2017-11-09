stations = ['Schagen', 'Heerhugowaar', 'Alkmaar','Castricum', 'Zaandam', 'Amsterdam Sloterdijk','Amsterdam Centraal', 'Amsterdam Amstel',
            'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_beginstation(stations):

    while True:
        beginstation = input('Wat is je beginstation?')
        if beginstation in stations:
            print('Uw heeft gekozen:', beginstation)
            break
        else:
            print('Fout invoer')
    return beginstation


def inlezen_eindstation(stations, beginstation):
    while True:
        eindstation = input('Wat is je eindstation?')
        if eindstation in stations and stations.index(eindstation)> stations.index(beginstation):
            print('U heeft gekozen voor station', eindstation)
            break
        else:
            print('Verkeerde station.')


    return eindstation

def omroepen_reis(stations, beginstation, eindstation):
    beginnummer = (stations.index(beginstation) + 1)
    eindnummer = (stations.index(eindstation) + 1)

    print(beginstation, 'is nummer', beginnummer, 'in het traject')
    print(eindstation, 'is nummer', eindnummer, 'in het traject')
    if eindnummer > beginnummer:
        print('De afstand bedraagt', eindnummer - beginnummer, 'station(s)')
        print('De prijs bedraagt', (eindnummer - beginnummer) * 5, 'euro')
    else:
        print(eindstation, 'is niet mogelijk')
    print('Je stapt in:', beginstation)
    print('Je stapt uit:', eindstation)

beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)


