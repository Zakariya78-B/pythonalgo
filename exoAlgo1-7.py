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

benefice=int(input("entrez le montant des benefice "))

if(benefice<10001):
    impot1 = (benefice*20)/100
    print("le montant de l'impot est de ",impot1)
elif(benefice>10000 and benefice<15001):
    tranche=benefice-10000
    impot2=10000*20/100
    impot2 += (tranche*26)/100
    print("le montant de l'impot est de ",impot2)
elif(benefice>15001):
    tranche2=benefice-15000
    impot2=10000*20/100
    impot3=5000*26/100
    impot4=(tranche2*22)/100
    total=impot3+impot4+impot2
    print(impot2,"€ pour la tranche de 0€ à 10000€ ")
    print(impot3,"€ pour la tranche de 10001€ à 15000€ ")
    print(impot4,"€ pour la tranche au-delà à 15001€ ")
    print("le montant total de l'impot est de ",total)
else:
    print("entrez un valeur au dessus de 0 ")
