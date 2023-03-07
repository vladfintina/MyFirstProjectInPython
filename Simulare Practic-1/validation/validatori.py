from errors.exceptii import ValidationError


class ValidatorProdus(object):
    """
    Clasa ce valideaza obiectul produs
    """
    def valideaza(self, produs):
        """
        Functie ce valideaa produsul produs
        :param produs:
        :return:
        """
        errors = ""
        if produs.get_id_produs() < 0:
            errors += "id invalid!\n"
        if produs.get_denumire_produs() == "":
            errors += "denumire invalida!\n"
        if produs.get_pret_produs() <= 0:
            errors += "pret invalid!\n"

        if len(errors) > 0:
            raise ValidationError(errors)

