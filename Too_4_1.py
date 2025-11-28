#1
# Sõna või lause analüüs
# Sisesta sõna või lause.
# Loenda:
#     mitu täishäälikut 
#     mitu kaashäälikut 
#     kui sisestati lause – loenda ka tühikud ja kirjavahemärgid
from random import randint
import string
m=string.punctuation #kirjavahemärgid !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~
t=['a','e','i','o','u','õ','ä','ö','ü']
k=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','š','z','ž','t','v','w','x','y']
täis_arv=0
kaas_arv=0
märkude_arv=0
sõne=input("Sisesta sõna või lause: ").lower() #küsi sõne="PythoN" -> sõne.lower()="python"
for täht in sõne:
    if täht in t:
        täis_arv+=1
    elif täht in k:
        kaas_arv+=1
    elif täht in m or täht==" ":
        märkude_arv+=1
print(f"Sõnes/lausees on {täis_arv} täishäälikut,")
print(f"{kaas_arv} kaashäälikut ja ")
print(f"{märkude_arv} märki (sh tühikud).")



#2
nimelist=[]
for i in range(5):
    nimi=input("Sisesta nimi: ").capitalize() # muudab nime esitähe suureks
    nimelist.append(nimi)
print(f"Alguses list on {nimelist}")
#1.variant
for i in range(5):
    print(f"{nimelist[i]}")
#2.variant
for n in nimelist:
    print(f"{n}")
nimelist.sort()
print(f"Sorteeritud list on {nimelist}")
print(f"Viimasena sisestatud {nimi}")
soov=input("Kas tahad nimesid muuda").lower()
if soov=="jah":
    vana_nimi=input("Sisesta vana nimi: ").capitalize()
    uus_nimi=input("Sisesta uus nimi: ").capitalize()
    if vana_nimi in nimelist:
        ind=nimelist.index(vana_nimi)
        nimelist[ind]=uus_nimi
print(f"Uus nimelist on {nimelist}")

mitu=0
ühekodselt_nimed=[]
for nime in nimelist:
    if nime not in ühekodselt_nimed:
        ühekodselt_nimed.append(nime)
print(f"Nimelist ilma kordusteta on {ühekodselt_nimed}")

unikalsed_nimed=list(set(nimelist)) #set eemaldab automaatselt korduvad nimed


#2.3
vanused=[]
mitu=randint(5,15)
for i in range(mitu):
    vanus=randint(1,100)
    vanused.append(vanus)
print(f"Vanused: {vanused}")