class svetopalka:
    
    kolvo_silouser = 0

    def __init__(self, n, c):
        self.n = n
        self.c = c
        svetopalka.kolvo_silouser += 1

    def kolvousersov (self):
        print ("Всего силоюзеров: %s" % svetopalka.kolvo_silouser)

Enakin = svetopalka ("Энакин","Синий")
Vindu = svetopalka ("Винду", "Фиолетовый")
Ashoka = svetopalka ("Асока", "Зеленый")
Obi1 = svetopalka ("Оби-Ван", "Синий")

Obi1.kolvousersov()

print(Ashoka.c)
