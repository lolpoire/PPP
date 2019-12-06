#!/usr/bin/python3
# ===========
# Les données
# ===========
# Une école d'ingénieur est modélisé par un dictionnaire {etablissement:{ description:(part1,part2,part3), adresse:(rue,ville,code_postal,n°tel), cordonnees:(lat,long),date_limite:date,image:image}
lat='à compléter'
long='à compléter'
date='à compléter'
ntel='à compléter'
dico_des_écoles={
    "Ensimag":{'description':('à compléter','à compléter','à compléter'), 'adresse':('681 Rue de la Passerelle','Saint-Martin-d\'Hères','38400',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'}, 
    "Ecole 42":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Paris','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'}, 
    "Ecole normale supérieure":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Lyon','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'}, 
    "Insa Toulouse":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Toulouse','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'}, 
    "ENSEEIHT":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Toulouse','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'}, 
    "Centrale Supélec":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Gif-sur-Yvette','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'}, 
    "Université Pierre et Marie Curie":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Paris','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'}, 
    "Télécom-Paristech":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Paris','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'}, 
    "Isima":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Clermont-Ferrand','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'}, 
    "Université Paul Sabatier":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Toulouse','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'},
    "Télécom Nancy":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Nancy','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'},
    "Epita":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Le Kremlin-Bicêtre','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'},
    "Isae - Supaéro":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Toulouse','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'},
    "Insa Lyon":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Lyon','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'},
    "ENSIIE":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Evry','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'},
    "Université Paris Sud":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Paris','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'},
    "Efrei":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Villejuif','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'},
    "Enseirb-Matmeca":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Bordeaux','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'},
    "Université Claude Bernard":{'description':('à compléter','à compléter','à compléter'), 'adresse':('Lyon','à compléter','à compléter',ntel), "cordonnees":(lat,long),"date_limite":date,'image':'à compléter'}
    }



def verifdico(dico):
    for etablissement in dico:
        if len(dico[etablissement])!=5:
            print("erreur,",etablissement,", nombre d'éléments pas respectés")
        if len(dico[etablissement]['description'])!=3:
            print("erreur,",etablissement,", nombre d'éléments de description pas respectés")
        if len(dico[etablissement]['adresse'])!=4:
            print("erreur,",etablissement,", nombre d'éléments d'adresse pas respectés")
        if len(dico[etablissement]["cordonnees"])!=2:
            print("erreur,",etablissement,", nombre d'éléments de cordonnees pas respectés")
        if dico[etablissement]["date_limite"]!=str(dico[etablissement]["date_limite"]):
            print("erreur,",etablissement,",date_limite n'est pas str")
        if dico[etablissement]['image']!=str(dico[etablissement]["date_limite"]):
            print("erreur,",etablissement,", image n'est pas str")
        for elem in dico[etablissement]:
            for elem2 in dico[etablissement][elem]:
                if elem2=='à compléter':
                    print(elem,"de",etablissement,"n'a pas été rempli(e)")