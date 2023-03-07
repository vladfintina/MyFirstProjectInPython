from domain.entitati import Produs
from copy import deepcopy


class ServiceProduse:
    def __init__(self, valid_produs, repo_produse):
        self.__valid_produs = valid_produs
        self.__repo_produs = repo_produse
        self._undo_list = []

    def adauga_produs_service(self, id_produs, denumire_produs, pret_produs):
        """
        Metoda ce adauga produsul-produs in lista de produse dupa ce verifica daca acesta eset valid
        :param id_produs:
        :param denumire_produs:
        :param pret_produs:
        """
        produs = Produs(id_produs, denumire_produs, pret_produs)
        self.__valid_produs.valideaza(produs)
        self.__repo_produs.adauga_produs_repo(produs)

    def sterge_produse(self, cifra):
        lista_produse = self.__repo_produs.get_all_produse()
        i = 0
        self._undo_list = deepcopy(lista_produse)
        while i < len(lista_produse):
            produs = lista_produse[i]
            if cifra in str(produs.get_pret_produs()):
                self.__repo_produs.sterge_produs(produs.get_id_produs())
                lista_produse.remove(produs)
            else:
                i = i+1

    def filtrare_produse(self, denumire, pret):
        """
        Metroda care filtreaza produsele din lista dupa denumire si pret, ramandoar produsele in care apare
        string-ul denumire si sunt sub pretul pret
        :param denumire: string
        :param pret: int
        :return: lista produse filtrate
        """
        lista_produse = self.__repo_produs.get_all_produse()
        rezultat = []
        if denumire == "" and pret == -1:
            return lista_produse[:]
        elif denumire == "" and pret != -1:
            for produs in lista_produse:
                if produs.get_pret_produs() < pret:
                    rezultat.append(produs)
            return rezultat[:]
        elif denumire != "" and pret == -1:
            for produs in lista_produse:
                if denumire in produs.get_denumire_produs():
                    rezultat.append(produs)
            return rezultat[:]
        elif denumire != "" and pret != -1:
            for produs in lista_produse:
                if (denumire in produs.get_denumire_produs()) and produs.get_pret_produs()<pret:
                    rezultat.append(produs)
            return rezultat[:]

    def undo(self):
        """
        Metoda ce reface ultima lista de produse din inaintea stergerii
        :return:
        """
        lista_produse = self.__repo_produs.get_all_produse()
        for element in self._undo_list:
            if element not in lista_produse:
                self.__repo_produs.adauga_produs_repo(element)




