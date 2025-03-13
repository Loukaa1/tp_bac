def taille(arbre, lettre):
    if lettre == '':
        return 0
    lgauche, ldroit = arbre[lettre]
    return 1 + taille(arbre, lgauche) + taille(arbre, ldroit)


a = {
    'F': ['B', 'G'], 'B': ['A', 'D'], 'A': ['', ''], 'D': ['C', 'E'],
    'C': ['', ''], 'E': ['', ''], 'G': ['', 'I'], 'I': ['', 'H'], 'H': ['', '']
}

assert taille(a, 'B') == 5





def echange(tab, i, j):
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp

def tri_selection(tab):
    N = len(tab)
    for k in range(N - 1):
        imin = k 
        for i in range(k, N):
            if tab[i] < tab[imin]:
                imin = i
        echange(tab, k, imin)
        
        
tab = [41, 55, 21, 18, 12, 6, 25]
expected = sorted(tab)
tri_selection(tab)
print(tab)
assert expected == tab, f"le résultat aurait du être{expected} mais vaut {tab}"



#https://www.math93.com/images/pdf/annales_bac/Bac_NSI/bac_NSI_2024/nsi-pratique-2024/24-NSI-01.pdf