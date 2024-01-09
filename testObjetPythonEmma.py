from typing import Any


class Personnage():

    def __init__(self, nom, prenom, vie, attaque, action):
        self.nom = nom
        self.prenom = prenom
        self.vie = vie
        self.attaque = attaque
        self.action = action

    def __repr__(self):
        return f"{self.nom} {self.prenom} {self.vie} {self.attaque} {self.action}"  
    
    def attaquer(self, cible):
        if self.vie <= 0:
            print(f"{self.nom} est mort")
            return
        if self.action == 0:
            print(f"{self.nom} n'a plus d'action")
            return
        cible.vie -= self.attaque
        self.action -= 1
        print(f"{self.nom} attaque {cible.nom} a {cible.vie} points de vie")

    def soigner(self):
        if self.vie <= 0:
            print(f"{self.nom} est mort")
            return
        if self.action == 0:
            print(f"{self.nom} n'a plus d'action")
            return
        self.vie += self.attaque
        self.action -= 1
        print(f"{self.nom} se soigne {self.vie} points de vie")

if __name__ == "__main__":
    with open("personnage.txt", 'r') as f:
        personnages = []
        for line in f:
            line = line.split()
            personnages.append(Personnage(line[0], line[1], int(line[2]), int(line[3]), int(line[4])))
            #print(personnages)

    with open("combat.txt", 'r') as f:
        for line in f:
            line = line.split()
            if line[1] == 'attaque':
                if line[0] == personnages[0].nom:
                    personnages[0].attaquer(personnages[1])
                else:
                    personnages[1].attaquer(personnages[0])
            if line[1] == 'soigne':
                if line[0] == personnages[0].nom:
                    personnages[0].soigner()
                else:
                    personnages[1].soigner()
            #[print(p) for p in personnages]
                    


























