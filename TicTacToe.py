
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[101m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


ln1=""
ln2=""
ln3=""
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
sos=1
ln4=""
ln5=""
ln6=""
round=0
while fofo==1:
    print("    1   2   3  \n  +---+---+---+\n1 |   |   |   |\n  +---+---+---+\n2 |   |   |   |\n  +---+---+---+\n3 |   |   |   |\n  +---+---+---+")

    while ö==1:
        if usa==1:
        
            print("    1   2   3  ")
            print("  +---+---+---+")
            print("1 |",k," | ",p,"| ",üü,"|")
            print("  +---+---+---+")
            print("2 |",l," | ",ü,"| ",ää,"|")
            print("  +---+---+---+")
            print("3 |",j," | ",ä,"| ",öö,"|")
            print("  +---+---+---+")
        round+=1
        if player==1:
            asa="O"
        else:
            asa="X"

        print ("Spieler",player,"(",asa,")"" ist dran.")
        x= int(input("Position x:"))
        y= int(input("Position y:"))
            
        
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
        elif x>3 or y>3:
            print(bcolors.WARNING +"Error - Falsche Eigabe! (Wähle zwischen 1-3)!"+bcolors.ENDC)
            if player==1:
                player+=1
                form="O"
            else:
                player-=1
                form="X"
        else:
            print(bcolors.WARNING + "\tUnmöglicher Spielzug! Feld bereits besetzt!"+bcolors.ENDC)
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
                print(bcolors.WARNING +"Player 1 (X) won!"+bcolors.ENDC)
                pipi=1
                sos=0
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
                print(bcolors.WARNING +"Player 2 (O) won!"+bcolors.ENDC)
                pipi=1
                sos=0
            

        if k and p and üü and l and ü and ää and j and ä and öö !="" and sos==1:
            print("    1   2   3  ")
            print("  +---+---+---+")
            print("1 | ",k,"| ",p,"| ",üü,"|")
            print("  +---+---+---+")
            print("2 | ",l,"| ",ü,"| ",ää,"|")
            print("  +---+---+---+")
            print("3 | ",j,"| ",ä,"| ",öö,"|")
            print("  +---+---+---+")
            print(bcolors.WARNING +"Game is over! Nobody won!"+bcolors.ENDC)
            pipi=1
        
    
        if pipi==1:
            opa=input(bcolors.WARNING +"Type 'r' to restart or 'e' to end: "+bcolors.ENDC)
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

        if x==2 and y==2 or y==1 or y==3 and k==l==j=="":
            ln1=="" 
            ln2==""
            ln3=="" 
