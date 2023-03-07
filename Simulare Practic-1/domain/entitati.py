
class Produs():
    """
    Clasa Produs creeaza obiectul produs cu atributele:
            id_produs -int
            denumire -string
            pret; float
    """
    def __init__(self, id_produs, denumire, pret):
        self.__id_produs = id_produs
        self.__denumire = denumire
        self.__pret = pret

    def get_id_produs(self):
        return int(self.__id_produs)

    def get_denumire_produs(self):
        return self.__denumire

    def get_pret_produs(self):
        return float(self.__pret)

    def __eq__(self, other):
        return self.__id_produs == other.__id_produs

    def __str__(self):
        return "[" +str(self.__id_produs) + "," + str(self.__denumire) + "," + str(self.__pret) + "]"

