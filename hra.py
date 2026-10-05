import random 

moznosti = ["kámen", "nůžky", "papír"]

vyhry = 0
prohry = 0
remizy = 0

while True:
    print("Vyber si z klasicke trojice")
    print("1. Kámen")
    print("2. Nůžky")
    print("3. Papír")
    print("4. Konec hry")
    try:
        volba = int(input("Co jste zvolili :): "))
    except ValueError:
        print("Vypln z moznosti.\n")
        continue

    if volba < 1 or volba > 4:
        print("Dej sem nejakou validni moznost (1-4)!\n")
        continue

    if volba == 4:
        print("\nKonec hry!")
        print("Celkove skore:")
        print("Vyhry:", vyhry, "| Prohry:", prohry, "| Remizy:", remizy)
        break

    user_choice = moznosti[volba - 1]

    print("\nVase volba:", user_choice)
    print("Ted python...")

    comp_choice = random.randint(1, 3)
    computer_choice = moznosti[comp_choice - 1]

    print("Volba pc je:", computer_choice)
    print(user_choice, "vs", computer_choice)

    if volba == comp_choice:
        print("Remiza")
        remizy += 1

    elif (
        (volba == 1 and comp_choice == 2) or
        (volba == 2 and comp_choice == 3) or
        (volba == 3 and comp_choice == 1)
    ):
        print("Vyhral jsi")
        vyhry += 1

    else:
        print("Program vyhral")
        prohry += 1

    print("Skore -> Ty:", vyhry, "PC:", prohry, "Remizy:", remizy, "\n")

wait = input("\nStiskni enter pro pokracovani...")