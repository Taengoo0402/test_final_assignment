#f= open('C:/Users\Gebruiker\OneDrive\Documenten\kluizen.txt', 'r')

def toon_aantal_kluizen_vrij():
    f = open('kluizen.txt', 'r')
    lines = f.readlines()
    f.close()
    return 12 - len(lines)

vrij_aantal = toon_aantal_kluizen_vrij()

def nieuwe_kluis():
    f = open('kluizen.txt', 'r')
    lines = f.readlines()
    f.close()

    kluizen = []
    if toon_aantal_kluizen_vrij() > 0:
        mogelijk_vrije_kluizen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        # gooi bezette er uit
        for line in lines:
            nr = line.split(';')[0]
            mogelijk_vrije_kluizen.remove(int(nr))

        print(mogelijk_vrije_kluizen)

        # bepaal eertse nieuwe kluis
        vrij = min(mogelijk_vrije_kluizen)

        # vraag wachtwoord
        wachtwoord = input('Wat is je wachtwoord?')

        f = open('kluizen.txt', 'a')
        f.write(str(vrij)+ ';' + wachtwoord+'\n')
        f.close()
        print('Je kluisnummer is', vrij)

    else:
        print('alle kluizen zijn in gebruik')


def kluis_openen():
    f = open('kluizen.txt', 'r')
    lines = f.readlines()
    f.close()

    nummer = input('kluisnummer? ')
    wachtwoord = input('wachtwoord? ')
    antw= nummer +';' +wachtwoord+'\n'

    if antw in lines:
        print('Dit is jouw kluisnummer:', nummer)
    else:
        print('Het nummer of wachtwoord is fout.')
    return(nummer)


def menu(cijfer):
    if cijfer == 1:
        kluizen = toon_aantal_kluizen_vrij()
        print('{0} kluizen zijn bezet'.format(kluizen))
    elif cijfer == 2:
        nieuwe_kluis()
    elif cijfer == 3:
        kluis_openen()
    elif cijfer == 4:
        exit(0)
    else:
        print('geef een andere cijfer.')

while True:
    print('kies een menu')
    print('1) vrije kluizen')
    print('2) nieuwe kluis')
    print('3) kluis openen')
    print('4) stop')
    menu(int(input('kies een menu.')))