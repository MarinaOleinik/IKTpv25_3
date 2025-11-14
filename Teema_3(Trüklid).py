# Sisestatakse 15 arvu.
#Määrata, mitu neist on täisarvud.
from random import *

print(randint(1,19))


t_arvud=0
for i in range(15):    # i= 0,1,2,...,14
    arv = input("Sisesta arv: ")
    try:
        int_arv = int(arv)
        print(f"{arv} on täisarv.")
        t_arvud+=1
    except ValueError:
        print(f"{arv} ei ole täisarv.")
print(f"Sisestatud {t_arvud} täisarvu.")

