def verifierLigne(grille, row, num):
    '''
        (list, int, int) -> Bool
        Vérifier si la case à ajouter n'existe pas sur la ligne.
        Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    #verification si nombre est dans la ligne:
    for col in range(9):
        if grille[row][col] == num:
            return False #retourne false si trouver et True s'il n'est pas dans la ligne
    return True

def verifierCol(grille, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la colonne.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
    #verification si le nombre est dans la colonne
    for row in range(9):
        if grille[row][col] == num:
            return False #retourne false si trouver et True s'il n'est pas dans la colonne
    return True

def verifierSousGrille(grille, row, col, num):
    '''
            (list, int, int) -> Bool
            Vérifier si la case à ajouter n'existe pas sur la sous-grille.
            Preconditions: grille est une reference a une matrice 9x9 qui contient déja des nombres de 1 à 9
    '''
#coordonees des la sous grille:
    ligneDebut = row // 3 * 3
    colDebut = col // 3 * 3
    for row in range(ligneDebut, ligneDebut + 3):     #verification si le nombre est dans la grille
        for col in range(colDebut, colDebut + 3):
            if grille[row][col] == num:
                return False #retourne false si trouver et True sinon
    return True

def verifierGagner(grille):
    '''(list) ->  bool
    * Preconditions: grille est une reference a une matrice 9x9 qui contient de nombres de 1 à 9
    * Verifie si la grille est completement remplie.
    '''

    for row in range(9): #verification des cases - doivent etre toutes remplies
        for col in range(9):
            if grille[row][col] == 0:
                return False #Retourne false si 1+ case non remplie(s) et True sinon
    return True

def verifierValide(grille, row, col, num):
    '''
    (list, int, int, int) -> bool
    verifie si le nombre proposé est bon sur la ligne et colonne et la sous-grille donné en parametre.
    Preconditions: tab est une reference a une matrice 9 x 9 qui contient des chiffres entre 1 et 9
    '''

    #verification si nombre est dans la ligne:
    for i in range(9):
        if grille[row][i] == num:
            return False

    #verification si le nombre est dans la colonne
    for i in range(9):
        if grille[i][col] == num:
            return False

    #verification si le nombre est dans la grille
    ligneDebut = row // 3 * 3
    colDebut = col // 3 * 3
    for i in range(ligneDebut, ligneDebut + 3):
        for j in range(colDebut, colDebut + 3):
            if grille[i][j] == num:
                return False

    return True
