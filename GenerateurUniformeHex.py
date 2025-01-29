from ArbreHexabinaire import HexabinaryTree
from ArbreHexabinaire import coefficients_hexa_tree as compute_H
import random

class UniformHexabinaryGenerator:
    """
    Générateur uniforme d'arbres hexabinaires de taille n.
    self.n = n if n > 0 else 0
    """
    
    def __init__(self, n: int = 1) -> None:
        """
        Initialise le générateur et précalcule les coefficients pour accélérer la génération.
        """
        self.n = n if n > 0 else 0
        self.precalculate_H()

    def compute_H2(self) -> list[int]:
        """
        Calcule les coefficients de H^2 : 
        H2_n = sum(H_i * H_(n-i) pour i de 0 à n)
        """
        return [sum(self.H[i] * self.H[k-i] for i in range(k+1)) for k in range(self.n+1)]

    def compute_H6(self) -> list[int]:
        """
        Calcule les coefficients de H^6 :
        H6_n = sum(H_i1 * H_i2 * H_i3 * H_i4 * H_i5 * H_i6 pour toutes les partitions de k)
        """
        H6 = []
        for k in range(self.n+1):
            s = 0
            for i1 in range(k+1):
                for i2 in range(k+1 - i1):
                    for i3 in range(k+1 - i1 - i2):
                        for i4 in range(k+1 - i1 - i2 - i3):
                            for i5 in range(k+1 - i1 - i2 - i3 - i4):
                                i6 = k - i1 - i2 - i3 - i4 - i5
                                s += self.H[i1] * self.H[i2] * self.H[i3] * self.H[i4] * self.H[i5] * self.H[i6]
            H6.append(s)
        return H6

    def precalculate_H(self) -> None:
        """
        Précalcule les coefficients H_n, H²_n et H⁶_n pour éviter les recalculs inutiles.
        """
        self.H = compute_H(self.n)
        self.H2 = self.compute_H2()
        self.H6 = self.compute_H6()

    def generate(self) -> "HexabinaryTree":
        """
        Génère un arbre hexabinaire uniforme de taille n.
        """
        def genH(n: int) -> "HexabinaryTree":
            if n == 0:
                return HexabinaryTree()  
            total = self.H2[n] + self.H6[n]
            if total == 0:  # Éviter division par zéro
                return HexabinaryTree()

            p_two_children = self.H2[n] / total
            rand_choice = random.random()

            node = HexabinaryTree(is_leaf=False)
            if rand_choice < p_two_children:
                # Cas 2 enfants
                split = random.randint(0, n-1)  # Répartition entre les deux
                node.add_children([genH(split), genH(n-1-split)])
            else:
                # Cas 6 enfants
                splits = [0] * 6
                remaining = n-1
                for i in range(5):
                    splits[i] = random.randint(0, remaining)
                    remaining -= splits[i]
                splits[5] = remaining  # Le dernier prend ce qui reste
                node.add_children([genH(size) for size in splits])

            return node
        
        return genH(self.n)

# -----------------------
# Exécution du Générateur
# -----------------------

if __name__ == "__main__":
    n = 2 # Taille de l'arbre à générer
    generator = UniformHexabinaryGenerator(n)
    arbre = generator.generate()
    print(f"Arbre hexabinaire généré : {arbre}")
    print(f"Chemin généré : {arbre.tree_to_path()}")
