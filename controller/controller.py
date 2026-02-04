# controller.py
from common.imodel import IModel
from common.iview import IView
from common.icontroller import IController


class Controller(IController):
    def __init__(self):
        self.__model: IModel | None = None
        self.__view: IView | None = None

    def setView(self, view: IView) -> None:
        self.__view = view
        self.__view.setActionPerformer(self)

    def setModel(self, model: IModel) -> None:
        self.__model = model
        if self.__view is not None:
            self.__view.setModel(model)

    def start(self) -> None:
        assert self.__model is not None
        assert self.__view is not None

        while self.__model.getProposalCount() < self.__model.getMaxNumberOfProposals():
            remaining = self.__model.getMaxNumberOfProposals() - self.__model.getProposalCount()
            self.__view.showMessage(f"Il vous reste {remaining} tentatives.")
            num = self.__view.askProposal()
            result = self.__model.compareToMagicNumber(num)

            if result == 0:
                self.__view.showMessage("Trouvé")
                return
            elif result < 0:
                self.__view.showMessage("Trop petit")
            else:
                self.__view.showMessage("Trop grand")

        self.__view.showMessage("Perdu !")

    def performProposeNumber(self, num: int) -> None:
        # ici on ne l’utilise pas dans start(), mais on respecte l’interface
        assert self.__model is not None
        assert self.__view is not None
        result = self.__model.compareToMagicNumber(num)
        if result == 0:
            self.__view.showMessage("Trouvé")
        elif result < 0:
            self.__view.showMessage("Trop petit")
        else:
            self.__view.showMessage("Trop grand")
