import tiedostonKasittely
import kayttoliittyma

#printtaa jäljellä olevien yritysten mukaan oikean hirsipuun
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

#hirsipuu
def peli(vastaus, yritykset, arvaukset):
    while True:
        sallitutInputit = ("abcdefghijklmnopqrstuvwxyzåäö")
        printattavaSana = (' ' .join(arvaus if arvaus in arvaukset else '_' for arvaus in vastaus))
        if '_' not in printattavaSana:
            kayttoliittyma.pelataankoUusiksi("voitto", vastaus)
            break
        else: 
            print (printattavaSana)
        
        #testaa onhan arvaus validi TAI pelintallennus
        while True:
            arvaus = (input("Arvaa kirjainta: "))
            arvaus = arvaus.lower()
            if arvaus == "tallenna peli":
                tiedostonKasittely.tallennaPeli(vastaus, yritykset, arvaukset)
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
                kayttoliittyma.pelataankoUusiksi("häviö", vastaus)

            else:
                arvaukset.append(arvaus)
                print(f"Yrityksiä jäljellä {yritykset}, arvatut kirjaimet {arvaukset}")

#uusi tai tiedostosta
def peliMuoto(pelinMuoto):
    vastaus = tiedostonKasittely.haeSana()
    yritykset = 6
    arvaukset = []

    if pelinMuoto == "uusi":
        pass

    if pelinMuoto == "tallennettu":
        vastaus, yritykset, arvaukset= tiedostonKasittely.lataaTallennettuPeli(vastaus, yritykset, arvaukset)

    peli(vastaus, yritykset, arvaukset)

kayttoliittyma.GUI()