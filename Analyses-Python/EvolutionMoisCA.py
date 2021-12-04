def caDuMois(dfDetailTic, dfTicket, mois):
    chiffreDaffaires = 0.0
    dfTicket = dfTicket[dfTicket['DateTicket'].str.match(".+[/]%d[/].+" % mois) == True]
    
    for ticNum in dfTicket['NoTicket']:
        for detailTicNum, prix, remise, qte in zip(dfDetailTic['NoTicket'], dfDetailTic['PrixUnit'], dfDetailTic['Remise%'], dfDetailTic['Qte']):
            if detailTicNum == ticNum:
                prixArticle = 0.0
                prix = prix.replace(',', '.')[0: len(prix) - 2]
                remise = remise.replace(',', '.')
                prixArticle = (float(prix) * int(qte))*(1 - float(remise))
                chiffreDaffaires += prixArticle
    return round(chiffreDaffaires, 2)