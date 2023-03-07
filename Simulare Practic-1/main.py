from validation.validatori import ValidatorProdus
from infrastracture.repository import RepoFileProduse
from business.servicii import ServiceProduse
from interface.user_interface import Console
if __name__ == '__main__':
    valid_produs = ValidatorProdus()

    repo_produse = RepoFileProduse("Produse.txt")

    srv_produse = ServiceProduse(valid_produs, repo_produse)

    ui = Console(srv_produse)

    ui.run()

