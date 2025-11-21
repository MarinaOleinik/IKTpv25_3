sõne=input("Sisesta sõne: ") #küsi sõne
sõne_list=list(sõne) #muudab sõne listiks
print(f"Sõne oli: {sõne}")
print(f"Sõne listina: {sõne_list}")
list2=[] #tühi list
print(f"Tühi list list2: {list2}")

while 1:
    print("\n\nVali tegevus:")
    print("1-Lisa elemente listi\n2-Lisa elemente positrioonile")
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
        
    print(f"Uus list2 on: {list2}")