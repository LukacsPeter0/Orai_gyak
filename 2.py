import random

def elso():
    szamok = []
    szamlalo = 0
    for i in range(100000):
        szam = random.randint(1, 6)
        szamok.append(szam)
        if szam == 6:
            szamlalo += 1
    print(szamlalo)

def masodik():
    lista = [3, 6, 12, 3, 14, 5, 18]
    szamlalo = 0
    for i in lista:
        if i > 10:
            szamlalo += 1
    print(szamlalo)

def harmadik():
    szamok = []
    kisebb = 0
    nagyobb = 0
    for i in range(100):
        szam = szamok.append(random.randint(1, 100))
        if szam < 30:
            kisebb += 1
        elif szam > 60:
            nagyobb += 1
    print(kisebb, nagyobb)

def negyedik():
    szoveg = 'Már egy hete csak a mamára gondolok.'
    AK = szoveg.upper.count('A')
    EK = szoveg.upper.count('E')
    print(AK, EK)

def otodik():
    szamok = []
    szamlalo = 0
    for i in range(100000):
        szam = random.randint(1, 6)
        szamok.append(szam)
    print(szamok.count(1))
    print(szamok.count(2))
    print(szamok.count(3))
    print(szamok.count(4))
    print(szamok.count(5))
    print(szamok.count(6))

def hatodik():
    szamok = []
    szamlalo = 0
    for i in range(100):
        szam = szamok.append(random.randint(1, 100))
    for szam in szamok:
        if szamok[szam] % 2 == 0 and szamok[szam+1] % 2 == 0:
            szamlalo += 1
    print(szamlalo)



        

    