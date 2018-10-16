import random

meny = 0 
spelare1 = 0
spelare2 = 0

print("Välkommen!")
while meny != 3: 
    print("Tryck 1 för PC.\n Tryck 2 för två spelare.\n Tryck 3 för att avsluta.\n")
    meny = int(input("PC eller två spelare?")) 

    if meny == 1:
        print("Du har valt att spela mot en PC.")
        while spelare1 != 2 or spelare2 != 2: 
            spelare2 = random.randint(1, 3)
            spelare1 = int(input("Tryck 1 för att välja sten.\n Tryck 2 för att välja sax.\n Tryck 3 för att välja påse."))
    elif meny == 2:
        print("Du har valt att spela mot en Spelare.")
    elif meny == 3:
        print("Avsluta")