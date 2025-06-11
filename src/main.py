import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from main_window import Ui_MainWindow  # this was generated from the .ui file

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()  # create an instance of your layout
        self.ui.setupUi(self)      # build the UI on this window

if __name__ == "__main__":
    app = QApplication(sys.argv)  # start the Qt app
    window = MainApp()            # create your window
    window.show()                 # show it on screen
    sys.exit(app.exec())          # run until user closes it
