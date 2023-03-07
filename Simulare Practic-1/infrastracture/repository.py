from domain.entitati import Produs
from errors.exceptii import RepositoryError

class RepoFileProduse:

    def __init__(self, file_path):
        self._produse = []
        self.__file_path = file_path

    def __len__(self):
        return len(self._produse)

    def __read_from_file(self):
        """
        Metoda ce citeste din fisierul destinatie toate produsele si le adauga in repository
        :return:
        """
        self._produse = []
        with open(self.__file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if len(line) > 0:
                    parts = line.split(",")
                    id_produs = int(parts[0])
                    denumire_produs = parts[1]
                    pret_produs = float(parts[2])
                    produs = Produs(id_produs, denumire_produs, pret_produs)
                    self._produse.append(produs)

    def __append_to_file(self, produs):
        """
        Metoda ce adauga in fisierul destinatie, produsul produs
        :param produs:
        """
        with open(self.__file_path, "a") as f:
            f.write(str(produs.get_id_produs()) + "," + str(produs.get_denumire_produs()) + ","
                    + str(produs.get_pret_produs()) + "\n")

    def __write_whole_file(self):
        """
        Metoda ce rescrie intregul fisier cu produsele ce se afla in repositoru
        """
        with open(self.__file_path, "w") as f:
            for produs in self._produse:
                f.write(str(produs.get_id_produs()) + "," + str(produs.get_denumire_produs()) + ","
                    + str(produs.get_pret_produs()) + "\n")

    def adauga_produs_repo(self, produs):
        """
        Metoda ce adauga un produs in repository
        :param produs:
        :raise: "id existent" daca mai exista un client in lista cu acelasi id
        """
        self.__read_from_file()
        for _produs in self._produse:
            if _produs == produs:
                raise RepositoryError("id existent!")
        self._produse.append(produs)
        self.__append_to_file(produs)

    def get_all_produse(self):
        """
        Metoda ce returneaza lista de produse
        :return:
        """
        self.__read_from_file()
        return self._produse[:]


    def sterge_produs(self, id_produs):
        """
        Metoda ce sterge produsul cu id-ul- id_produs din lista produse
        :param produs: Produs
        """
        self.__read_from_file()
        for _produs in self._produse:
            if _produs.get_id_produs() == id_produs:
                self._produse.remove(_produs)
                self.__write_whole_file()



