import pickle
from datetime import datetime

class Czlowiek:
    def __init__(self, imie: str, rok_urodzenia: int):
        self.imie = imie
        self.rok_urodzenia = rok_urodzenia
        self.wiek = datetime.now().year - rok_urodzenia

    def __repr__(self):
        return f"Czlowiek(imie='{self.imie}', wiek={self.wiek})"

def zapisz_imiona(nazwa_pliku, imiona):
    with open(nazwa_pliku, 'wb') as plik:
        pickle.dump(imiona, plik)

def wczytaj_imiona(nazwa_pliku):
    with open(nazwa_pliku, 'rb') as plik:
        return pickle.load(plik)

def zapisz_ludzi(nazwa_pliku, ludzie):
    with open(nazwa_pliku, 'wb') as plik:
        pickle.dump(ludzie, plik)

def wczytaj_ludzi(nazwa_pliku):
    with open(nazwa_pliku, 'rb') as plik:
        ludzie = pickle.load(plik)
        for czlowiek in ludzie:
            czlowiek.wiek = datetime.now().year - czlowiek.rok_urodzenia
        return ludzie

imiona = input("podaj imiona po spacji: ").split()
zapisz_imiona("imiona.pkl", imiona)
print("wczytane imiona:", wczytaj_imiona("imiona.pkl"))

ludzie = [Czlowiek(imie, int(input(f"podaj rok urodzenia dla {imie}: "))) for imie in imiona]
zapisz_ludzi("ludzie.pkl", ludzie)
print("obiekty:", wczytaj_ludzi("ludzie.pkl"))
