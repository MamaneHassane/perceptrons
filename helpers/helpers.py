import numpy as np

# Transposée d'un vecteur
def transposee(vecteur_np):
    return vecteur_np.T

# Calculer x' : ajouter x au début d'un vecteur
def x_prime(vecteur_np):
    return transposee(np.insert(vecteur_np, 0, 1))

# Savoir si x'.T(w) d'un vecteur est positif ou négatif
def signe_de_x_prime_transposee_omega(vecteur_np, omega):
    return np.dot(x_prime(vecteur_np), transposee(omega)) > 0

# Générer un vecteur de n éléments nuls
def vecteur_nul(dimension):
    return np.zeros(dimension)

# Générer un vecteur de n éléments aléatoires entre -1 et 1
def random_vecteur(dimension) :
    return np.random.uniform(-1, 1, dimension)

# Générer un vecteur omega dont le premier élément est 1, en prenant en compte la dimension de l'ensemble
def random_omega(dimension):
    return np.insert(np.random.uniform(-1, 1, dimension),0,1)

# Calculer la norme d'un vecteur
def norme(vecteur_np):
    return np.linalg.norm(vecteur_np)

# Calculer le récouvrement R entre deux vecteurs
def recouvrement_r(vecteur1, vecteur2):
    produit_scalaire = np.dot(vecteur1, vecteur2)
    norme_produit = norme(vecteur1) * norme(vecteur2)
    return produit_scalaire / norme_produit
