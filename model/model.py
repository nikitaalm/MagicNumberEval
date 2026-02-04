import random
from common.imodel import IModel


class Model(IModel):
    def __init__(self):
        self.__magic_number = random.randint(0, 100)
        self.__proposal_count = 0
        self.__max_proposals = 10

    def compareToMagicNumber(self, num: int) -> int:
        self.__proposal_count += 1
        if num == self.__magic_number:
            return 0
        elif num < self.__magic_number:
            return -1
        else:
            return 1

    def getProposalCount(self) -> int:
        return self.__proposal_count

    def getMaxNumberOfProposals(self) -> int:
        return self.__max_proposals
