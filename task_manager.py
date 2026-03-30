import sys
import re


def hlavni_menu():
    while True:
        print("\nSprávce úkolů - Hlavní menu")
        print("1. Přidat nový úkol\n2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol\n4. Konec programu")
        global vyber_akce 

        # ošetření vstupu:
        while True:
            vyber_akce = input("Vyberte možnost (1-4): ")
            if vyber_akce.isdigit() and 0 < int(vyber_akce) < 5:
                vyber_akce = int(vyber_akce)
                break
            print('Neplatný vstup, zadejte číslo 1. - 4.')

        # přesun k akcím
        if (vyber_akce == 1):
            pridat_ukol()
        elif (vyber_akce == 2):
            zobrazit_ukoly()
        elif (vyber_akce == 3):
            odstranit_ukol()
        elif (vyber_akce == 4):
            print("Konec programu.")
            sys.exit()


def pridat_ukol():
    # zadání názvu úkolu
    while True:
        nazev = input('Zadejte název úkolu: ').strip()
        if not nazev:
            print('Název úkolu nesmí být prázdný.')
            continue
        if not any(char.isalpha() for char in nazev):
            print("Název úkolu musí obsahovat alespoň jedno písmeno.")
            continue
        if not any(char.isdigit() for char in nazev):
            print("Název úkolu musí obsahovat alespoň jedno číslo.")
            continue
        # vyčlenění čísla úkolu
        match = re.search(r"\d+", nazev)
        cislo = int(match.group())
        # kontrola duplicity čísla
        if any(ukol["cislo"] == cislo for ukol in ukoly):
            print(f'Úkol s číslem {cislo} už existuje. Zadejte jiný název úkolu.')
            continue
        break

    # zadání popisu úkolu
    while True:
        popis = input('Zadejte popis úkolu: ').strip()
        if not popis:
            print('Popis úkolu nesmí být prázdný.')
            continue
        break

    # vytvoření slovníku
    ukol = {
        "cislo": cislo,
        "nazev": nazev,
        "popis": popis
    }

    # přidání do seznamu
    ukoly.append(ukol)

    print(f'Úkol "{nazev}" byl přidán')


def zobrazit_ukoly():
    print('\nSeznam úkolů:')

    global i
    i = 1

    for u in ukoly:
        print(f'{i}. {u["nazev"]} - {u["popis"]}')
        i += 1


def odstranit_ukol():
    if not ukoly:
        print('Nejsou uloženy žádné úkoly.\n')
        return

    zobrazit_ukoly()

    while True:

        # validace vstupu
        while True:
            maz_cislo = input('\nZadejte číslo úkolu, který chcete odstranit: ').strip()
            if maz_cislo.isdigit():
                maz_cislo = int(maz_cislo)
                break
            print('Neplatný vstup, zadejte číslo.')

        # hledání úkolu
        for index, ukol in enumerate(ukoly):
            if ukol["cislo"] == maz_cislo:
                odebrany = ukoly.pop(index)
                print(f'Úkol "{odebrany["nazev"]}" byl odstraněn.')
                return  # ← tady končíme úspěšně

        # pokud se nenašel
        print('Úkol s tímto číslem nebyl nalezen. Zkuste to znovu.')



ukoly = []
hlavni_menu()