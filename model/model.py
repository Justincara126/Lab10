from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()
        self.lista_hub=[]

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        #print(lista_coppie_hub)
        self.get_num_nodes()
        self.get_num_edges(threshold)
        lista_hub=[]
        for i, (u, v, data) in enumerate(self.G.edges(data=True)):
                lista_hub.append([i + 1, u, v, data.get("weight")])
        #print(lista_hub)
        return lista_hub




        # TODO

    def get_num_edges(self,threshold):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        dao = DAO()
        lista_coppie_hub = dao.get_tratte_hub_valore_medio_maggiore(threshold)
        for coppia in lista_coppie_hub:
            self.G.add_edge(self.lista_hub[coppia[0]],self.lista_hub[coppia[1]], weight=coppia[2])




    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        dao=DAO()
        self.lista_hub = dao.get_hub()
        lista_hub=self.lista_hub
        for hub in lista_hub:
            self.G.add_node(hub)


    def get_all_edges(self,threshold):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO

    def get_nodi_ponti(self):
        x=len(self.G.nodes)
        Y=(len(self.G.edges))
        return [x,Y]












