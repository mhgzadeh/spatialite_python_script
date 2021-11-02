from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QPushButton, QLabel, QLineEdit, QFileDialog, QDesktopWidget
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.input_data = {'input_file': None, "output_folder": None, 'epsg_num': None}
        # Load the ui file
        uic.loadUi("ui_files/first.ui", self)
        # Initialize ui widgets
        self.init_ui()
        # Centralize main window
        self.centralize_window()

    def init_ui(self):
        # Define our widgets
        QDesktopWidget().availableGeometry().center()

        self.findChild(QPushButton, 'btn_input')
        self.findChild(QPushButton, 'btn_output')
        self.findChild(QPushButton, 'btn_submit')
        self.findChild(QLabel, 'lbl_epsg_num')
        self.findChild(QLineEdit, 'le_input')
        self.findChild(QLineEdit, 'le_output')
        self.findChild(QLineEdit, 'le_epsg_num')

        # Click the input, output, submit button
        self.btn_input.clicked.connect(self.file_name_selector)
        self.btn_output.clicked.connect(self.folder_name_selector)
        self.btn_submit.clicked.connect(self.get_epsg_num)
        # Show the app
        self.show()

    def centralize_window(self):
        frame_geometry = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        center_point = QApplication.desktop().screenGeometry(screen).center()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())

    def file_name_selector(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Input File", "", "SQL Files (*.sql)")
        if file_name:
            self.le_input.setText(file_name)
            self.input_data['input_file'] = file_name

    def folder_name_selector(self):
        folder_name = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if folder_name:
            self.le_output.setText(folder_name)
            self.input_data['output_folder'] = folder_name

    def get_epsg_num(self):
        self.input_data["epsg_num"] = self.le_epsg_num.text()
        self.close()
