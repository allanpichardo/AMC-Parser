from AMCParser.amc_parser import parse_asf
from AMCParser.amc_parser import parse_amc


class Subject:

    def __init__(self, id):
        self.__id = id
        asf_path = './data/subjects/{}/{}.asf'.format(id, id)
        self.__joints = parse_asf(asf_path)

    def get_joints(self):
        return self.__joints

    def get_id(self):
        return self.__id

    def get_left_hand(self):
        return self.__joints['lhand']

    def get_right_hand(self):
        return self.__joints['rhand']


class Trial:

    def __init__(self, id, subject, sentiment):
        self.__id = id
        self.__sentiment = sentiment
        amc_path = './data/subjects/{}/{}_{}.amc'.format(subject.get_id(), subject.get_id(), id)
        self.__motions = parse_amc(amc_path)

    def get_motions(self):
        return self.__motions

    def get_sentiment(self):
        return self.__sentiment


