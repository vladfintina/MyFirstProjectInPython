from errors.exceptii import ValidationError, RepositoryError


class Console:
    def __init__(self, srv_produse):
        self.__srv_produse = srv_produse

    def __ui_adauga_produs(self):
        try:
            id_produs = int(input("Introduceti  id-ul produsului:"))
        except ValueError:
            print("Valoare numerica invalida pentru id!")
            return
        denumire_produs = input("Introduceti denumirea produsului:")
        try:
            pret_produs = float(input("Introduceti  pretul produsului:"))
        except ValueError:
            print("Valoare numerica invalida pentru pret!")
            return
        try:
            self.__srv_produse.adauga_produs_service(id_produs, denumire_produs, pret_produs)
        except RepositoryError as re:
            print("repository error: " + str(re))
        except ValidationError as ve:
            print("validation error: " + str(ve))

    def __ui_stergere_produse(self):
        try:
            cifra = int(input("Introduceti cifra: "))
        except ValueError:
            print("Valoare numerica invalida pentru cifra!")
            return
        if cifra < 0 or cifra >=10:
            print("Nu este cifra!")
            return
        self.__srv_produse.sterge_produse(str(cifra))

    def __ui_filtrare_produse(self):
        denumire = input("Intoduceti sirul dupa care doriti sa fie filtrate produsele: ")
        try:
            pret = int(input("Introduceti pretul dupa care sa fie filtrate produsele: "))
        except ValueError:
            print("Valoare numerica invalida pentru cifra!")
            return
        if pret<0 and pret!=-1:
            print("Valoare invalida pentru pret:")
            return
        rezultat = self.__srv_produse.filtrare_produse(denumire, pret)
        for produs in rezultat:
            print(produs)

    def __ui__undo(self):
        self.__srv_produse.undo()


    def __ui_afisare_meniu(self):
        print("1.Adaugare produs")
        print("2.Stergere produs")
        print("3.Filtare produse")
        print("4.Undo")
        print("exit-pentru a iesi din aplicatie")

    def run(self):
        while True:
            self.__ui_afisare_meniu()
            cmd = input(">>>")
            if cmd == "exit":
                return
            elif cmd == "":
                return
            elif cmd == "1":
                self.__ui_adauga_produs()
            elif cmd == "2":
                self.__ui_stergere_produse()
            elif cmd == "3":
                self.__ui_filtrare_produse()
            elif cmd == "4":
                self.__ui__undo()
            else:
                print("Comanda invalida!")




