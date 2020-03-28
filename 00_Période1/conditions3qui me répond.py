##nom = input("quel est ton nom? ")
##print("Bonjour " , nom)
##clash = input("a tu clash? ")
##print("Bonjour " , clash)
####niveau_vie = int(input("Quel est ton niveau 
##niveau_vie = int(input("Quel est ton niveau de vie de 0 à 100? "))
##
##if niveau_vie > 20:
##    print("ça va tu es tranquille.")
##else:
##    print("ça craint!")

niveau_vie = int(input("Quel est ton niveau de vie de 0 à 100? "))
if niveau_vie < 0 or niveau_vie > 100 :
    print("J'ai dit entre 0 et 100.")
elif niveau_vie > 20:
    print("ça va tu es tranquille.")
else:
    print("ça craint!")

