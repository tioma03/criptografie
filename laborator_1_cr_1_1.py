 #           Lucrare de laborator - sarcina 1.1 (ELSE)


#definim functia 
def caesar():
    alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # Alegerea operației
    operatie = input("Alege operatia (criptare=c / decriptare=d): ").lower()
    if operatie not in ["criptare", "decriptare", "c", "d"]:
        print("Te rog scrie doar: criptare sau decriptare (sau c/d).")
        return

    if operatie == "c":
        operatie = "criptare"
    elif operatie == "d":
        operatie = "decriptare"

    # Introducerea cheii
    try:
        k = int(input("Introdu cheia (1-25): "))
    except:
        print("Cheia trebuie să fie un număr întreg.")
        return

    if k < 1 or k > 25:
        print("Cheia trebuie să fie între 1 și 25.")
        return

    # Introducerea mesajului
    mesaj = input("Introdu mesajul (doar litere): ")

    mesaj = mesaj.replace(" ", "").upper()

    if not mesaj.isalpha():
        print("Mesajul trebuie să conțină doar litere(A-Z).")
        return

    rezultat = ""

    for litera in mesaj:
        pozitie = alfabet.index(litera)

        if operatie == "criptare":
            noua_pozitie = (pozitie + k) % 26
        else:
            noua_pozitie = (pozitie - k) % 26

        rezultat += alfabet[noua_pozitie]

    if operatie == "criptare":
        print("Mesaj criptat este:", rezultat)
    else:
        print("Mesaj decriptat este:", rezultat)
        
      


# pornim programul
caesar()
