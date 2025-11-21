from random import randint
sõne=input("Sisesta sõne: ") #küsi sõne
sõne_list=list(sõne) #muudab sõne listiks
print(f"Sõne oli: {sõne}")
print(f"Sõne listina: {sõne_list}")
list2=[] #tühi list
print(f"Tühi list list2: {list2}")

while 1:
    print("\n\nVali tegevus:")
    print("1-Lisa elemente listi\n2-Lisa elemente positrioonile") #lisa element kindlale positsioonile
    print("3-kustuta elemente\n4-kustuta element positsioonilt") #kustuta element ja element kindlalt positsioonilt
    print("5-listide ühendamine\n6-listide läbimine") #listide ühendamine ja läbimine")
    print("7-index() kasutamine\n8-sort() kasutamine\n9-reverse()\n10-clear() ")
    print("11-töö arvudega (max(), min(), sum()")
    while True:
        try:
            vastus=int(input("Sisesta tegevuse number: "))
            if vastus>0 and vastus<10:
                break
        except:
            print("Viga! Palun sisesta tegevuse number!")
    if vastus==1:
        element=input("Sisesta element, mida soovid listi lisada: ")
        list2.append(element) #lisa element listi list2

    elif vastus==2:
        element=input("Sisesta element, mida soovid listi lisada: ")
        while True:
            try:
                pos=int(input(f"Sisesta positsioon, kuhu soovid '{element}' lisada (0-{len(list2)}): "))
                if pos>=0 and pos<=len(list2):
                    break
            except:
                print("Viga! Palun sisesta positsioon!")
        list2.insert(pos,element) #lisa element kindlale positsioonile
    elif vastus==3:
        element=input("Sisesta element, mida soovid listist kustutada: ")
        mitu=list2.count(element) #loeb mitu korda element esineb listis
        if mitu==0:
            print(f"Elementi '{element}' ei leitud listist.")
        else:
            for i in range(mitu):
                list2.remove(element) #kustuta element listist
            print(f"Eemaldati {mitu} korda element '{element}' listist.")
    elif vastus==4:
        while True:
            try:
                pos=int(input(f"Sisesta järjekorra number kustutava elemente: "))
                if pos>=0 and pos<len(list2):
                    break
            except:
                print("Viga! Palun sisesta positsioon!")
        kust_element=list2.pop(pos) #kustuta element kindlalt positsioonilt
        print(f"Eemaldati element '{kust_element}' positsioonilt {pos}.")
    elif vastus==5:
        print(f"{sõne_list} ühendatakse {list2}-ga")
        sõne_list.extend(list2) #ühenda listid
        print(f"Uus sõne_list on: {sõne_list}")
    elif vastus==6:
        print("Sõne_listi läbimine 1. variant:")
        for i, el in enumerate(sõne_list): #läbib listi koos positsioonidega
            print(f"Positsioon {i}: Element '{el}'")
        print("Sõne_listi läbimine 2. variant:")
        for el in sõne_list:
            print(f"Element '{el}'")
    elif vastus==7:
        element=input("Sisesta element, mille positsiooni soovid leida: ")
        if element in list2: #kontrollib, kas element on listis
            pos=list2.index(element) #leiab elemendi positsiooni
            print(f"Element '{element}' asub positsioonil {pos}.")
        else:
            print(f"Elementi '{element}' ei leitud listist.")
    elif vastus==8:
        list2.sort() #sorteerib listi
    elif vastus==9:
        list2.reverse() #pöörab listi järjekorra
    elif vastus==10:
        list2.clear() #tühjendab listi
    elif vastus==11:
        arvud=[]
        for i in range(10):
            arvud.append(randint(1,100)) #lisab listi 10 juhuslikku arvu)
        print(f"Arvude list: {arvud}")
        print(f"Suurim arv on: {max(arvud)}") #leiab listi suurima väärtuse
        print(f"Väikseim arv on: {min(arvud)}") #leiab listi väikseima väärtuse
        print(f"Arvude summa on: {sum(arvud)}") #liidab kõik listi elemendid kokku (ainult numbrilised väärtused)
        



    print(f"Uus list2 on: {list2}")
#index() - leiab elemendi positsiooni
#sort() - sorteerib listi
#reverse() - pöörab listi järjekorra
#clear() - tühjendab listi
#max() - leiab listi suurima väärtuse
#min() - leiab listi väikseima väärtuse
#sum() - liidab kõik listi elemendid kokku (ainult numbrilised väärtused