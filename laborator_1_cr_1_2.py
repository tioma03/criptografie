#           Lucrare de laborator - sarcina 1.2 (ELSE cu 2 chei)

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

    # Introducerea cheii 1 (numerică)
    try:
        k1 = int(input("Introdu cheia 1 (1-25): "))
    except:
        print("Cheia 1 trebuie să fie un număr întreg.")
        return

    if k1 < 1 or k1 > 25:
        print("Cheia 1 trebuie să fie între 1 și 25.")
        return

    # Introducerea cheii 2 (text, doar litere, minim 7)
    k2 = input("Introdu cheia 2 (doar litere, minim 7): ").upper()
    if not k2.isalpha() or len(k2) < 7:
        print("Cheia 2 trebuie să conțină doar litere și să aibă cel puțin 7 caractere.")
        return

    # Transformăm cheia 2 în lista de deplasari (A=0, B=1, ..., Z=25)
    k2_shifts = [alfabet.index(litera) for litera in k2]

    # Introducerea mesajului
    mesaj = input("Introdu mesajul (doar litere): ")
    mesaj = mesaj.replace(" ", "").upper()

    if not mesaj.isalpha():
        print("Mesajul trebuie să conțină doar litere(A-Z).")
        return

    rezultat = ""

    for i, litera in enumerate(mesaj):
        pozitie = alfabet.index(litera)

        # Pasul 1: aplicăm cheia 1
        if operatie == "criptare":
            noua_pozitie = (pozitie + k1) % 26
        else:
            noua_pozitie = (pozitie - k1) % 26

        # Pasul 2: aplicăm cheia 2 (ciclic, pe baza poziției literei)
        shift2 = k2_shifts[i % len(k2_shifts)]
        if operatie == "criptare":
            noua_pozitie = (noua_pozitie + shift2) % 26
        else:
            noua_pozitie = (noua_pozitie - shift2) % 26

        rezultat += alfabet[noua_pozitie]

    # Afișăm rezultatul final
    if operatie == "criptare":
        print("Mesaj criptat este:", rezultat)
    else:
        print("Mesaj decriptat este:", rezultat)


# pornim programul
caesar()