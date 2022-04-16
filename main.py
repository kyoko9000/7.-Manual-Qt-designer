import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from Gui_1 import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        # khai bao nut chay
        self.uic.actionNew.triggered.connect(self.showtext)
    def showtext(self):
        # show no len man hinh text
        self.uic.textEdit_1.setText('hello world')

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
