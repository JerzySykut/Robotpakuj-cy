liczba_paczek_wyslanych = 0
suma_kilogrmow_wyslanych = 0
waga_elementu = 0
waga_paczki = 0
puste_kg_paczki = 0
suma_pustych_kg = 0
najleżejsza_paczka = 0
numer_paczki = 0
print("Robot_Pakujacy")
print("Podaj liczbe elementow do wysylki")
ilosc_sztuk = int (input())
liczba_paczek_wyslanych += 1
while ilosc_sztuk > 0:
    print("Podaj wage elementu")
    waga_elementu = float(input())
    if (waga_elementu == 0 or waga_elementu > 10 or waga_elementu < 1):
        break
    else:
        suma_kilogrmow_wyslanych += waga_elementu
        if waga_paczki + waga_elementu <= 20:
            #jeszcze upchniemy sie w paczce
            waga_paczki = waga_paczki + waga_elementu
        else:
            # sumujemy puste kilogramy z powietrzem ostatniej paczki
            puste_kg_paczki = 20 - waga_paczki
            suma_pustych_kg += puste_kg_paczki
            # zapamiętujemy najbardziej pustą paczkę
            if puste_kg_paczki > najleżejsza_paczka:
                najleżejsza_paczka = puste_kg_paczki
                numer_paczki = liczba_paczek_wyslanych
            #zaczynamy nowa paczke
            liczba_paczek_wyslanych += 1
            waga_paczki = 0 + waga_elementu
        ilosc_sztuk -= 1
# sumujemy puste kilogramy z powietrzem ostatniej!! paczki
# zapamiętujemy najbardziej pustą paczkę
puste_kg_paczki = 20 - waga_paczki
suma_pustych_kg += puste_kg_paczki
if puste_kg_paczki > najleżejsza_paczka:
    najleżejsza_paczka = puste_kg_paczki
    numer_paczki = liczba_paczek_wyslanych

print("liczba paczek wysłałnych ", format(liczba_paczek_wyslanych))
print("liczba kilogramow wyslanych ", format(suma_kilogrmow_wyslanych))
print("suma pustych kilogramow ", format(suma_pustych_kg))
print("najbardziej pusta paczka: nr ", format(numer_paczki), " waży ", format(najleżejsza_paczka), " kg")
