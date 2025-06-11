import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.main_window import Ui_MainWindow
from db.db_init import init_db

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_connections()

    def setup_connections(self):
        self.ui.addPatientButton.clicked.connect(self.add_patient)

    def add_patient(self):
        name = self.ui.nameInput.text()
        contact = self.ui.contactInput.text()
        # Save to DB logic here

if __name__ == "__main__":
    init_db()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
