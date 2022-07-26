import random
from dataclasses import dataclass


@dataclass
class Predmet:
    predmet = {
        'Russian': 5,
        'Math': 2,
        'Geogrephy': 8,
        'Droch': 1,
        'Fizra-Svivird': 3123,
        'asdf': 3,
        'asd': 3
    }


def predmet_dict(hours) -> dict:
    day = {}

    predmet_copy = list(Predmet.predmet.keys())
    for i in range(1, hours + 1):
        predmet_d = random.choice(predmet_copy)
        predmet_copy.remove(predmet_d)

        day[i] = predmet_d
        Predmet.predmet[predmet_d] -= 1
        if Predmet.predmet[predmet_d] == 0:
            del Predmet.predmet[predmet_d]

    return day


def main():
    mondey_k = 2
    tuesday_k = 5
    wednesday_k = 6
    thursday_k = 4
    friday_k = 3

    try:
        mondey = predmet_dict(mondey_k)
        tuesday = predmet_dict(tuesday_k)
        wednesday = predmet_dict(wednesday_k)
        thursday = predmet_dict(thursday_k)
        friday = predmet_dict(friday_k)

        print(mondey)
        print(tuesday)
        print(wednesday)
        print(thursday)
        print(friday)
    except Exception:
        print("неудалось сформировать расписание")


if __name__ == '__main__':
    main()
