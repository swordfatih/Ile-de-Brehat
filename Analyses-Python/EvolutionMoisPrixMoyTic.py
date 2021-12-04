def prixMoyenTicketDuMois(dfDetailTic, dfTicket, mois):
    tabTickets = []
    dfTicket = dfTicket[dfTicket['DateTicket'].str.match(".+[/]%d[/].+" % mois) == True]

    for ticNum in dfTicket['NoTicket']:
        totalTicket = 0.0
        for detailTicNum, prix, remise, qte in zip(dfDetailTic['NoTicket'], dfDetailTic['PrixUnit'], dfDetailTic['Remise%'], dfDetailTic['Qte']):
            if detailTicNum == ticNum:
                prixArticle = 0.0
                prix = prix.replace(',', '.')[0: len(prix) - 2]
                remise = remise.replace(',', '.')
                prixArticle = (float(prix) * int(qte))*(1 - float(remise))
                totalTicket += prixArticle
        tabTickets.append(totalTicket)
    return round(statistics.mean(tabTickets), 2)

