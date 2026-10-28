
class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self._titulaire = titulaire
        self.__solde = solde_initial

    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            print("Dépôt effectué.")
        else:
            print("Montant invalide.")

    def retirer(self, montant):
        if montant <= 0:
            print("Montant invalide.")
        elif montant > self.__solde:
            print("Fonds insuffisants.")
        else:
            self.__solde -= montant
            print("Retrait effectué.")

    @property
    def solde(self):
        return self.__solde

    def __str__(self):
        return f"Titulaire : {self._titulaire}, Solde : {self.solde} €"


if __name__ == "__main__":
    compte = CompteBancaire("Ali", 1000)

    compte.deposer(200)
    compte.retirer(150)

    print(compte)
    print("Solde accessible (lecture) :", compte.solde)

    # Tentative de modification directe
    compte.solde = 500
