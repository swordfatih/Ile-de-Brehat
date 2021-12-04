import numpy as np

def prixMoyenClient(tabClients, dfDetailTic, dfTicket, dfClient):
    NaN = float("NaN")
    for i in range(len(tabClients)):
        tabTickets = []
        for codeCliTic, numTic in zip(dfTicket['CodeCli'], dfTicket['NoTicket']):
            if tabClients[i].code == codeCliTic:
                prixTicket = 0.0
                for numTicDet, prix, remise, qte in zip(dfDetailTic['NoTicket'], dfDetailTic['PrixUnit'], dfDetailTic['Remise%'], dfDetailTic['Qte']):
                    if numTic == numTicDet:
                        prixArticle = 0.0
                        prix = prix.replace(',', '.')[0: len(prix) - 2]
                        remise = remise.replace(',', '.')
                        prixArticle = (float(prix) * int(qte))*(1 - float(remise))
                        prixTicket += prixArticle
                tabTickets.append(prixTicket)
        if(np.isnan(round(np.mean(tabTickets), 2))):
            tabClients[i].prix = 0.0
        else: tabClients[i].prix = round(np.mean(tabTickets), 2)
    return tabClients