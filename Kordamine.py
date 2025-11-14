# Pitsa
#     Võtsite sõpradega (näiteks P inimest) suure pitsa, mille hind on 12,90 €.
#     Jätate teenindajale 10% jootraha.
#     Koosta programm, mis arvutab, kui palju igaüks peab maksma.
# from random import *
# P=randint(2,10)
# print(f"Sõprade arv: {P}")
# pitsa_hind=12.90
# hind_jootrahaga=1.1*pitsa_hind
# maksumus=hind_jootrahaga/P
# print(f"Iga sõber peab maksma: {maksumus:.2f} €")
# print(f"Iga sõber maksab: {round(maksumus,2)} €")

#Arvutame kolmnurga ümbermõõdu. Küsi kolm täisarvulist muutujat a, b, c. 
#Kasuta valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
while True:
    try:
        a=int(input("Sisesta kolmnurga a külje pikkus: "))
        break
    except:
        print("Viga! Palun sisesta täisarv!")
while True:
    try:
        b=int(input("Sisesta kolmnurga b külje pikkus: "))
        break
    except:
        print("Viga! Palun sisesta täisarv!")
while True:
    try:
        c=int(input("Sisesta kolmnurga c külje pikkus: "))
        break
    except:
        print("Viga! Palun sisesta täisarv!")

if a>0 and b>0 and c>0:
    print("Kõik küljed on positiivsed.")
    print("Kontrollime. Kas nad on ühe kolmnurga küljed?")
    if a+b>c and a+c>b and b+c>a:
        print("Jah, need on ühe kolmnurga küljed.")
        P=a+b+c
        print(f"Kolmnurga ümbermõõt on: {P}")
    else:
        print("Ei, sellist kolmnurka ei saa olemas olla.")
else:
    print("Viga! Kõik küljed peavad olema positiivsed!")
print("Lõpp")