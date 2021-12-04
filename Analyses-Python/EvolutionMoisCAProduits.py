def caCategorieDuMois(dfDetailTic, dfTicket, dfProduit, catProduit, mois):
    caCategorie = 0.0
    dfTicket = dfTicket[dfTicket['DateTicket'].str.match(".+[/]%d[/].+" % mois) == True]
    dfProduit = dfProduit[dfProduit['Nomprod'].str.match("(?i).+ %s |.+ %s$|.+ %s,$" % (catProduit, catProduit, catProduit)) == True]
    for ticNum in dfTicket['NoTicket']:
        for detailTicNum, prod, prix, remise, qte in zip(dfDetailTic['NoTicket'], dfDetailTic['Refprod'], dfDetailTic['PrixUnit'], dfDetailTic['Remise%'], dfDetailTic['Qte']):
            if ticNum == detailTicNum:
                for refProduit in dfProduit['Refprod']:
                    if prod == refProduit:
                        prixArticle = 0.0
                        prix = prix.replace(',', '.')[0: len(prix) - 2]
                        remise = remise.replace(',', '.')
                        prixArticle = (float(prix) * int(qte))*(1 - float(remise))
                        caCategorie += prixArticle
    return round(caCategorie, 2)
