import sys
from PyQt5.QtWidgets import QApplication
from add_edit_geometry_in_sql import AddGeometry
from pyqt_gui_designer import MainWindow

if __name__ == "__main__":
    # Create app and window by PyQt5
    app = QApplication(sys.argv)
    main_window = MainWindow()
    app.exec_()
    # Get inputs by PyQt5
    add_geometry_inputs = main_window.input_data
    output_file = add_geometry_inputs["input_file"].split('/')[-1].split('.')[0] + '_edited.sql'
    # Generate edited sql queries
    add_geometry = AddGeometry(add_geometry_inputs["epsg_num"],
                               add_geometry_inputs["input_file"],
                               output_file)
    print('Successfully done.')
