import unittest
from validation.validatori import ValidatorProdus
from infrastracture.repository import RepoFileProduse
from business.servicii import ServiceProduse
from domain.entitati import Produs
from errors.exceptii import RepositoryError, ValidationError

class Teste(unittest.TestCase):

    def setUp(self):
        file_path_produse = "test_produse.txt"

        self.valid_produs = ValidatorProdus()
        self.repo_produse = RepoFileProduse(file_path_produse)
        self.srv_produse = ServiceProduse(self.valid_produs, self.repo_produse)

        with open(file_path_produse, "w") as f:
            f.write("")

    def tearDown(self):
        pass

    def test_creeaza_produs(self):
        id_produs = 1
        denumire_produs = "cafea"
        pret_produs = 12.05
        produs = Produs(id_produs, denumire_produs, pret_produs)
        self.assertEqual(produs.get_id_produs(), 1)
        self.assertEqual(produs.get_denumire_produs(), denumire_produs)
        self.assertEqual(produs.get_pret_produs(), pret_produs)

    def test_adauga_produs(self):
        self.assertEqual(len(self.repo_produse), 0)
        id_produs = 2
        denumire_produs = "cafea"
        pret_produs = 12.05
        produs = Produs(id_produs, denumire_produs, pret_produs)
        self.repo_produse.adauga_produs_repo(produs)
        with self.assertRaises(RepositoryError) as re:
            self.repo_produse.adauga_produs_repo(produs)
        self.assertEqual(str(re.exception), "id existent!")

    def test_get_all_produse(self):
        self.assertEqual(len(self.repo_produse), 0)
        id_produs = 2
        id_produs2 = 3
        denumire_produs = "cafea"
        pret_produs = 12.05
        produs = Produs(id_produs, denumire_produs, pret_produs)
        self.repo_produse.adauga_produs_repo(produs)
        produs2 = Produs(id_produs2, denumire_produs, pret_produs)
        self.repo_produse.adauga_produs_repo(produs2)
        lista = self.repo_produse.get_all_produse()
        self.assertEqual(len(lista), 2)

    def test_valideaza_produs(self):
        id_produs = -5
        denumire_produs = ""
        pret_produs = -12.05
        produs = Produs(id_produs, denumire_produs, pret_produs)
        with self.assertRaises(ValidationError) as ve:
            self.valid_produs.valideaza(produs)
        self.assertEqual(str(ve.exception), "id invalid!\ndenumire invalida!\npret invalid!\n")

    def test_adauga_produs_service(self):
        id_produs = -5
        denumire_produs = ""
        pret_produs = -12.05
        with self.assertRaises(ValidationError) as ve:
            self.srv_produse.adauga_produs_service(id_produs, denumire_produs, pret_produs)
        self.assertEqual(str(ve.exception), "id invalid!\ndenumire invalida!\npret invalid!\n")
        id_produs2 = 5
        denumire_produs2 = "lapte"
        pret_produs2 = 12.05
        self.srv_produse.adauga_produs_service(id_produs2, denumire_produs2, pret_produs2)
        lista = self.repo_produse.get_all_produse()
        self.assertEqual(len(lista), 1)
        self.assertEqual(lista[0].get_id_produs(), 5)

    def test_sterge_produs(self):
        id_produs2 = 5
        denumire_produs2 = "lapte"
        pret_produs2 = 12.05
        produs2 = Produs(id_produs2, denumire_produs2, pret_produs2)
        self.srv_produse.adauga_produs_service(id_produs2, denumire_produs2, pret_produs2)
        id_produs1 = 9
        denumire_produs1 = "lapte"
        pret_produs1 = 12.05
        self.srv_produse.adauga_produs_service(id_produs1, denumire_produs1, pret_produs1)
        self.repo_produse.sterge_produs(id_produs2)
        self.assertEqual(self.repo_produse.__len__(), 1)
        lista = self.repo_produse.get_all_produse()
        self.assertEqual(lista[0].get_id_produs(), 9)

    def test_sterge_produse_service(self):
        id_produs = 5
        denumire_produs = "lapte"
        pret_produs = 13.05
        id_produs2 = 6
        denumire_produs2 = "lapte"
        pret_produs2 = 12.05
        id_produs3 = 7
        denumire_produs3 = "lapte"
        pret_produs3 = 12.06
        self.srv_produse.adauga_produs_service(id_produs, denumire_produs, pret_produs)
        self.srv_produse.adauga_produs_service(id_produs2, denumire_produs2, pret_produs2)
        self.srv_produse.adauga_produs_service(id_produs3, denumire_produs3, pret_produs3)
        self.srv_produse.sterge_produse("5")
        self.assertEqual(self.repo_produse.__len__(), 1)


    def test_filtrare_produse(self):
        id_produs = 5
        denumire_produs = "lapte"
        pret_produs = 13.05
        id_produs2 = 6
        denumire_produs2 = "paste"
        pret_produs2 = 12.05
        id_produs3 = 7
        denumire_produs3 = "miere"
        pret_produs3 = 12.06
        self.srv_produse.adauga_produs_service(id_produs, denumire_produs, pret_produs)
        self.srv_produse.adauga_produs_service(id_produs2, denumire_produs2, pret_produs2)
        self.srv_produse.adauga_produs_service(id_produs3, denumire_produs3, pret_produs3)
        rezultat1 = self.srv_produse.filtrare_produse("te", 13)
        self.assertEqual(len(rezultat1), 1)
        rezultat2= self.srv_produse.filtrare_produse("re",-1)
        self.assertEqual(len(rezultat2), 1)

    def test_undo(self):
        id_produs = 5
        denumire_produs = "lapte"
        pret_produs = 13.05
        id_produs2 = 6
        denumire_produs2 = "paste"
        pret_produs2 = 12.05
        id_produs3 = 7
        denumire_produs3 = "miere"
        pret_produs3 = 12.06
        self.srv_produse.adauga_produs_service(id_produs, denumire_produs, pret_produs)
        self.srv_produse.adauga_produs_service(id_produs2, denumire_produs2, pret_produs2)
        self.srv_produse.adauga_produs_service(id_produs3, denumire_produs3, pret_produs3)
        self.srv_produse.sterge_produse("5")
        self.assertEqual(self.repo_produse.__len__(), 1)
        self.srv_produse.undo()
        lista = self.repo_produse.get_all_produse()
        #for el in lista:
        #    print(el)
        self.assertEqual(self.repo_produse.__len__(), 3)



