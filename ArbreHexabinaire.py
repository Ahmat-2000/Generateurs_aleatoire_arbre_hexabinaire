import math

class HexabinaryTree:
  """
  Classe représentant un arbre hexabinaire. 
  Un arbre hexabinaire est une structure où chaque nœud peut avoir 0, 2 ou 6 enfants. 
  Les nœuds internes sont représentés par 'O', tandis que les feuilles sont représentées par 'x'.
  """
  def __init__(self, is_leaf=True) -> None:
    """
    Initialise un nœud de l'arbre hexabinaire.

    :param is_leaf: Indique si le nœud est une feuille. Par défaut, il s'agit d'une feuille.
    """
    self.is_leaf = is_leaf  
    self.children = []      # Liste des enfants du nœud
    self.nb_children = 0    # Nombre d'enfants (0, 2 ou 6)
    self.size = 0         # Taille (nombre de nœuds internes)

  def __str__(self) -> str:
    """
    Représente l'arbre sous forme de chaîne de caractères, avec la taille et la structure ASCII de l'arbre.
    :return: Chaîne représentant l'arbre.
    """
    return f"\nTaille = {self.size}\n{self.print_tree(node=self, prefix='', is_last=self.is_leaf)}"

  def add_children(self, children) -> None:
    """
    Ajoute des enfants au nœud actuel.
    :param children: Liste d'objets HexabinaryTree représentant les enfants à ajouter.
    Si le nombre d'enfants n'est pas 0, 2 ou 6, un message d'erreur sera affiché.
    """
    n = len(children)
    if n != 2 and n != 6:
      raise ValueError("Un arbre hexabinaire doit avoir 0, 2 ou 6 enfants.")

    self.children = children
    self.is_leaf = False
    self.nb_children = n
    self.size = self.calculate_size()

  def calculate_size(self) -> int:
    """
    Calcule récursivement la taille de l'arbre hexabinaire, définie comme le nombre de nœuds internes.
    :return: Nombre total de nœuds internes dans l'arbre.
    """
    if self.is_leaf:
      return 0  
    self.size = 1  
    for child in self.children:
      self.size += child.calculate_size() 
    return self.size

  def print_tree(self, node: "HexabinaryTree", prefix: str, is_last: bool) -> str:
    """
    Affiche l'arbre hexabinaire sous forme graphique ASCII.

    :param node: Nœud actuel de l'arbre à afficher.
    :param prefix: Préfixe pour l'indentation des sous-arbres.
    :param is_last: Indique si le nœud actuel est le dernier enfant de son parent.
    :return: Représentation ASCII de l'arbre à partir du nœud donné.
    """
    # Détermine le symbole de branche
    connector = "└──" if is_last else "├──"
    value = f"{prefix}{connector}{'x' if node.is_leaf else 'O'}\n"

    # Préparer le préfixe pour les enfants
    new_prefix = prefix + ("   " if is_last else "│  ")
    for i, child in enumerate(node.children):
      is_last_child = (i == len(node.children) - 1)
      value += self.print_tree(child, new_prefix, is_last_child)
    return value

  def tree_to_path(self) -> str:
    """
    Transforme un arbre hexabinaire en chemin combinatoire C
    :param node: Racine de l'arbre.
    :return: Liste de tuples représentant le chemin.
    """
    path = []

    def dfs(current):
      if current.is_leaf:
        # Une feuille correspond à un pas (-1, +1)
        path.append("(-1, +1)")
      else:
        # Nœud interne avec 2 ou 6 enfants
        if len(current.children) == 2:
          path.append("(+1, +1)")
        elif len(current.children) == 6:
          path.append("(+5, +1)")
        else:
          raise ValueError("Un nœud interne doit avoir 2 ou 6 enfants.")
        # Parcourir les enfants en profondeur
        for child in current.children:
          dfs(child)

    # Lancer la transformation en profondeur
    dfs(self)
    path = ["(0, 0)"] + path
    return " → ".join(path)
    
def compute_coefficient(n: int ) -> int:
  """
  Calcule le coefficient de la série génératrice pour les arbres hexabinaires
  de taille n. La formule utilisée est basée sur les combinaisons binomiales.
  Paramètre : n (int) : Taille des arbres hexabinaires (doit être >= 0).
  Retourne : int : Le coefficient correspondant à la taille n dans la série génératrice.
  """
  if n == 0:
    return 1
  s = 0
  for k in range(n+1):
    s += math.comb(n, k) * math.comb(2*n + 4*k, n + 4*k + 1)
  return s // n

def coefficients_hexa_tree(n : int) -> list[int]:
  """
  Génère une liste des coefficients des arbres hexabinaires de taille 0 à n.
  Paramètre : n (int) : La taille maximale des arbres hexabinaires.
  Retourne : list : Une liste des coefficients correspondant aux tailles 0, 1, ..., n.
  """
  return [compute_coefficient(i) for i in range(n+1)]

if __name__ == "__main__":
  root = HexabinaryTree()  # Racine
  node1 = HexabinaryTree()  # Premier nœud enfant de la racine
  node2 = HexabinaryTree()  # Deuxième nœud enfant de la racine
  node3 = HexabinaryTree()  # Nœud enfant de node1
  node3.add_children([HexabinaryTree() for _ in range(6)])
  node2.add_children([HexabinaryTree() for _ in range(6)])
  node1.add_children([HexabinaryTree(), node3])
  root.add_children([node1, node2])

  print(root)
  print("\n##################################\n")
  print(coefficients_hexa_tree(10))
