import json
from datetime import datetime
import random

# poistaa tiedostosta rivinvaihdot, hakee random sanan 'sanat.txt' tiedostosta
def haeSana():
    with open("sanat.txt") as tiedosto:
        rivit = [line.rstrip('\n') for line in tiedosto]
        sana = random.choice(rivit)
        print(sana)
        return sana

#tallentaa pelin ja palaa alkunäyttöön
def tallennaPeli(vastaus, yritykset, arvaukset):
    paiva = datetime.now()
    tiedosto = open("tallennus.txt", "w")
    tallennusSanakirja = {"Päivämäärä" : paiva.strftime("%d"+".""%B"+".""%Y"),
    "vastaus" : vastaus, "yritykset" : yritykset, "arvaukset" : arvaukset}
    json.dump(tallennusSanakirja, tiedosto, ensure_ascii=False)
    tiedosto.close()
    print("Pelisi on nyt tallennettu! Palataan alkunäyttöön")
    GUI()

def lataaTallennettuPeli():
    with open("tallennus.txt", "r") as tiedosto:
        data = json.load(tiedosto)
        try:
            vastaus = data["vastaus"]
            yritykset = data["yritykset"]
            arvaukset = data["arvaukset"]
        except KeyError:
            print("Tallennusta ei ole olemassa, aloitetaan uusi peli")
            peliMuoto("uusi")
    return vastaus, yritykset, arvaukset


def pelinTilanne(yritykset):
    match yritykset:
        case 5:
             print("---|---- \n"
                    "---|---- \n"
                    "---|---- \n"
                    "--===--- \n"
                    "--|-|--- \n")
        case 4:
             print("---|––|- \n"
                    "---|---- \n"
                    "---|---- \n"
                    "--===--- \n"
                    "--|-|--- \n")
        case 3:
             print("---|––|- \n"
                    "---|--O- \n"
                    "---|---- \n"
                    "--===--- \n"
                    "--|-|--- \n")
        case 2:
             print("---|––|- \n"
                    "---|--O- \n"
                    "---|--|- \n"
                    "--===--- \n"
                    "--|-|--- \n")
        case 1:
             print("---|––|- \n"
                    "---|--O- \n"
                    "---|-/|\ \n"
                    "--===--- \n"
                    "--|-|--- \n")
        case 0:
             print("---|––|- \n"
                    "---|--|- \n"
                    "---|--O- \n"
                    "---|-/|\ \n"
                    "--===/-\ \n"
                    "--|-|--- \n")

def peli(vastaus, yritykset, arvaukset,):
    while yritykset > 0:
        sallitutInputit = ("abcdefghijklmnopqrstuvwxyzåäö")
        printattavaSana = (' ' .join(arvaus if arvaus in arvaukset else '_' for arvaus in vastaus))
        if '_' not in printattavaSana:
            print(f"VOITIT PELIN, vastaus oli {vastaus}. Palataan alkunäyttöön.")
            GUI()
            break
        else: 
            print (printattavaSana)
        
        #testaa onhan arvaus validi TAI pelintallennus
        while True:
            arvaus = (input("Arvaa kirjainta: "))
            arvaus = arvaus.lower()
            if arvaus == "tallenna peli":
                tallennaPeli(vastaus, yritykset, arvaukset)
            if arvaus in sallitutInputit and len(arvaus) == 1:
                break
            else:
                print("Arvaus ei kelvollinen. Arvauksen pitää olla yksi kirjain (a-ä).")
        
        if arvaus in arvaukset:
            print("Arvasit tämän jo! Arvaa jotain muuta")

        if arvaus in vastaus and arvaus not in arvaukset:
            arvaukset.append(arvaus)

        if arvaus not in vastaus and arvaus not in arvaukset:
            yritykset = yritykset-1
            pelinTilanne(yritykset)

            if yritykset == 0:
                print(f"Yritykset loppuivat kesken, oikea sana oli {vastaus}. Palataan alkunäyttöön")
                GUI()

            else:
                arvaukset.append(arvaus)
                print(f"Yrityksiä jäljellä {yritykset}")
                print(f"Arvatut kirjaimet {arvaukset}")

#uusi tai tiedostosta
def peliMuoto(pelinMuoto):

    if pelinMuoto == "uusi":
        vastaus = haeSana()
        yritykset = 6
        arvaukset = []

    if pelinMuoto == "tallennettu":
       lataaTallennettuPeli()
       vastaus = vastaus
       print (vastaus + "miksei toimi")
       yritykset = yritykset
       arvaukset = arvaukset
       print(f"Peli ladattu onnistuneesti! Tämänhetkiset yritykset: {yritykset} ja arvaukset: {arvaukset}")

    peli(vastaus, yritykset, arvaukset)

def GUI():
    print("---------" '\n' "HIRSIPUU" '\n' "---------" '\n' "Tervetuloa pelaamaan. Arvauksen on oltava yksi kirjain väliltä a-ä tai 'tallenna peli',"
    "jolloin peli tallennetaan tiedostoon. Valitse pelimuoto:"'\n' "0 - jos haluat sulkea pelin" '\n' "1 - jos haluat pelata uuden pelin" '\n' 
    "2 - jos haluat pelata tallennetun pelin")
    pelimuoto = int(input())
    match pelimuoto:
        case 0:
            exit()
        case 1:
            peliMuoto("uusi")
        case 2:
            peliMuoto("tallennettu")

GUI()