'''
age = int(input("Quel age avez vous?"))
if (age < 18 ) or (age > 130):
    print("Desole, vous etes hors des limites d'age")
print("--FIN--")
#Solution from the teacher:
age = input ("Quel est votre age?")
age = int(age)
if age < 18 or age > 130:
    print("Désolé, vous êtes hors des limites d'âge")
else:
    print("Bienvenue chez Interface3!")
print("--FIN--")
#Vous pouvez faire comme suivant (mais pas très joli)
if age < 18:
    print("Désolé, vous êtes trop jeune.")
else:
    if age > 130:
        print("Désolé, vous êtes au-delà de la limite d'age.")
        else:
            print("Bienvenue!")
'''
#Doc, Python a un autre facon pour faire ca: elif:
age = int(input("Quel age avez vous?"))
if age < 18:
    print("Désolé, vous êtes trop jeune.")
elif age > 130:
    print("Désolé, vous êtes au-delà de la limite d'age.")
else:
    print("Bienvenue!")

