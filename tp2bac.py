def correspond(mot, mot_a_trous) :
    """
    mot : chaine de caractère contenant uniquement des majuscules
    mot_a_trous : chaine de caractère contenenant uniquement des
    majuscules et des caractères *
    Renvoie True si en remplacant * dans mot_a_trous on obtient mot
    Renvoie false sinon
    """
    if len(mot)!= len(mot_a_trous):
        return False
    else:
        for lettre in range(len(mot)):
            if mot[lettre]!= mot_a_trous[lettre] and mot_a_trous[lettre]!= '*':
                return False
        return True
    
    
assert correspond('INFORMATIQUE', '*NFO*MA*IQUE') == True
assert correspond('AUTOMATIQUE', 'INFO*MA*IQUE') == False
assert correspond('STOP', 'S*') == False




def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et
    False sinon.'''
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinataires = 1
    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinataires += 1
    return nb_destinataires == len(plan)



assert est_cyclique({'A':'E','F':'A','C':'D','E':'B','B':'F','D':'C'}) == False
assert est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'}) == True
assert est_cyclique({'A':'B','F':'C','C':'D','E':'A','B':'F','D':'E'}) == True
assert est_cyclique({'A':'B','F':'A','C':'D','E':'C','B':'F','D':'E'}) == False









