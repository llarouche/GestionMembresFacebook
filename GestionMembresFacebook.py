#coding:utf-8
import pandas as pd
import copy
'''
Created on 19 mai 2024

@author: Louis-Alain
'''

def EnleverAccents(iStr):
    wStr=iStr.replace("é","e")
    wStr=wStr.replace("è","e")
    wStr=wStr.replace("ł","l")
    wStr=wStr.replace("ö","o")
    wStr=wStr.replace("-"," ")
    wStr=wStr.replace("."," ")
    wStr=wStr.replace("á","a")
    wStr=wStr.replace("í","i")
    wStr=wStr.replace("ô","o")
    wStr=wStr.replace("è","e")
    wStr=wStr.replace("é","e")
    wStr=wStr.replace("č","c")
    wStr=wStr.replace("ç","c")
    
    
    

    return wStr
    

if __name__ == '__main__':
    
    # Ouvre la liste csv des membres
    
    wListeCsvDataFrame=pd.read_csv("Membres 2024 - Membres.csv")
    wListeCsv=list()
    wDictCourriels=dict()
    wPrenoms=wListeCsvDataFrame["Prénom"]
    wNoms=wListeCsvDataFrame["Nom famille"]
    wCourriels=wListeCsvDataFrame["Courriel"]
    for (wP,wN,wC) in zip(wPrenoms,wNoms,wCourriels):
        wNomPrenom=wP.strip()+" "+wN.strip()
        wNomPrenomSansAccents=EnleverAccents(wNomPrenom.lower())
        wListeCsv.append(wNomPrenomSansAccents)
        wDictCourriels[wNomPrenomSansAccents]=wC
        
    wListeTraduction=pd.read_csv("Correspondances CSV-Facebook.txt")
    wListeTradCsv=wListeTraduction["nom csv"]
    wListeTradFb=wListeTraduction["nom facebook"]
    wPairesTrad=zip(wListeTradCsv,wListeTradFb)
        
    wSetCsv=set(wListeCsv)
    wSetCsvTraduit=copy.copy(wSetCsv)
    
    for wC,wF in wPairesTrad:
        if EnleverAccents(wC) in wSetCsvTraduit:
            wSetCsvTraduit.remove(EnleverAccents(wC))
            wSetCsvTraduit.add(EnleverAccents(wF))
        else:
            print("Mauvaise traduction pour %s vers %s"%(wC,wF))
        
    
    # Ouvre la liste Facebook
    with open("Liste Facebook.txt", encoding="utf-8") as f:
        wSetFacebook=set(f.readlines())
    wSetFacebookSansN=set()
    for wS in wSetFacebook:
        wSetFacebookSansN.add(EnleverAccents(wS.strip().lower()))
    
    # Ouvre la liste des termes non-pertinants (chaines de caractères de ville ou d'entreprise)
    with open("Termes non pertinants.txt", encoding="utf-8") as f:
        wSetNonPertinants=set(f.readlines())
    wSetNonPertinantsSansN=set()
    for wS in wSetNonPertinants:
        wSetNonPertinantsSansN.add(EnleverAccents(wS.strip().lower()))

    # Supprime de la liste Facebook les termes non-pertinants (set)
    wListeFacebookPertinante=list()
    for wF in wSetFacebookSansN:
        wPasDansSet=True
        for wS in wSetNonPertinantsSansN:
            if wS in wF:
                wPasDansSet=False
                break
        if wPasDansSet:
            wListeFacebookPertinante.append(wF)
    wSetFacebookPertinant=set(wListeFacebookPertinante)
    
    # Identifie les membres du csv présents dans la liste Facebook
    wSetDansCsvDansFacebook=wSetCsvTraduit.intersection(wSetFacebookPertinant)

    wSetDansCsvPasDansFacebook=sorted(wSetCsvTraduit-wSetFacebookPertinant)
    
    wSetIntrusPossibles=sorted(wSetFacebookPertinant-wSetDansCsvDansFacebook)
    
    with open("Intrus possibles.txt",'w', encoding="utf-8") as f:
        for wS in wSetIntrusPossibles:
            f.write(wS+"\n")
        
    with open("DansCsvPasDansFacebook.txt",'w', encoding="utf-8") as f:
        for wS in wSetDansCsvPasDansFacebook:
            f.write(wS+"\n")
    
    with open("CourrielsÀEnvoyerPourNomFacebook.txt",'w', encoding="utf-8") as f:
        for wS in wSetDansCsvPasDansFacebook:
            f.write(wDictCourriels[wS]+";")        
    # Ouvre le fichier Manuel_DansCsvDansFacebook (nom csv.  nom Facebook)
    
    # Crée une liste DansCsvPasDansFacebook (tous les autres du csv)
    '''
    wDansCsvPasDansFacebook=list()
    for wLC in wListeCsv:
        if wLC not in wDansCsvDansFacebook:
            # Regarde toutes les lignes et valide si la personne est dans Facebook
            if wLC in wListeFacebook:
                wDansCsvDansFacebook[wLC]=wLC
            else:
                wDansCsvPasDansFacebook.append(wLC)
    
    # Supprime de la liste Facebook les personnes dans le csv: crée la liste intrus possibles
    wIntrusPossibles=list()
    wFacebookConnus=set()
    wListeFacebookPertinants
    wIntrusPossibles=wListeFacebookPertinants-wFacebookConnus
    
    # Écrit le fichier: intrus possibles
    # Écrit le fichier: DansCsvPasDansFacebook
    '''
    
    # 
    pass