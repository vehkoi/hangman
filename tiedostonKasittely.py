import json
from json.decoder import JSONDecodeError
import random
import hirsipuu
import kayttoliittyma

#poistaa tiedostosta rivinvaihdot, hakee random sanan 'sanat.txt' tiedostosta
def haeSana():
    with open("sanat.txt") as tiedosto:
        rivit = [line.rstrip('\n') for line in tiedosto]
        sana = random.choice(rivit)
        return sana

#tallentaa pelin 'tallennus' tiedostoon ja palaa alkunäyttöön
def tallennaPeli(vastaus, yritykset, arvaukset):
    tiedosto = open("tallennus.txt", "w")
    tallennusSanakirja = {"vastaus" : vastaus, "yritykset" : yritykset, "arvaukset" : arvaukset}
    json.dump(tallennusSanakirja, tiedosto, ensure_ascii=False)
    tiedosto.close()
    print("Pelisi on nyt tallennettu! Palataan alkunäyttöön")
    kayttoliittyma.GUI()

#ladataan peli 'tallennus' tiedostosta
def lataaTallennettuPeli(vastaus, yritykset, arvaukset):
    with open("tallennus.txt", "r") as tiedosto:
        try:
            data = json.load(tiedosto)
            vastaus = data["vastaus"]
            yritykset = data["yritykset"]
            arvaukset = data["arvaukset"]
            print(f"Peli ladattu onnistuneesti! Tämänhetkiset yritykset: {yritykset} ja arvaukset: {arvaukset}.")

        except JSONDecodeError:
            print("Tallennusta ei ole olemassa, aloitetaan uusi peli")

    return vastaus, yritykset, arvaukset