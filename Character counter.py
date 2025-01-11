def analyser_phrase(phrase):
    longueur = 0
    nombre_mots = 0
    nombre_voyelles = 0
    voyelles = "aeiouAEIOU"
    
    mot_en_cours = False
    
    for caractere in phrase:
        longueur += 1
        
        if caractere in voyelles:
            nombre_voyelles += 1
        
        if caractere == ' ':
            if mot_en_cours:
                nombre_mots += 1
                mot_en_cours = False
        elif caractere == '.':
            if mot_en_cours:
                nombre_mots += 1
            break
        else:
            mot_en_cours = True
    
    return longueur, nombre_mots, nombre_voyelles

phrase = input("Saisissez une phrase qui se termine par un point(.): ")
longueur, nombre_mots, nombre_voyelles = analyser_phrase(phrase)
print(f"Longueur de la phrase : {longueur}")
print(f"Nombre de mots : {nombre_mots}")
print(f"Nombre de voyelles : {nombre_voyelles}")
