import graphviz
from ArbreHexabinaire import HexabinaryTree
from IPython.display import display

def draw_tree_unlabelled(tree : "HexabinaryTree", width:int=3, height:int=3):
    """
    Dessine un arbre hexabinaire sans étiquettes en utilisant Graphviz.
    
    :param tree: Instance de HexabinaryTree
    :param width: Largeur de la figure
    :param height: Hauteur de la figure
    """
    dot = graphviz.Graph(graph_attr={'size': f"{width},{height}"}, 
                         node_attr={'label': '', 'shape': 'circle', 
                                    'fillcolor': 'white', 'style': 'filled', 'fixedsize': 'true'})

    count = 0  # ID des nœuds

    def draw(node):
        """ Fonction récursive pour dessiner l'arbre """
        nonlocal count
        node_id = str(count)
        count += 1

        # Définir la couleur en fonction du type de nœud
        color = 'black' if not node.is_leaf else 'white'
        dot.node(node_id, fillcolor=color, fontcolor=color)

        # Dessiner les enfants
        child_ids = []
        for child in node.children:
            child_id = draw(child)
            dot.edge(node_id, child_id)
            child_ids.append(child_id)

        return node_id

    # Ajouter un nœud racine vide et dessiner l'arbre
    root_id = str(count)
    dot.node(root_id, fillcolor='black', fontcolor='black')  # Racine
    count += 1
    for child in tree.children:
        child_id = draw(child)
        dot.edge(root_id, child_id)

    # Afficher l'arbre
    display(dot)


def draw_tree_labelled(tree, width=5, height=5):
    """
    Dessine un arbre hexabinaire avec des étiquettes en utilisant Graphviz.

    :param tree: Instance de HexabinaryTree
    :param width: Largeur de la figure
    :param height: Hauteur de la figure
    """
    dot = graphviz.Graph(graph_attr={'size': f"{width},{height}"},
                         node_attr={'shape': 'circle', 'style': 'filled', 
                                    'fixedsize': 'true', 'fontname': 'Arial'})

    count = 0  # ID unique des nœuds

    def draw(node):
        """ Fonction récursive pour dessiner l'arbre """
        nonlocal count
        node_id = str(count)
        count += 1

        # Définir la couleur et l'étiquette du nœud
        if node.is_leaf:
            dot.node(node_id, label="x", fillcolor="white", fontcolor="black")
        else:
            dot.node(node_id, label="O", fillcolor="black", fontcolor="white")

        # Dessiner les enfants et ajouter les arêtes
        for child in node.children:
            child_id = draw(child)
            dot.edge(node_id, child_id)

        return node_id

    # Dessiner le nœud racine et appeler la récursion
    root_id = draw(tree)
    display(dot)