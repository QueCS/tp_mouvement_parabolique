# %%
import numpy as np
import matplotlib.pyplot as plt

# importation des bibliothèques nécessaires pour le tracé de graphiques et la gestion des listes
# %%
# valeurs experimentales

##Paramètres de la fonction "readCol()" qui sera utilisée pour récupérer les données du fichier
nom_fichier = "valeurs mouvement parabolique.txt"
sep = "\t"  # la séparation est une tabulation
u = 1  # On saute la première ligne du fichier avant de commencer à récupérer les données (non nécessaire si la ligne commence par #)


############définition de la fonction readCol#####################
def readCol(n):
    col = np.loadtxt(nom_fichier, dtype=str, delimiter=sep, skiprows=u, usecols=[n])
    col = [float(elmt.replace(",", ".")) for elmt in col]  # On remplace les , par des .

    return col


############On applique la fonction au fichier afichier de données qui doit se trouver dans le même répertoire#####################
t = readCol(0)  # Première colonne
x = readCol(1)  # Seconde colonne
y = readCol(2)  # Troisième colonne

########### Affichage des valeurs###########
print(t)
print(x)
print(y)


vxl = []  # on crée une liste vide
m = np.arange(len(t) - 2)  # on crée une liste d'entiers qui va aller jusqu'à N-2
# pour pouvoir faire des différences finies jusqu'à N-2

for i in m:  # on lance la boucle
    vx = (x[i + 2] - x[i]) / (
        t[i + 2] - t[i]
    )  # on calcule la vitesse par la méthode des différences de i à i+2
    vxl.append(vx)  # on complète la liste des vxl

vyl = []  # idem pour vyl
m = np.arange(len(t) - 2)
for i in m:
    vy = (y[i + 2] - y[i]) / (t[i + 2] - t[i])
    vyl.append(vy)

# idem pour l'accélération, mais il faut là encore faire attention à la taille de la liste
axl = []
m = np.arange(len(t) - 4)
for i in m:
    ax = (vxl[i + 2] - vxl[i]) / (t[i + 2] - t[i])
    axl.append(ax)

ayl = []
m = np.arange(len(t) - 4)
for i in m:
    ay = (vyl[i + 2] - vyl[i]) / (t[i + 2] - t[i])
    ayl.append(ay)
m = np.arange(1, len(t) - 4)
# %%

# courbe
plt.figure()
for i in m:
    plt.arrow(x[i + 2], y[i + 2], 0.02 * axl[i], 0.02 * ayl[i], head_width=0.03)
    # on fait tracer des vecteurs variation de vitesse de positions initiales x[i+2],y[i+2], de coordonnées 0.02*axl[i]
    # et idem pour uy, avec une largeur de tête donnée
    plt.arrow(x[i + 2], y[i + 2], 0, -0.02 * 9.8, fc="r", ec="r", head_width=0.03)
# on fait tracer les vecteurs accélération théoriques (verticaux, de norme 9.8, avec une correction d'échelle 0.02)
plt.xlim(0, 2)
plt.ylim(0, 1.2)
plt.grid()
plt.plot(x, y, "bo-")
plt.xlabel("xreelle")
plt.ylabel("yreelle")
plt.title("Comparaison entre variation de vitesse et intensité de la pesanteur")
plt.show()

# %%
m = np.arange(0, len(t) - 4)
ath = 0 * m - 9.8
mod = np.polyfit(m, ayl, 0)  # on modélise l'évolution précédente par une constante
moda = (
    0 * m + mod[0]
)  # on définit une liste de valeurs de cette constante, pour pouvoir la tracer.

# %%
# Courbe
plt.figure()  # Tracé avec options classiques.
plt.plot(m, ayl, "bo-", label="aréelle")
plt.legend()
plt.grid()
plt.ylim(-20, 0)
plt.plot(m, ath, "r-", label="g")
plt.legend()
plt.plot(m, moda, "g-", label="moyenne")
plt.legend()
plt.xlabel("points de la trajectoire")
plt.ylabel("accélération verticale réelle")
plt.title("Comparaison entre variation de vitesse et intensité de la pesanteur")
plt.show()
print(round(mod[0], 1))
