def depenseProdClient(tabClients, tabMois, dfTicket, dfDetailTic, dfProduit, catProduit):
    tabDepClients = []
    for i in range(len(tabClients)):
        colonne = []
        for j in range(len(tabMois)):
            colonne.append(0.0)
        tabDepClients.append(colonne)

    for i in range(len(tabClients)):
        dfProduit = dfProduit[dfProduit['Nomprod'].str.match("(?i).+ %s |.+ %s$|.+ %s,$" % (catProduit, catProduit, catProduit)) == True]
        for j in range(len(tabMois)):
            dfTicketMois = dfTicket[dfTicket['DateTicket'].str.match(".+[/]%d[/].+" % tabMois[j]) == True]
            depenseTotale = 0.0
            for codeCliTic, numTic in zip(dfTicketMois['CodeCli'], dfTicketMois['NoTicket']):
                if tabClients[i].code == codeCliTic:
                    for numTicDet, prod, prix, remise, qte in zip(dfDetailTic['NoTicket'], dfDetailTic['Refprod'], dfDetailTic['PrixUnit'], dfDetailTic['Remise%'], dfDetailTic['Qte']):
                        if numTic == numTicDet:
                            for refProduit in dfProduit['Refprod']:
                                if prod == refProduit:
                                    prixArticle = 0.0
                                    prix = prix.replace(',', '.')[0: len(prix) - 2]
                                    remise = remise.replace(',', '.')
                                    prixArticle = (float(prix) * int(qte))*(1 - float(remise))
                                    depenseTotale += prixArticle
            tabDepClients[i][j] = round(depenseTotale, 2)
    return tabDepClients