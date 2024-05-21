class Noeud:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfants = []
    def __repr__(self):
        return f"Position : {self.valeur[0]}, Speed : {self.valeur[1]}"
    
def creer_arbre_racine_profondeur(racine, profondeur_max, liste_distances):
    if profondeur_max == 0:
        return
    position, speed = racine.valeur
    distances = liste_distances(position, speed)

    for _, distance in enumerate(distances):
        valeur_enfant = distance
        enfant = Noeud(valeur_enfant)
        racine.enfants.append(enfant)
        creer_arbre_racine_profondeur(enfant, profondeur_max - 1, liste_distances)

# Exemple d'utilisation
racine = Noeud((0, 0))
profondeur_max = 3

# Supposons que votre fonction liste_distances a la signature suivante :
# def liste_distances(noeud):  # Cette fonction doit renvoyer une liste de 9 distances

# Vous pouvez utiliser une fonction lambda pour adapter la signature
liste_distances_function = lambda x, y: [(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9)]

creer_arbre_racine_profondeur(racine, profondeur_max, liste_distances_function)
print(racine.enfants[0].enfants)

def depth_first_search(node):
    # Traiter le nœud courant
    max_node = max([racine, node], key=lambda x: x.valeur[2])
    # ICI IL FAUT GARDER LE MEILLEUR NOEUD (QUI A LA DISTANCE LA PLUS GRANDE)
    print(node) # ici on affiche le noeud courant

    # Parcourir les enfants du nœud courant
    for child in node.enfants:
        depth_first_search(child)
    
depth_first_search(racine)
# Vous pouvez maintenant accéder à l'arbre à partir de la racine et explorer les nœuds et les enfants.
