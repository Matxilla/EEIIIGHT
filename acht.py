from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Vollbild-Bildanzeige")
        MainWindow.showFullScreen()  # Vollbild anzeigen
        self.centralwidget = QtWidgets.QLabel(MainWindow)
        self.centralwidget.setScaledContents(True)  # Bild skalieren
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setPixmap(QtGui.QPixmap("E:\Coding\EIGHHHHT\png-transparent-eight-number-8-digit-thumbnail.png"))
        MainWindow.setCentralWidget(self.centralwidget)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    sys.exit(app.exec_())
