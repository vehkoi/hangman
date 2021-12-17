import hirsipuu
#alkunäyttö
def GUI():
    print("---------" '\n' "HIRSIPUU" '\n' "---------" '\n' "Tervetuloa pelaamaan. Arvauksen on oltava yksi kirjain väliltä a-ä tai 'tallenna peli',"
    "jolloin peli tallennetaan tiedostoon. Valitse pelimuoto:"'\n' "0 - jos haluat sulkea pelin" '\n' "1 - jos haluat pelata uuden pelin" '\n' 
    "2 - jos haluat pelata tallennetun pelin")
    pelimuoto = int(input())
    match pelimuoto:
        case 0:
            exit()
        case 1:
            hirsipuu.peliMuoto("uusi")
        case 2:
            hirsipuu.peliMuoto("tallennettu")


#kutsutaan pelin jälkeen
def pelataankoUusiksi(lopputulos, vastaus):
    if lopputulos == "voitto":
        uusiksi = input((f"VOITIT PELIN, vastaus oli {vastaus}. Haluatko pelata uusiksi? K/E "))
    if lopputulos == "häviö":
        uusiksi = input((f"HÄVISIT PELIN, vastaus oli {vastaus}. Haluatko pelata uusiksi? K/E "))
    
    if uusiksi.lower() == "k":
        hirsipuu.peliMuoto("uusi")
    else:
        print("Palataan alkunäyttöön!")
        GUI()