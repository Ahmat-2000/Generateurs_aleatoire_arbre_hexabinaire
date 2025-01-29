import scipy , scipy.optimize
import random , math

###### Rayon de convergence pour les arbres binaires #########

def rayon_Catalan():
    
    def f(X):
        x = X[0]
        y = X[1]
        return [  - y + 1 + x*y*y      ,  -1 + 2*x*y ]
    
    A = scipy.optimize.fsolve(f,[0,1])
    return A[0]

###### Rayon de convergence pour les arbres unaires-binaires #########

def rayon_unaires_binaires():

    def f2(X):
        x = X[0]
        y = X[1]
        return [  - y + 1 + x*y + x*y*y      ,  -1 +  x + 2*x*y ]

    A = scipy.optimize.fsolve(f2,[0,1])
    return A[0]

##### Arbres binaires ######

class Arbre:
    
    def __init__(self): #Initialise à une feuille
        self.feuille = True
        self.l = None
        self.r = None
        self.taille = 0

    def __repr__(self):  #pour faire des print
        if self.feuille:
            return "feuille"
        return "n("+ repr(self.l) + "," + repr(self.r) + ")"

def Cat(z):
    import math
    return (1-math.sqrt(1-4*z))/2/z

def Boltzmann_Binaire(z):
    if z > 1/4:
        print("Erreur : paramètre trop grand")
        return None
    
    c = Cat(z)

    def B():
        x = random.random()
        if x < 1/c:
            return Arbre()
        else:
            a = Arbre()
            a.feuille = False
            a.l = B()
            a.r = B()
            a.taille = a.l.taille + a.r.taille + 1
            return a

    return B()

def esperance_binaire_boltzmann(z):
    return (1 - math.sqrt(1 - 4*z) - 2*z)/(2*math.sqrt(1 - 4*z)*z*z) / ((1-math.sqrt(1-4*z))/2/z)
    
def binaire_au_moins_taille(x,n):
    k = 1
    a = Boltzmann_Binaire(x)
    while (a.taille < n):
        k += 1
        a = Boltzmann_Binaire(x)
    print(k,"tirages nécessaire pour obtenir au final un objet de taille",a.taille)
    return a

#### Un peu d'optimisation ####

def inductif_Boltzmann_Binaire(z): #version inductive de Boltzmann pour éviter le surpassement de la limite maximale de récursion

    if z > rayon_Catalan():
        print("Erreur : paramètre trop grand")
        return None
    
    c = Cat(z)
    a = Arbre()
    l = [a]
    gl = [a]
    
    while len(l) > 0:
        b = l.pop()
        x = random.random()

        if x > 1/c:
            b.feuille = False

            al = Arbre()
            b.l = al
            ar = Arbre()
            b.r = ar
            
            l.append(al)
            gl.append(al)
            l.append(ar)
            gl.append(ar)

    while len(gl) > 0:
        b = gl.pop()
        if not(b.feuille):
            b.taille = b.l.taille + b.r.taille + 1

    return a

def binaire_au_moins_taille2(x,n):
    k = 1
    a = Boltzmann_Binaire(x)
    while (a.taille < n):
        k += 1
        a = inductif_Boltzmann_Binaire(x)
    print(k,"tirages nécessaire pour obtenir au final un objet de taille",a.taille)
    return a

################################

##### Arbres unaires-binaires ######

class Unarbre:
    def __init__(self): #Initialise à une feuille
        self.l = None
        self.r = None
        self.taille = 1

    def __repr__(self):  #pour faire des print
        return "arbre unaire-binaire de taille " + str(self.taille)
 
def ser_gen_ub(x):
    def f(y):
        return  - y + 1 + x*y + x*y*y

    A = scipy.optimize.fsolve(f,0)
    return A[0]
    
def Boltzmann_Unaire_Binaire(z):
    if z > rayon_unaires_binaires():
        print("Erreur : paramètre trop grand")
        return None
    
    y = ser_gen_ub(z)
    
    def B():
        x = random.random()
        if x < 1/y:
            return Unarbre()
        elif x < 1/y + z :
            a = Unarbre()
            a.l = B()
            a.taille = a.l.taille + 1
            return a
        else:
            a = Unarbre()
            a.l = B()
            a.r = B()
            a.taille = a.l.taille + a.r.taille + 1
            return a

    return B()

def unaire_binaire_au_moins_taille(x,n):
    k = 1
    a = Boltzmann_Unaire_Binaire(x)
    while (a.taille < n):
        k += 1
        a = Boltzmann_Unaire_Binaire(x)
    print(k,"tirages nécessaire pour obtenir au final un objet de taille",a.taille)
    return a

##### Arbres ternaires ######
class Ternaires:
    def __init__(self): #Initialise à une feuille
        self.l = None
        self.m = None
        self.r = None
        self.taille = 0

    def __repr__(self):  #pour faire des print
        return "arbre ternaire de taille "+str(self.taille)

def rayon_ternaires():
    def f(X):
        x = X[0]
        y = X[1]
        return [  - y + x + y*y*y      ,  - 1 + 3*y*y ]
    A = scipy.optimize.fsolve(f,[0,0])
    return A[0]

def ser_gen_ter(x):
    def f(y):
        return   - y + x + y*y*y
    A = scipy.optimize.fsolve(f,0)
    return A[0]
    
def Boltzmann_Ternaire(z):
    if z > rayon_ternaires():
        print("Erreur : paramètre trop grand")
        return None
    
    y = ser_gen_ter(z)
    
    def B():
        x = random.random()
        if x < 1/y:
            return Ternaires()
        else:
            a = Ternaires()
            a.l = B()
            a.m = B()
            a.r = B()
            a.taille = a.l.taille + a.m.taille +  a.r.taille + 1
            return a

    return B()

def ternaire_au_moins_taille(x,n):
    k = 1
    a = Boltzmann_Ternaire(x)
    while (a.taille < n):
        k += 1
        a = Boltzmann_Ternaire(x)
    print(k,"tirages nécessaire pour obtenir au final un objet de taille",a.taille)
    return a

##### Arbres Plans ######

class Plan:
    def __init__(self): #Initialise à une feuille
        self.enfants = []
        self.taille = 0

    def __repr__(self):  #pour faire des print
        return "arbre plan de taille "+str(self.taille)+"ou le noeud racine a "+str(len(self.enfants))+" enfants"

def rayon_plans():

    def f(X):
        x = X[0]
        y = X[1]
        return [  - y + 1/(1-x*y)      ,  - 1 + x/(1-x*y)/(1-x*y) ]

    A = scipy.optimize.fsolve(f,[0,1])
    return A[0]

def ser_gen_plan(x):
    def f(y):
        return   - y + 1/(1-x*y) 
    A = scipy.optimize.fsolve(f,0)
    return A[0]
    
def Boltzmann_Plan(z):
    if z > rayon_plans():
        print("Erreur : paramètre trop grand")
        return None
    
    y = ser_gen_plan(z)
    
    def B():
        a = Plan()
        x = random.random()
        while x < y*z:
            a.enfants.append(B())
            a.taille += (a.enfants[len(a.enfants)-1]).taille + 1
            x = random.random()
        return a

    return B()

def plan_au_moins_taille(x,n):
    k = 1
    a = Boltzmann_Plan(x)
    while (a.taille < n):
        k += 1
        a = Boltzmann_Plan(x)
    print(k,"tirages nécessaire pour obtenir au final un objet de taille",a.taille)
    return a