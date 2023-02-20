
# Omar Soliman Gil

import random

jugar = True
posicio = 0
daustirats = 0
rebotar = 0

caselles = int(input("Quantes caselles te el tauler? "))


while(caselles < 10 or caselles > 100 ):

    caselles = int(input("Error, el tauler no pot tindre menys de 10 o 100 caselles. Torna a provar:  "))

while jugar:
    dau = random.randint(1,6)

    if posicio != caselles:
        posicio += dau
        print(f"Ha eixit un {dau} vaig a la casella {posicio}")
        daustirats += 1
    
    elif posicio == caselles:
        print(f"Soc un fiera! He guanyat la partida!")
        print(f"He tirat el dau {daustirats} voltes.")
        jugar = False

    if posicio % 5 == 0 and posicio != caselles:
        posicio += 5
        print(f"D'oca en oca i tire perque hem toca. Estic en la casella {posicio}")

    if posicio > caselles:
        
        rebotar = posicio - caselles
        posicio -= rebotar*2

        print(f"M'he pasat torne arrere {rebotar} caselles. Estic en la casella {posicio}")

            
            
        
    

    






    
    