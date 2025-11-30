from database.DB_connect import DBConnect
from model.compagnia import Compagnia
from model.hub import Hub
from model.spedizione import Spedizione


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    def get_compagnia(self):
        DB=DBConnect.get_connection()
        cursor=DB.cursor(dictionary=True)
        cursor.execute("select * from compagnia")
        result=[]
        for row in cursor:
            result.append(Compagnia(row['id'],row['codice'],row['nome']))
        return result
    def get_hub(self):
        DB=DBConnect.get_connection()
        cursor=DB.cursor(dictionary=True)
        cursor.execute("select * from hub")
        result=[]
        for row in cursor:
            result.append(Hub(row['id'],row['codice'],row['nome'],row['citta'],row['stato'],row['latitudine'],row['longitudine']))
        return result
    def get_spedizione(self):
        DB=DBConnect.get_connection()
        cursor=DB.cursor(dictionary=True)
        cursor.execute("select * from spedizione")
        result=[]
        for row in cursor:
            result.append(Spedizione(row['id'],row['id_compagnia'],row['numero_tracking'],row['id_hub_origine'],row['id_hub_destinazione'],row['data_ritiro_programmata'],row['distanza'],row['data_consegna'],row['valore_merce']))



    def get_tratte_hub_valore_medio_maggiore(self,valore_minimo):
        DB=DBConnect.get_connection()
        cursor=DB.cursor()
        query=('''SELECT LEAST(s.id_hub_origine,s.id_hub_destinazione),GREATEST(s.id_hub_origine,s.id_hub_destinazione),SUM(valore_merce) AS tot,COUNT(*) as num
            FROM spedizione s
            GROUP BY s.id_hub_origine,s.id_hub_destinazione''')

        cursor.execute(query)
        coppie_hub=[]
        for row in cursor:
            hub_partenza=row[0]
            hub_arrivo=row[1]
            somma=row[2]
            count=row[3]
            media=somma/count
            if media >= valore_minimo:
                #print(hub_partenza,hub_arrivo,media)
                coppie_hub.append([hub_partenza,hub_arrivo,media])
        cursor.close()
        DB.close()
        return coppie_hub