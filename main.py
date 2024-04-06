from PyQt5.QtWidgets import QApplication, QMainWindow, QShortcut, QDesktopWidget, QMdiSubWindow, QWidget

from PyQt5.QtCore import Qt

import sys
from acht import Ui_MainWindow as ACHT
from eighhttt import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acht")

        self.open_windows = []
        self.minimized_windows = []

        self.custom_ui = Ui_MainWindow()
        self.custom_ui.setupUi(self)

class SecondWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Acht")

        self.open_windows = []
        self.minimized_windows = []

        self.custom_ui = ACHT()
        self.custom_ui.setupUi(self)
        # Create a shortcut for F11 to toggle fullscreen
        #self.shortcut = QShortcut(Qt.Key_F11, self)
        #self.shortcut.activated.connect(self.toggle_fullscreen)

        # Resize the main window to fit the screen
        # screen = QDesktopWidget().availableGeometry()
        # self.resize(screen.width(), screen.height())


secondWin = None
def eighth():
    global secondWin
    secondWin = SecondWindow()  # Erstellen Sie eine neue MainWindow-Instanz
    secondWin.showFullScreen() 

def main():
    
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    
    mainWin.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    