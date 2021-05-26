class HB:

    imenninik = 0

    def __init__(self, day,mon,year):
        self.day = day
        self.mon = mon
        self.year = year
        HB.imenninik += 1

    def spissok (self):
        print ("Количество людей в списке: %s" % HB.imenninik)

class sladkoe:

    slastei = 0

    def __init__(self, ves, stoimost):
        self.ves = ves
        self.stoimost = stoimost
        sladkoe.slastei += 1

    def spissok (self):
        print ("Количество сладостей в списке: %s" % sladkoe.slastei)

class napitki:

    pitio = 0

    def __init__(self, name, schen):
        self.name = name
        self.schen = schen
        napitki.pitio += 1

    def spissok (self):
        print ("Количество напитков в списке: %s" % napitki.pitio)

    def __repr__(self):
        return f"{self.__class__}: {self.name}"

class Problem:
    def __init__(self, lvl):
        self.lvl = lvl

    def __del__(self):
        print("Удаление экземпляра: " + self.__str__())

Kolya = HB (24, 4,2000)
Sveta = HB (8, 11,1998)
Dima = HB (11, 12,1987)

Dima.spissok()

Tort = sladkoe (1000, 1700)
Pirogenoe = sladkoe (150, 65)
Ekler = sladkoe (100, 55)

Ekler.spissok()

Soda = napitki ("Coca-cola", 120)
Sok = napitki ("Dobraj", 100)
Voda = napitki ("SvetoiIstochnik", 50)

Voda.spissok()

strah = Problem(23)
besson = Problem(11)