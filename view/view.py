# view.py
from common.iview import IView
from common.imodel import IModel
from common.icontroller import IController


class View(IView):
    def __init__(self):
        self.__model: IModel | None = None
        self.__controller: IController | None = None

    def setActionPerformer(self, actionPerformer: IController) -> None:
        self.__controller = actionPerformer

    def setModel(self, model: IModel) -> None:
        self.__model = model

    def setController(self, model: IController) -> None:
        self.__controller = model

    def showMessage(self, message: str) -> None:
        print(message)

    def askProposal(self) -> int:
        while True:
            try:
                s = input("Entrez une proposition de nombre :\n")
                return int(s)
            except ValueError:
                print("Veuillez entrer un nombre entier.")
