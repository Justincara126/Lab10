import flet as ft
from UI.view import View
from model.model import Model
from UI.alert import AlertManager


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        try:
            valore_minimo=int(self._view.guadagno_medio_minimo.value)
            lista_coppie_hub=self._model.costruisci_grafo(valore_minimo)
            self._view.lista_visualizzazione.controls.clear()
            num_nodi_ponti=self._model.get_nodi_ponti()
            self._view.lista_visualizzazione.controls.append(ft.Text(f'Ci sono {num_nodi_ponti[0]} nodi e {num_nodi_ponti[1]} edges'))#lista con due numeri/elementi


            #returna una lista di liste, dove ci sono le info dei collegamenti
            for riga in lista_coppie_hub:
                print(riga)
                self._view.lista_visualizzazione.controls.append(ft.Text(f'{riga[0]}: {riga[1]} ---> {riga[2]} -- guadagno medio: {riga[3]}'))
            self._view.update()




            #int(self._view.)
        # TODO
        except ValueError:
            x=AlertManager
            y="SELEZIONARE UN NUMERO!!!"
            x.show_alert(y)



