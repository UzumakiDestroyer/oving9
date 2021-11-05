class spørrespill:
    def  __init__(self, spørsmål="hvor mange øyne har en edderkopp?", alternativer=[8, 2, 4, 1], svar=1) -> None:
        self.svarAlternativer = alternativer
        self.svar = svar
        self.spørsmål = spørsmål 

    def __str__(self) -> str:
        ferdigSpørsmål = self.spørsmål + "\n"
        for num, svar in enumerate(self.svarAlternativer, start=1):
            ferdigSpørsmål += f"\n{num}. {svar}"
        return ferdigSpørsmål      

    def sjekkSvar(self, svar) -> bool:
        if svar == self.svar:
            return True
        return False

    def korekkt_svar_text(self):
        return self.svarAlternativer[self.svar-1]




def klasseManager(filnavn="sporsmaalsfil.txt"):
    with open (filnavn, "r", encoding="utf-8") as r:
        linjeleser = r.readlines()
        listami = []
        for linje in linjeleser:
            spørsmål = linje.split(":")
            alternativer = spørsmål[2].strip().strip("[]").split(", ")
            svar = int(spørsmål[1].strip())
            spørsmaul = spørsmål[0].strip()
            listami.append(spørrespill(spørsmaul, alternativer, svar))
        return listami


       
if __name__ == "__main__":
    klasseListe = klasseManager()
    player1 = 0
    player2 = 0
    
    for objekt in klasseListe:
        print(objekt.__str__())
        svar1 = int(input("Svar spiller 1!"))
        svar2 = int(input("Svar spiller 2!"))
        print("korrekt svar:" + objekt.korekkt_svar_text())
        if objekt.sjekkSvar(svar1):
            print("\nspiller1: riktig")
            player1 += 1
        else:
            print("\nspiller1: feil")
        
        if  objekt.sjekkSvar(svar2):
            print("spiller2: riktig")
            player2 += 1
        else:
            print("spiller2 feil")
    print(f"spiller1: {player1}" )
    print(f"spiller2: {player2}" )