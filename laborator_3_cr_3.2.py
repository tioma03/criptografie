# Alfabetul limbii române (31 litere mari)
alfabet = ["A","Ă","Â","B","C","D","E","F","G","H","I","Î","J","K","L","M",
           "N","O","P","Q","R","S","Ș","T","Ț","U","V","W","X","Y","Z"]



# Alegerea operatiei (repetăm până e validă)
while True:
    operatie = input("Alege operatia (c = criptare, d = decriptare): ").lower()
    if operatie in ["c", "d"]:
        break
    else:
        print("Scrie doar 'c' sau 'd'!")

# Citim cheia (trebuie minim 7 litere si toate in alfabet)
while True:
    cheie = input("Introdu cheia (minim 7 litere): ").replace(" ", "").upper()
    if len(cheie) < 7:
        print("Eroare: cheia trebuie sa aiba minim 7 litere!")
        continue
    if all(lit in alfabet for lit in cheie):
        break
    else:
        print("Eroare: cheia trebuie sa contina doar litere din alfabetul limbii romane[A-Z]!")

# Criptare
if operatie == "c":
    while True:
        mesaj = input("Introdu mesajul: ").replace(" ", "").upper()
        if all(lit in alfabet for lit in mesaj):
            criptat = ""
            for i in range(len(mesaj)):
                poz_m = alfabet.index(mesaj[i])
                poz_k = alfabet.index(cheie[i % len(cheie)])
                poz_c = (poz_m + poz_k) % len(alfabet)   # formula criptare
                criptat += alfabet[poz_c]
            print("Mesaj criptat:", criptat)
            break
        else:
            print("Eroare: mesajul contine caractere invalide! Foloseste doarlitere din alfabetul limbii romane[A-Z]")

# Decriptare
elif operatie == "d":
    while True:
        criptograma = input("Introdu criptograma: ").replace(" ", "").upper()
        if all(lit in alfabet for lit in criptograma):
            text = ""
            for i in range(len(criptograma)):
                poz_c = alfabet.index(criptograma[i])
                poz_k = alfabet.index(cheie[i % len(cheie)])
                poz_m = (poz_c - poz_k + len(alfabet)) % len(alfabet)  # formula decriptare
                text += alfabet[poz_m]
            print("Mesaj decriptat:", text)
            break
        else:
            print("Eroare: criptograma contine caractere invalide! Foloseste doar litere din alfabetul limbii romane[A-Z]")
