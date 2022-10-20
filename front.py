import datetime

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog
from betatest import Ui_MainWindow
import sys
from main import main


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.label.setFont(QtGui.QFont('Segoe', 30))
        self.ui.label_2.hide()
        self.ui.savename.hide()
        self.ui.pushButton_2.hide()
        self.ui.pushButton.clicked.connect(self.browsefiles)

    def btnOKclicked(self):
        self.ui.label.setText("Нажали ОК")

    def browsefiles(self):
        self.fname = QFileDialog.getOpenFileName(self, "Open File", "C:", "Лист Microsoft Excel (*.xlsx)")
        self.ui.pushButton_2.clicked.connect(self.make_statement)

    def make_statement(self):
        savefname = f"{str(datetime.datetime.now().date())}_" + self.ui.savename.text()
        main(self.fname[0], savefname)
        # today = rf"\{str(datetime.datetime.now().date())})"
        # pathtosave = r"Рабочий стол\выписка" + today
        # print(pathtosave)
        # if self.ui.savename.text() == "":
        #     main(self.fname[0], r"Рабочий стол\QWERTYUIOP")
        # else:
        #     main(self.fname[0], rf"Рабочий стол\{self.ui.savename.text()}")


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
