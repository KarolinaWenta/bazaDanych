dane = []

def nowaBaza():
    dane = []
    print("Rozpoczynasz nową bazę")

def search():
    for i in range(len(dane)):
        if wartosc == dane[i]:
            return (i)
    return(-1)


def maksymalna():
    max = int(dane[0])
    for i in range(len(dane)):
        if int(dane[i]) > int(max):
            max = dane[i]
    print(max)


def value(indeks):
    for i in range(len(dane)):
        if indeks == i:
            return dane[indeks]
    return -1


def minimalna():
    min = int(dane[0])
    for i in range(len(dane)):
        if int(dane[i]) < int(min):
            min = dane[i]
    print(min)


def wypisywanie():
    wypisz = ""
    for i in range(0, len(dane)):
        wypisz += str(dane[i])
        if len(dane)-1 != i:
            wypisz += ','
    print(wypisz)


def delete(dane):
    x = int(input())
    dane2 = []
    for i in dane:
        dane2.append(i)
    return dane2[:-x]


def sumowanie():
    suma = 0
    for liczba in dane:
        suma += liczba
    return suma


def srednia():
    ilosc_liczb = len(dane)
    suma = 0
    srednia = 0
    for liczba in dane:
        suma += liczba
    srednia = suma / ilosc_liczb
    return 'Srednia z liczb to: ' + str(srednia)


def zamiana():
    indeks1 = int(input())
    indeks2 = int(input())
    for i in range(len(dane)):
        if indeks1 == i:
            dane[indeks1], dane[indeks2] = dane[indeks2], dane[indeks1]
            return dane

print("""Witamy w bazie damych, możesz wpisać podane polecania:
START - tworzenie bazy
ADD - dodaje liczbę do jak narazie pustej bazy, 
PRINT - wypisyje wszytkie liczby w bazie,
SEARCH - podaj liczbę z bazy, a następnie pokaże Ci się pod jakim indeksem znajduje się ta liczba
MAX - pokazuje największą liczbę w bazie
MIN - pokazuje najmniejszą liczbę w bazie
VALUE - podaj indeks, a następnie pokaże Ci się jaka znajduje się pod nim liczba
DELETE - usnie od końca tyle liczb, ile podasz
AVG - pokaże średnią z liczb
SUM - doda do siebie liczby z bazy
SWAP - zamieni licczby, indeksami, które podasz
END - kończy dostęp do bazy""")

komenda = input() and nowaBaza()
while True and komenda != "END":
    komenda = input()
    if komenda == "ADD":
        wartosc = int(input())
        dane.append(wartosc)
    elif komenda == "PRINT":
        wypisywanie()
    elif komenda == "SEARCH":
        wartosc = int(input())
        print(search())
    elif komenda == "MAX":
        maksymalna()
    elif komenda == "MIN":
        minimalna()
    elif komenda == "VALUE":
        indeks = int(input())
        print(value(indeks))
    elif komenda == "DELETE":
        print(delete(dane))
    elif komenda == "AVG":
        print(srednia())
    elif komenda == "SUM":
        print(sumowanie())
    elif komenda == "SWAP":
        print(zamiana())
    elif komenda == "END":
        print("dostęp do bazy zamknięty")
    elif komenda == "START":
        print(nowaBaza())


