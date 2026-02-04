from common.iview import IView
from common.imodel import IModel
from common.icontroller import IController


class View(IView):
    #def __init__(self):
        self.__model = None
        self.__controller = None

    def setActionPerformer(self, actionPerformer: IController) -> None:
        self.__controller = actionPerformer

    def setModel(self, model: IModel) -> None:
        self.__model = model

    def setController(self, model: IController) -> None:
        self.__controller = controller

    def showMessage(self, message: str) -> None:
        print(message)

    def askProposal(self) -> int:
        try:
            val = int(input(f"Essai n°{self.__model.getProposalCount() + 1} - Entrez un nombre : "))
            return val
        except ValueError:
            self.showMessage("Veuillez entrer un nombre valide.")
            return self.askProposal()
