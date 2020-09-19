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

annee=int(input("Entrez une année "))



if(annee%4==0 or annee%100==0 and annee%400==0):
    print("l'année est bissextille ")
else:
    print("non pa bissextille")


