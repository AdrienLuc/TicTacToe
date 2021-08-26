
player=1
ö=1
form=""
k=""
l=""
j=""
p=""
ü=""
ä=""
üü=""
ää=""
öö=""
usa=0
fofo=1
pipi=0
while fofo==1:
    print("    1   2   3  \n  +---+---+---+\n1 |   |   |   |\n  +---+---+---+\n2 |   |   |   |\n  +---+---+---+\n3 |   |   |   |\n  +---+---+---+")

    while ö==1:
        if usa==1:
        
            print("    1   2   3  ")
            print("  +---+---+---+")
            print("1 | ",k,"| ",p,"| ",üü,"|")
            print("  +---+---+---+")
            print("2 | ",l,"| ",ü,"| ",ää,"|")
            print("  +---+---+---+")
            print("3 | ",j,"| ",ä,"| ",öö,"|")
            print("  +---+---+---+")
        
        if player==1:
            asa="O"
        else:
            asa="X"

        print ("Spieler",player,"(",asa,")""ist dran.")
        x= int(input("Position x:"))
        y= int(input("Position y:"))

        if x>3 or y>3:
            print("Error - Falsche Eigabe! (Wähle zwischen 1-3)!")
            if player==1:
                player+=1
                form="O"
            else:
                player-=1
                form="X"
        
        if player==1:
            player+=1
            form="O"
        else:
            player-=1
            form="X"
        
        if x==1 and y==2 and l=="":
            l=form
        elif x==1 and y==1 and k=="":
            k=form
        elif x==1 and y==3 and j=="":
            j=form
        elif x==2 and y==1 and p=="":
            p=form
        elif x==2 and y==3 and ä=="":
            ä=form
        elif x==2 and y==2 and ü=="":
            ü=form
        elif x==3 and y==3 and öö=="":
            öö=form
        elif x==3 and y==2 and ää=="":
            ää=form
        elif x==3 and y==1 and üü=="":
            üü=form
        else:
            print("Unmöglicher Spielzug! Feld ist bereits besetzt!")
            if player==1:
                player+=1
                form="O"
            else:
                player-=1
                form="X"
        usa=1

        if k==p==üü==["X","O"] or l==ü==ää=="X" or j==ä==öö=="X" or k==l==j=="X" or p==ü==ä=="X" or üü==ää==öö=="X" or k==ü==öö=="X" or j==ä==üü=="X":
            
            print("    1   2   3  ")
            print("  +---+---+---+")
            print("1 | ",k,"| ",p,"| ",üü,"|")
            print("  +---+---+---+")
            print("2 | ",l,"| ",ü,"| ",ää,"|")
            print("  +---+---+---+")
            print("3 | ",j,"| ",ä,"| ",öö,"|")
            print("  +---+---+---+")
            if form=="X":
                print("Player 1 (X) won!")
                pipi=1
        elif k==p==üü=="O" or l==ü==ää=="O" or j==ä==öö=="O" or k==l==j=="O" or p==ü==ä=="O" or üü==ää==öö=="O" or k==ü==öö=="O" or j==ä==üü=="O":
            if form=="O":
                print("    1   2   3  ")
                print("  +---+---+---+")
                print("1 | ",k,"| ",p,"| ",üü,"|")
                print("  +---+---+---+")
                print("2 | ",l,"| ",ü,"| ",ää,"|")
                print("  +---+---+---+")
                print("3 | ",j,"| ",ä,"| ",öö,"|")
                print("  +---+---+---+")
                print("Player 2 (O) won!")
                pipi=1
            

        if k and p and üü and l and ü and ää and j and ä and öö !="":
            print("    1   2   3  ")
            print("  +---+---+---+")
            print("1 | ",k,"| ",p,"| ",üü,"|")
            print("  +---+---+---+")
            print("2 | ",l,"| ",ü,"| ",ää,"|")
            print("  +---+---+---+")
            print("3 | ",j,"| ",ä,"| ",öö,"|")
            print("  +---+---+---+")
            print("Game is over! Nobody won!")
            pipi=1
        
    
        if pipi==1:
            opa=input("Type 'r' to restart or 'e' to end: ")
            popo=1
            if opa=="r":
                fofo=1
                usa=0
                print("    1   2   3  \n  +---+---+---+\n1 |   |   |   |\n  +---+---+---+\n2 |   |   |   |\n  +---+---+---+\n3 |   |   |   |\n  +---+---+---+")
                k=p=üü=l=ü=ää=j=ä=öö=""
                pipi=0
            else:
                fofo=0
                ö=0
                pipi=0

            



 