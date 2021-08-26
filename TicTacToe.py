
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
class TicTacToe:
    start=("")
    ln1=""
    ln2=""
    ln3=""
    player=1
    ö=1
    form=""
    k=" "
    l=" "
    j=" "
    p=" "
    ü=" "
    ä=" "
    üü=" "
    ää=" "
    öö=" "
    usa=0
    fofo=1
    pipi=0
    sos=1
    ln4=""
    ln5=""
    ln6=""
    round=0    
    text=1
    if round==0:

        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\t\t\t\t\t\t\t\t\t\t ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗")
        print("\t\t\t\t\t\t\t\t\t\t ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝")
        print("\t\t\t\t\t\t\t\t\t\t ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░")
        print("\t\t\t\t\t\t\t\t\t\t ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░")
        print("\t\t\t\t\t\t\t\t\t\t ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗")
        print("\t\t\t\t\t\t\t\t\t\t ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝")
        print("\n\n\n\n\n")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t   ████████╗░█████╗░")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t   ╚══██╔══╝██╔══██╗")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t   ░░░██║░░░██║░░██║")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t   ░░░██║░░░██║░░██║")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t   ░░░██║░░░╚█████╔╝")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t   ░░░╚═╝░░░░╚════╝░")
        print("\n\n\n\n\n")
        print("\t\t\t\t\t\t\t\t\t\t████████╗██╗░█████╗░████████╗░█████╗░░█████╗░████████╗░█████╗░███████╗")
        print("\t\t\t\t\t\t\t\t\t\t╚══██╔══╝██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔════╝")
        print("\t\t\t\t\t\t\t\t\t\t░░░██║░░░██║██║░░╚═╝░░░██║░░░███████║██║░░╚═╝░░░██║░░░██║░░██║█████╗░░")
        print("\t\t\t\t\t\t\t\t\t\t░░░██║░░░██║██║░░██╗░░░██║░░░██╔══██║██║░░██╗░░░██║░░░██║░░██║██╔══╝░░")
        print("\t\t\t\t\t\t\t\t\t\t░░░██║░░░██║╚█████╔╝░░░██║░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝███████╗")
        print("\t\t\t\t\t\t\t\t\t\t░░░╚═╝░░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚══════╝")
        print("")
        if text==5:
            print("")
            print(" ______     __  __        ______     _____     ______     __     ______     __   __        __         __  __     ______     ______     __  __     __     ______     __  __     _____    ")
            print("/\  == \   /\ \_\ \      /\  __ \   /\  __-.  /\  == \   /\ \   /\  ___\   /\ -.\ \      /\ \       /\ \/\ \   /\  ___\   /\  __ \   /\ \/\ \   /\ \   /\  __ \   /\ \/\ \   /\  __-.  ")
            print("\ \  __<   \ \____ \     \ \  __ \  \ \ \/\ \ \ \  __<   \ \ \  \ \  __\   \ \ \-.  \     \ \ \____  \ \ \_\ \  \ \ \____  \ \ \/\_\  \ \ \_\ \  \ \ \  \ \  __ \  \ \ \_\ \  \ \ \/\ \ ")
            print(" \ \_____\  \/\_____\     \ \_\ \_\  \ \____-  \ \_\ \_\  \ \_\  \ \_____\  \ \_\\\_\     \ \_____\  \ \_____\  \ \_____\  \ \___\_\  \ \_____\  \ \_\  \ \_\ \_\  \ \_____\  \ \____- ")
            print("  \/_____/   \/_____/      \/_/\/_/   \/____/   \/_/ /_/   \/_/   \/_____/   \/_/ \/_/      \/_____/   \/_____/   \/_____/   \/___/_/   \/_____/   \/_/   \/_/\/_/   \/_____/   \/____/ ")
        elif text==4:
            print("█▀▀▄ █░░█ 　 ░█▀▀█ █▀▀▄ █▀▀█ ░▀░ █▀▀ █▀▀▄ 　 ▒█░░░ █░░█ █▀▀ █▀▀█ █░░█ ░▀░ █▀▀█ █░░█ █▀▀▄ ")
            print("█▀▀▄ █▄▄█ 　 ▒█▄▄█ █░░█ █▄▄▀ ▀█▀ █▀▀ █░░█ 　 ▒█░░░ █░░█ █░░ █░░█ █░░█ ▀█▀ █▄▄█ █░░█ █░░█ ")
            print("▀▀▀░ ▄▄▄█ 　 ▒█░▒█ ▀▀▀░ ▀░▀▀ ▀▀▀ ▀▀▀ ▀░░▀ 　 ▒█▄▄█ ░▀▀▀ ▀▀▀ ▀▀▀█ ░▀▀▀ ▀▀▀ ▀░░▀ ░▀▀▀ ▀▀▀░")
            print("")
        elif text==3:
                print("  _                         _      _              _                           _                 _ ")
                print(" | |               /\      | |    (_)            | |                         (_)               | |")
                print(" | |__  _   _     /  \   __| |_ __ _  ___ _ __   | |    _   _  ___ __ _ _   _ _  __ _ _   _  __| |")
                print(" | '_ \| | | |   / /\ \ / _` | '__| |/ _ \ '_ \  | |   | | | |/ __/ _` | | | | |/ _` | | | |/ _` |")
                print(" | |_) | |_| |  / ____ \ (_| | |  | |  __/ | | | | |___| |_| | (_| (_| | |_| | | (_| | |_| | (_| |")
                print(" |_.__/ \__, | /_/    \_\__,_|_|  |_|\___|_| |_| |______\__,_|\___\__, |\__,_|_|\__,_|\__,_|\__,_|")
                print("         __/ |                                                       | |       ")
                print("        |___/                                                        |_|    ")
                print("")
        elif text==2:
            print("████████████████████████████████████████████████████████████████████████████████████████████████████████████")
            print("█▄─▄─▀█▄─█─▄████▀▄─██▄─▄▄▀█▄─▄▄▀█▄─▄█▄─▄▄─█▄─▀█▄─▄███▄─▄███▄─██─▄█─▄▄▄─█─▄▄▄─█▄─██─▄█▄─▄██▀▄─██▄─██─▄█▄─▄▄▀█")
            print("██─▄─▀██▄─▄█████─▀─███─██─██─▄─▄██─███─▄█▀██─█▄▀─█████─██▀██─██─██─███▀█─██▀─██─██─███─███─▀─███─██─███─██─█")
            print("▀▄▄▄▄▀▀▀▄▄▄▀▀▀▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▀▄▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀───▄▄▀▀▄▄▄▄▀▀▄▄▄▀▄▄▀▄▄▀▀▄▄▄▄▀▀▄▄▄▄▀▀")
        elif text==6:
                print("█▄▄ █▄█   ▄▀█ █▀▄ █▀█ █ █▀▀ █▄░█   █░░ █░█ █▀▀ █▀█ █░█ █ ▄▀█ █░█ █▀▄")
                print("█▄█ ░█░   █▀█ █▄▀ █▀▄ █ ██▄ █░▀█   █▄▄ █▄█ █▄▄ ▀▀█ █▄█ █ █▀█ █▄█ █▄▀")
        elif text==1:
                print("")
                print("\t\t\t\t\t\t\t\t\t\t _          _____   _     _            __                    _           _ ")
                print("\t\t\t\t\t\t\t\t\t\t| |_ _ _   |  _  |_| |___|_|___ ___   |  |   _ _ ___ ___ _ _|_|___ _ _ _| |")
                print("\t\t\t\t\t\t\t\t\t\t| . | | |  |     | . |  _| | -_|   |  |  |__| | |  _| . | | | | .'| | | . |")
                print("\t\t\t\t\t\t\t\t\t\t|___|_  |  |__|__|___|_| |_|___|_|_|  |_____|___|___|_  |___|_|__,|___|___|")
                print("\t\t\t\t\t\t\t\t\t\t    |___|                                             |_| ")
                print("\n\n\n\n\n")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t    Press 's' to start\n\n\n")
        start=input()
        if start==("s"):
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t     Started the game\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    if start==("s"):
        while fofo==1:
            #print("    1   2   3  \n  +---+---+---+\n1 |   |   |   |\n  +---+---+---+\n2 |   |   |   |\n  +---+---+---+\n3 |   |   |   |\n  +---+---+---+")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t         1   2   3  ")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t     1 |",k,"|",p,"|",üü,"|")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t     2 |",l,"|",ü,"|",ää,"|")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t     3 |",j,"|",ä,"|",öö,"|")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")

            while ö==1:
                if usa==1:
                
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t         1   2   3  ")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t     1 |",k,"|",p,"|",üü,"|")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t     2 |",l,"|",ü,"|",ää,"|")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t     3 |",j,"|",ä,"|",öö,"|")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                round+=1
                if player==1:
                    form=asa="O"
                    player+=1
                else:
                    form=asa="X"
                    player-=1

                print ("\n\t\t\t\t\t\t\t\t\t\t\t\t\tSpieler",player,"(",asa,")"" ist dran.")
                x= int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\tPosition x:"))
                y= int(input("\n\t\t\t\t\t\t\t\t\t\t\t\t\tPosition y:"))
                    
                
                if x==1 and y==2 and l==" ":
                    l=form
                elif x==1 and y==1 and k==" ":
                    k=form
                elif x==1 and y==3 and j==" ":
                    j=form
                elif x==2 and y==1 and p==" ":
                    p=form
                elif x==2 and y==3 and ä==" ":
                    ä=form
                elif x==2 and y==2 and ü==" ":
                    ü=form
                elif x==3 and y==3 and öö==" ":
                    öö=form
                elif x==3 and y==2 and ää==" ":
                    ää=form
                elif x==3 and y==1 and üü==" ":
                    üü=form
                elif x>3 or y>3:
                    print(bcolors.WARNING +"\t\t\t\t\t\t\t\t\t\t\t\t\tError - Falsche Eigabe! (Wähle zwischen 1-3)!"+bcolors.ENDC)
                    if player==1:
                        player+=1
                        form="O"
                    else:
                        player-=1
                        form="X"
                else:
                    print(bcolors.WARNING + "\t\t\t\t\t\t\t\t\t\t\t\t\tUnmöglicher Spielzug! Feld bereits besetzt!"+bcolors.ENDC)
                    if player==1:
                        player+=1
                        form="O"
                    else:
                        player-=1
                        form="X"
                usa=1

                if k==p==üü==["X","O"] or l==ü==ää=="X" or j==ä==öö=="X" or k==l==j=="X" or p==ü==ä=="X" or üü==ää==öö=="X" or k==ü==öö=="X" or j==ä==üü=="X":
                    
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t         1   2   3  ")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t     1 |",k,"|",p,"|",üü,"|")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t     2 |",l,"|",ü,"|",ää,"|")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t     3 |",j,"|",ä,"|",öö,"|")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                    if form=="X":
                        print(bcolors.WARNING +"\t\t\t\t\t\t\t\t\t\t\t\t\tPlayer 1 (X) won!"+bcolors.ENDC)
                        pipi=1
                        sos=0
                elif k==p==üü=="O" or l==ü==ää=="O" or j==ä==öö=="O" or k==l==j=="O" or p==ü==ä=="O" or üü==ää==öö=="O" or k==ü==öö=="O" or j==ä==üü=="O":
                    if form=="O":
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\t         1   2   3  ")
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\t     1 |",k,"|",p,"|",üü,"|")
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\t     2 |",l,"|",ü,"|",ää,"|")
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\t     3 |",j,"|",ä,"|",öö,"|")
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                        print(bcolors.WARNING +"\t\t\t\t\t\t\t\t\t\t\t\t\tPlayer 2 (O) won!"+bcolors.ENDC)
                        pipi=1
                        sos=0
                    

                if k!=" "  and p!=" "  and üü!=" "  and l!=" "  and ü!=" "  and ää!=" "  and j!=" "  and ä!=" "  and öö !=" " and sos==1:
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t         1   2   3  ")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t     1 |",k,"|",p,"|",üü,"|")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t     2 |",l,"|",ü,"|",ää,"|")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t     3 |",j,"|",ä,"|",öö,"|")
                    print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                    print(bcolors.WARNING +"\t\t\t\t\t\t\t\t\t\t\t\t\tGame is over! Nobody won!"+bcolors.ENDC)
                    pipi=1
                
            
                if pipi==1:
                    opa=input(bcolors.WARNING +"\t\t\t\t\t\t\t\t\t\t\t\t\tType 'r' to restart or 'e' to end: "+bcolors.ENDC)
                    popo=1
                    if opa=="r":
                        fofo=1
                        usa=0
                        #print("    1   2   3  \n  +---+---+---+\n1 |   |   |   |\n  +---+---+---+\n2 |   |   |   |\n  +---+---+---+\n3 |   |   |   |\n  +---+---+---+")
                        k=p=üü=l=ü=ää=j=ä=öö=" "
                        pipi=0
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\t         1   2   3  ")
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\t     1 |",k,"|",p,"|",üü,"|")
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\t     2 |",l,"|",ü,"|",ää,"|")
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\t     3 |",j,"|",ä,"|",öö,"|")
                        print("\t\t\t\t\t\t\t\t\t\t\t\t\t       +---+---+---+")
                        sos=1
                    else:
                        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        print("\t\t\t\t\t\t\t\t\t\t ████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗░██████╗  ███████╗░█████╗░██████╗░")
                        print("\t\t\t\t\t\t\t\t\t\t ╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝██╔════╝  ██╔════╝██╔══██╗██╔══██╗")
                        print("\t\t\t\t\t\t\t\t\t\t ░░░██║░░░███████║███████║██╔██╗██║█████═╝░╚█████╗░  █████╗░░██║░░██║██████╔╝")
                        print("\t\t\t\t\t\t\t\t\t\t ░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░░╚═══██╗  ██╔══╝░░██║░░██║██╔══██╗")
                        print("\t\t\t\t\t\t\t\t\t\t ░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗██████╔╝  ██║░░░░░╚█████╔╝██║░░██║")
                        print("\t\t\t\t\t\t\t\t\t\t ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝\n")
                        print("\t\t\t\t\t\t\t\t\t\t\t    ██████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗███╗░░██╗░██████╗░")
                        print("\t\t\t\t\t\t\t\t\t\t\t    ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██║████╗░██║██╔════╝░")
                        print("\t\t\t\t\t\t\t\t\t\t\t    ██████╔╝██║░░░░░███████║░╚████╔╝░██║██╔██╗██║██║░░██╗░")
                        print("\t\t\t\t\t\t\t\t\t\t\t    ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██║██║╚████║██║░░╚██╗")
                        print("\t\t\t\t\t\t\t\t\t\t\t    ██║░░░░░███████╗██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝")
                        print("\t\t\t\t\t\t\t\t\t\t\t    ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        fofo=0
                        ö=0
                        pipi=0

                if x==2 and y==2 or y==1 or y==3 and k==l==j==" ":
                    ln1=="" 
                    ln2==""
                    ln3=="" 
