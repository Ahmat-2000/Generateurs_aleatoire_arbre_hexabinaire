# 🌳 Génération Uniforme d'Arbres Hexabinaires

## 📌 Présentation

Ce projet implémente **un générateur uniforme d'arbres hexabinaires**, une classe d'arbres où **chaque nœud interne a soit 0, 2 ou 6 enfants**.  

L'algorithme est basé sur **la série génératrice** des arbres hexabinaires :  

$`H(z) = 1 + z*H(z)^2 + z*H(z)^6 `$

Nous utilisons également **une correspondance avec des chemins combinatoires**.

---

## 📖 Ressources

Les méthodes implémentées sont inspirées des travaux suivants :  

- 📄 **Slides GT Aléa - Carine Pivoteau (2023)**  
  🔗 [GT Aléa 2023 - Génération uniforme](https://gt-alea.math.cnrs.fr/Archives/Pivoteau_alea2023_Slides.pdf)  

- 📄 **Méthodes Génératives & Combinatoire**  
  🔗 [Méthodes Génératives](http://jl.baril.u-bourgogne.fr/cmi4c.pdf)  

- 💻 **Notebook d'exploration sur GitHub**  
  🔗 [Alea2023Notebooks - Génération uniforme](https://github.com/CarinePivoteau/Alea2023Notebooks/blob/main/gR_binary_trees.ipynb)  

---

## 🏗️ Fonctionnalités

- ✅ **Génération uniforme d'arbres hexabinaires** en respectant leur distribution combinatoire.
- ✅ **Transformation d'un arbre en chemin combinatoire**.
- ✅ **Reconstruction d'un arbre hexabinaire à partir d'un chemin**.
- ✅ **Affichage ASCII des arbres générés**.
- ✅ **Utilisation d'une approche récursive pour le parcours et la construction**.

---
