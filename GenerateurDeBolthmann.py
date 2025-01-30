import scipy, scipy.optimize
import random, math
from ArbreHexabinaire import HexabinaryTree

class BoltzmannGenerator:
    def __init__(self):
        self.radius = self.radius_of_convergence()

    def radius_of_convergence(self) -> float:
        """
        Calcule le rayon de convergence pour les arbres hexabinaires.
        """
        def f2(X):
            x, y = X  # x = z (rayon), y = H(z) (valeur critique)
            return [
                -y + 1 + x * y**2 + x * y**6,  # Série génératrice
                2 * x * y + 6 * x * y**5 - 1  # Condition critique
            ]
        A = scipy.optimize.fsolve(f2, [0, 1])  # Point de départ pour la résolution
        return A[0]  # Retourne le rayon de convergence

    def generating_series(self, x: float) -> float:
        """
        Calcule la valeur de la série génératrice H(x) pour un paramètre donné x.
        """
        def f(y):
            return -y + 1 + x * y**2 + x * y**6
        solution = scipy.optimize.fsolve(f, 0)  # Résout pour H(x)
        return solution[0]

    def generate(self, z: float) -> "HexabinaryTree":
        """
        Génère un arbre hexabinaire aléatoire selon la distribution Boltzmann pour le paramètre z.
        """
        if z > self.radius:
            raise ValueError("Erreur : le paramètre z dépasse le rayon de convergence.")

        y = self.generating_series(z)
        # self.H2 = y**2
        # self.H6 = y**6

        def B():
            x = random.random()  
            if x < 1/y:  
                return HexabinaryTree()
                
            node = HexabinaryTree(is_leaf=False)
            # if x < 1 / y + self.H2 / (self.H2 + self.H6):  
            if x < 1/y + z: # donne une bonne distribution entre les noeuds avec 2 ou 6 enfants
                node.add_children([B(), B()])
            else:
                node.add_children([B() for _ in range(6)])
            return node

        return B()
    
    def tree_of_size_n(self, z: float, n: int):
        """
        Génère un arbre hexabinaire de taille exactement `n`.
        """
        k = 0
        while True:
            k += 1
            a = self.generate(z)
            if a.size == n:
                print(f"{k} tirages nécessaires pour obtenir un arbre de taille {n}")
                return a


if __name__ == "__main__":
    generator = BoltzmannGenerator()
    print(generator.radius)
    z = 0.01  # Choisir une valeur pour z
    n = 5
    arbre = generator.tree_of_size_n(z,n)
    print(f"Arbre hexabinaire généré : {arbre}")
