import random

choix = ["p","f","c"]
humain_gagne = ["fp","pc","cf"]

choix_humain = input("Fais ton choix [p->pierre, f->feuille, c->ciseaux, q->quitter]: ")
choix_ordi = random.choice(choix)
resultat = choix_humain + choix_ordi

print("Humain a choisi " + choix_humain)
print("Ordinateur a choisi " + choix_ordi)


if choix_humain == choix_ordi:
    print("Match nul")
elif resultat in humain_gagne:
    print("Humain gagne.")
else:
    print("Perdu!")
