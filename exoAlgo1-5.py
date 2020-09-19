#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      moi
#
# Created:     19/09/2020
# Copyright:   (c) moi 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
montant=int(input("montant à epargner"))
annee=int(input("nombre d'annee"))
taux=float(input("taux annuel"))
parAn=montant*taux/100
total=parAn*annee



print("votre credit va vous raporter par an",(parAn))
print("le montant total est ",montant+total,"le benef est de ", total,"€")
