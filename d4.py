#QUESTIONS 1 À 3

#q1

#Fonction traduction de francais a anglais et anglais a francais
def transl(d, s):
    if s in d:     #verifie si s est en anglais
        return d[s]
    elif s in list(d.values()):     #verifie si s est en francais
        for key, value in d.items(): #cherceh la bonne cle
            if value == s:
                return key
    else: #or si s ni en francais ou anglais : on retourne une erreur
        return "UNKNOWN"

# Dictionnaire global
d = {"apple": "pomme", "banana": "banane", "pear": "poire", "plum": "prune"}
print(transl(d, "apple"))


#q2
def setOp(list1, list2): #prends 2 listes en entree et retourne le set de leur union
    return list(set(list1+list2))

#appel de la fonction
print(setOp([1],[2,3,2,2]))


#q3
def matrixMinMax(m):
    n = len(m) #qte de rangees
    #minimum
    min = m[0][0] #initialization de la valeur minimale de la matrice
    for row in m: #boucle pour chaque rangee
        for i in row: #boucle pour chaque element des ranges
            if (i < min): #compare la valeur minimale i actuelle avec la prochaine et remplace si la prochaine est inferieur
                min = i

    #maximum
    max = m[0][0] #initialization de la valeur maximale de la matrice
    for row in m: #boucle pour chaque rangee
        for i in row: #boucle pour chaque element des ranges
            if (i> max): #compare la valeur max i actuelle avec la prochaine et remplace si la prochaine est superieur
                max = i

    print((min,max))

#appel de la fonction
matrixMinMax([[1, 5], [2, 8]])
