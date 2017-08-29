import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "my.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Calculate)

    def Calculate(self):
        price = int(self.textEdit.toPlainText())
        tax = (self.spinBox.value())
        total_price = price + ((tax / 100) * price)
        self.textEdit_2.setText(str(total_price))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

