from garazas import Garazas
import pandas

garazas = Garazas()

if __name__ == "__main__":
    while True:
        veiksmas = int(input("1 - įvesti auto, 2 - įvesti elektroauto, 3 - peržiūrėti, 0 - išeiti: "))
        match veiksmas:
            case 1: garazas.prideti_auto()
            case 2: garazas.prideti_elektromobili()
            case 3: garazas.atvaizduoti_auto()
            case 0: break
            case _: print("Neteisingas pasirinkimas")
