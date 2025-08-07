from models.elektromobilis import Automobilis, Elektromobilis
import pickle

class Garazas:
    def __init__(self):
        self.automobiliai = self.nuskaityti_is_failo()

    def irasyti_i_faila(self):
        with open("automobiliai.pkl", 'wb') as file:
            pickle.dump(self.automobiliai, file)

    def nuskaityti_is_failo(self):
        try:
            with open("automobiliai.pkl", 'rb') as file:
                automobiliai = pickle.load(file)
        except:
            automobiliai = []
        return automobiliai

    def prideti_auto(self):
        marke = input("Markė: ")
        modelis = input("Modelis: ")
        metai = int(input("Metai: "))
        auto = Automobilis(marke, modelis, metai)
        self.automobiliai.append(auto)
        self.irasyti_i_faila()

    def prideti_elektromobili(self):
        marke = input("Markė: ")
        modelis = input("Modelis: ")
        metai = int(input("Metai: "))
        talpa = int(input("Talpa: "))
        auto = Elektromobilis(marke, modelis, metai, talpa)
        self.automobiliai.append(auto)
        self.irasyti_i_faila()

    def atvaizduoti_auto(self):
        for auto in self.automobiliai:
            print(auto)