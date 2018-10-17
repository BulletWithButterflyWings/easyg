import random, getpass

meny = 0 


print("Välkommen!")
while meny != 3: 
    print("Tryck 1 för PC.\n Tryck 2 för två spelare.\n Tryck 3 för att avsluta.\n")
    meny = int(input("PC eller två spelare?")) 

    if meny == 1:
        rundor = int(input("Välj antal rundor för att vinna: "))
        spelare1 = 0
        spelare2 = 0
        spelarepoäng1 = 0
        spelarepoäng2 = 0
        print("Du har valt att spela mot en PC.")
        while spelarepoäng1 != rundor:
            if spelarepoäng2 == rundor:
                break
            spelare2 = random.randint(1, 3)
            spelare1 = int(input("Tryck 1 för att välja sten.\n Tryck 2 för att välja sax.\n Tryck 3 för att välja påse."))
            if spelare1 == spelare2: 
                print("Ni valde lika, försök igen.")
            elif spelare1 == 1:
                if spelare2 == 2:
                    print("Du har vunnit!")
                    spelarepoäng1 = spelarepoäng1 + 1
                    print(int(spelarepoäng1))
                    print(int(spelarepoäng2))
                elif spelare2 == 3:
                    print("Du har förlorat!") 
                    spelarepoäng2 = spelarepoäng2 + 1
                    print(int(spelarepoäng1))
                    print(int(spelarepoäng2))
            elif spelare1 == 2:
                if spelare2 == 3:
                    print("Du har vunnit!")
                    spelarepoäng1 = spelarepoäng1 + 1
                    print(int(spelarepoäng1))
                    print(int(spelarepoäng2))
                elif spelare2 == 1:
                    print("Du har förlorat!") 
                    spelarepoäng2 = spelarepoäng2 + 1
                    print(int(spelarepoäng1))
                    print(int(spelarepoäng2))
            elif spelare1 == 3:
                if spelare2 == 1:
                    print("Du har vunnit!")
                    spelarepoäng1 = spelarepoäng1 + 1
                    print(int(spelarepoäng1))
                    print(int(spelarepoäng2))
                elif spelare2 == 2:
                    print("Du har förlorat!") 
                    spelarepoäng2 = spelarepoäng2 + 1
                    print(int(spelarepoäng1))
                    print(int(spelarepoäng2))
    elif meny == 2:
        rundor = int(input("Välj antal rundor för att vinna: "))
        print("Du har valt att spela mot en Spelare.")
        spelare1 = 0
        spelare2 = 0
        spelarepoäng1 = 0
        spelarepoäng2 = 0
        print("Du har valt att spela mot en PC.")
        while spelarepoäng1 != rundor:
            if spelarepoäng2 == rundor:
                break
            spelare1 = int(getpass.getpass(" Spelare ett tryck 1 för att välja sten.\n Spelare ett tryck 2 för att välja sax.\n Spelare ett tryck 3 för att välja påse."))
            spelare2 = int(getpass.getpass("Spelare två tryck 1 för att välja sten.\n Spelare två tryck 2 för att välja sax.\n Spelare två tryck 3 för att välja påse."))
            if spelare1 == spelare2: 
                print("Ni valde lika, försök igen.")
            elif spelare1 == 1:
                if spelare2 == 2:
                    print("Spelare ett har vunnit!")
                    spelarepoäng1 = spelarepoäng1 + 1
                    print(int(spelarepoäng1))
                    print(int(spelarepoäng2))
                elif spelare2 == 3:
                    print("Spelare två har vunnit!") 
                    spelarepoäng2 = spelarepoäng2 + 1
                    print(int(spelarepoäng1))
                    print(int(spelarepoäng2))
            elif spelare1 == 2:
                if spelare2 == 3:
                    print("Spelare två har vunnit!")
                    spelarepoäng1 = spelarepoäng1 + 1
                    print(int(spelarepoäng1))
                    print(int(spelarepoäng2))
                elif spelare2 == 1:
                    print("Spelare ett har vunnit!") 
                    spelarepoäng2 = spelarepoäng2 + 1
                    print(int(spelarepoäng1))
                    print(int(spelarepoäng2))
            elif spelare1 == 3:
                if spelare2 == 1:
                    print("Spelare ett har vunnit!")
                    spelarepoäng1 = spelarepoäng1 + 1
                    print(int(spelarepoäng1))
                    print(int(spelarepoäng2))
                elif spelare2 == 2:
                    print("Spelare två har förlorat!") 
                    spelarepoäng2 = spelarepoäng2 + 1
                    print(int(spelarepoäng1))
                    print(int(spelarepoäng2))

    elif meny == 3:
        print("Avsluta")
