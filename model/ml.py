import sklearn
import pickle
from datetime import datetime

counters = {
    '149157': 'Haukkalampi - Solvalla yhdysreitin kävijälaskuri',
    '151989': 'Nuuksio, Veikkolan kävijälaskuri',
    '186819': 'Mustakorventien 2. laskuri',
    '188852': 'Siikaranta kävijälaskuri',
    '109144': 'Kattila niityn portin kävijälaskuri',
    '125383': 'Nuuksio Takalanpolun laskuri',
    '94722': 'Klassarinkierroksen kävijälaskuri',
    '51257': 'Haukkalammen ekopisteen kävijälaskuri',
    '168237': 'Matalajärven kävijälaskuri'
}

features = {
    'hour': 0,
    'weekday_0': 0,
    'weekday_1': 0,
    'weekday_2': 0,
    'weekday_3': 0,
    'weekday_4': 0,
    'weekday_5': 0,
    'weekday_6': 0,
    'month_1': 0,
    'month_2': 0,
    'month_3': 0,
    'month_4': 0,
    'month_5': 0,
    'month_6': 0,
    'month_7': 0,
    'month_8': 0,
    'month_9': 0,
    'month_10': 0,
    'month_11': 0,
    'month_12': 0,
    '51257': 0,
    '94722': 0,
    '109144': 0,
    '125383': 0,
    '149157': 0,
    '151989': 0,
    '168237': 0,
    '186819': 0,
    '188852': 0
}


counters = {
    '149157': 'Haukkalampi - Solvalla yhdysreitin kävijälaskuri',
    '151989': 'Nuuksio, Veikkolan kävijälaskuri',
    '186819': 'Mustakorventien 2. laskuri',
    '188852': 'Siikaranta kävijälaskuri',
    '109144': 'Kattila niityn portin kävijälaskuri',
    '125383': 'Nuuksio Takalanpolun laskuri',
    '94722': 'Klassarinkierroksen kävijälaskuri',
    '51257': 'Haukkalammen ekopisteen kävijälaskuri',
    '168237': 'Matalajärven kävijälaskuri'
}


class Ml:
    def __init__(self, model_file='model.sav'):
        self.model = pickle.load(open(model_file, 'rb'))

    def __create_features(self, timestamp, counter):
        fe = features.copy()
        dt = datetime.utcfromtimestamp(timestamp)
        fe['hour'] = dt.hour
        fe['weekday_' + str(dt.weekday())]
        fe['month_' + str(dt.month)]
        fe[counter] = 1
        return [list(fe.values())]

    def predict(self, timestamp, counter=None):
        if counter:
            fe = self.__create_features(timestamp, counter)
            result = self.model.predict(fe)[0]
            return result

        result = 0
        for c in counters:
            fe = self.__create_features(timestamp, c)
            result += self.model.predict(fe)[0]

        return result
