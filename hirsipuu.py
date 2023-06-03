import tiedostonKasittely

#printtaa jäljellä olevien yritysten mukaan oikean hirsipuun
def pelinTilanne(yritykset):
    match yritykset:
        case 5:
            print("---|----")
            print("---|----")
            print("---|----")
            print("--===---")
            print("--|-|---")
        case 4:
            print("---|––|-")
            print("---|----")
            print("---|----")
            print("--===---")
            print("--|-|---")
        case 3:
            print("---|––|-")
            print("---|--O-")
            print("---|----")
            print("--===---")
            print("--|-|---")
        case 2:
            print("---|––|-")
            print("---|--O-")
            print("---|--|-")
            print("--===---")
            print("--|-|---")
        case 1:
            print("---|––|-")
            print("---|--O-")
            print("---|-/|\\")
            print("--===---")
            print("--|-|---")
        case 0:
            print("---|––|-")
            print("---|--|-")
            print("---|--O-")
            print("---|-/|\\")
            print("--===/-\\")
            print("--|-|---")


#uusi tai tiedostosta
def peliMuoto(pelinMuoto):
    vastaus = tiedostonKasittely.haeSana()
    yritykset = 6
    arvaukset = []

    if pelinMuoto == "uusi":
        pass

    if pelinMuoto == "tallennettu":
        vastaus, yritykset, arvaukset = tiedostonKasittely.lataaTallennettuPeli(vastaus, yritykset, arvaukset)

    peli(vastaus, yritykset, arvaukset)


def GUI():
    print("---------")
    print("HIRSIPUU")
    print("---------")
    print("Tervetuloa pelaamaan. Arvauksen on oltava yksi kirjain väliltä a-ä tai 'tallenna peli',"
          "jolloin peli tallennetaan tiedostoon. Valitse pelimuoto:")
    print("0 - jos haluat sulkea pelin")
    print("1 - jos haluat pelata uuden pelin")
    print("2 - jos haluat pelata tallennetun pelin")
    pelimuoto = input()

    match pelimuoto:
        case "0":
            exit()
        case "1":
            peliMuoto("uusi")
        case "2":
            peliMuoto("tallennettu")


#kutsutaan pelin jälkeen
def pelataankoUusiksi(lopputulos, vastaus):
    if lopputulos == "voitto":
        uusiksi = input(f"VOITIT PELIN, vastaus oli {vastaus}. Haluatko pelata uusiksi? K/E ")
    if lopputulos == "häviö":
        uusiksi = input(f"HÄVISIT PELIN, vastaus oli {vastaus}. Haluatko pelata uusiksi? K/E ")

    if uusiksi.lower() == "k":
        peliMuoto("uusi")
    else:
        print("Palataan alkunäyttöön!")
        GUI()


#hirsipuu
def peli(vastaus, yritykset, arvaukset):
    while True:
        sallitutInputit = "abcdefghijklmnopqrstuvwxyzåäö"
        printattavaSana = ''.join(arvaus if arvaus in arvaukset else '_' for arvaus in vastaus)
        if '_' not in printattavaSana:
            pelataankoUusiksi("voitto", vastaus)
            break
        else:
            print(printattavaSana)

        #testaa onhan arvaus validi TAI pelintallennus
        while True:
            arvaus = input("Arvaa kirjainta: ").lower()
            if arvaus == "tallenna peli":
                tiedostonKasittely.tallennaPeli(vastaus, yritykset, arvaukset)
                print("Pelisi on tallennettu. Palataan alkunäyttöön.")
                GUI()
            if arvaus in sallitutInputit and len(arvaus) == 1:
                break
            else:
                print("Arvaus ei kelvollinen. Arvauksen pitää olla yksi kirjain (a-ä).")

        if arvaus in arvaukset:
            print("Arvasit tämän jo! Arvaa jotain muuta")

        if arvaus in vastaus and arvaus not in arvaukset:
            arvaukset.append(arvaus)

        if arvaus not in vastaus and arvaus not in arvaukset:
            yritykset -= 1
            pelinTilanne(yritykset)

            if yritykset == 0:
                pelataankoUusiksi("häviö", vastaus)

            else:
                arvaukset.append(arvaus)
                print(f"Yrityksiä jäljellä {yritykset}, arvatut kirjaimet {arvaukset}")


GUI()