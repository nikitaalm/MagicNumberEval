import random

from common.imodel import IModel


class Model(IModel):
    # To be completed
    def __init__(self):
        self.__magicNumber = random.randint(1, 100)  # Exemple de plage
        self.__proposalCount = 0
        self.__maxNumberOfProposals = 10

    def compareToMagicNumber(self, num: int) -> int:
        self.__proposalCount += 1
        if num < self.__magicNumber:
            return -1  # Plus grand
        elif num > self.__magicNumber:
            return 1  # Plus petit
        else:
            return 0  # Gagné

    def getProposalCount(self) -> int:
        return self.__proposalCount

    def getMaxNumberOfProposals(self) -> int:
        return self.__maxNumberOfProposals
