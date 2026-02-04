from common.imodel import IModel
from common.iview import IView
from common.icontroller import IController


class Controller(IController):
    #def __init__(self):
        self.__view = None
        self.__model = None

    def setView(self, view: IView) -> None:
        pass
        self.__view = view
    def setModel(self, model: IModel) -> None:
        self.__model = model

    def start(self) -> None:
        self.__view.showMessage("Bienvenue dans le jeu du Nombre Magique !")
        # Boucle de jeu simple
        isOver = False
        while not isOver:
            if self.__model.getProposalCount() >= self.__model.getMaxNumberOfProposals():
                self.__view.showMessage("Dommage, vous avez épuisé vos essais !")
                isOver = True
            else:
                proposal = self.__view.askProposal()
                self.performProposeNumber(proposal)
                # On vérifie si le dernier coup était gagnant via le modèle (optionnel selon implémentation)

    def performProposeNumber(self, num: int) -> None:
        result = self.__model.compareToMagicNumber(num)
        if result == -1:
            self.__view.showMessage("C'est plus grand !")
        elif result == 1:
            self.__view.showMessage("C'est plus petit !")
        else:
            self.__view.showMessage(f"Félicitations ! Trouvé en {self.__model.getProposalCount()} coups.")
            exit()  # Fin du jeu
