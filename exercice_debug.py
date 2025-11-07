# exercice_debug.py

# 🧩 Cas 1 : Erreur de syntaxe
# Essaie d'exécuter ce code : il manque une parenthèse
print("Bonjour débutant Python!"

# 🧩 Cas 2 : Erreur de variable
# La variable "nom" n'existe pas encore ici
print("Salut " + nom)

# 🧩 Cas 3 : Erreur de type
# On essaie d'additionner une chaîne et un nombre
age = "25"
print("Ton âge dans 5 ans sera : " + (age + 5))

# 🧩 Cas 4 : Erreur de logique (le résultat n'est pas faux techniquement, mais illogique)
# On veut afficher les nombres pairs de 0 à 10, mais le code est mal écrit
for i in range(10):
    if i % 2 == 1:
        print(i, "est pair")

# 🧩 Cas 5 : Erreur dans une fonction
# La fonction doit renvoyer la somme de deux nombres
def addition(a, b):
    somme = a - b  # ❌ erreur volontaire
    return somme

print("2 + 3 =", addition(2, 3))

# 🧩 Cas 6 : Erreur avec liste
# On veut accéder à un élément qui n'existe pas
ma_liste = [1, 2, 3]
print(ma_liste[5])  # l'index 5 n'existe pas

# 🧩 Cas 7 : Erreur logique avancée
# On veut calculer la moyenne d'une liste, mais division incorrecte
notes = [10, 15, 20]
moyenne = sum(notes) / len(notes) - 1  # ❌ erreur de calcul
print("Moyenne:", moyenne)

# 🧩 Cas 8 : Erreur de condition
# On veut vérifier si l'âge est supérieur ou égal à 18
age = 17
if age > 18:
    print("Majeur")
else:
    print("Mineur mais condition mal écrite")  # vérifier la logique
