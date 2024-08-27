from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 527)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(20, 0, 360, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(15, 30, 370, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.choose_what_to_do_label = QtWidgets.QLabel(self.centralwidget)
        self.choose_what_to_do_label.setGeometry(QtCore.QRect(20, 50, 360, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choose_what_to_do_label.setFont(font)
        self.choose_what_to_do_label.setObjectName("choose_what_to_do_label")
        self.choose_what_to_do_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.choose_what_to_do_combo_box.setGeometry(QtCore.QRect(20, 80, 360, 35))
        self.choose_what_to_do_combo_box.setCurrentText("")
        self.choose_what_to_do_combo_box.setObjectName("choose_what_to_do_combo_box")
        self.specify_label = QtWidgets.QLabel(self.centralwidget)
        self.specify_label.setGeometry(QtCore.QRect(20, 130, 360, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.specify_label.setFont(font)
        self.specify_label.setObjectName("specify_label")
        self.specify_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.specify_combo_box.setGeometry(QtCore.QRect(20, 160, 360, 35))
        self.specify_combo_box.setObjectName("specify_combo_box")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 200, 360, 241))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.calculate_button = QtWidgets.QPushButton(self.frame, clicked=lambda: self.calculate())
        self.calculate_button.setGeometry(QtCore.QRect(10, 190, 340, 41))
        self.calculate_button.setObjectName("calculate_button")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 9, 340, 171))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.entry1_label = QtWidgets.QLabel(self.frame_2)
        self.entry1_label.setGeometry(QtCore.QRect(0, 50, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.entry1_label.setFont(font)
        self.entry1_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entry1_label.setObjectName("entry1_label")
        self.entry1 = QtWidgets.QTextEdit(self.frame_2)
        self.entry1.setGeometry(QtCore.QRect(105, 50, 230, 30))
        self.entry1.setObjectName("entry1")
        self.entry2_label = QtWidgets.QLabel(self.frame_2)
        self.entry2_label.setGeometry(QtCore.QRect(0, 90, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.entry2_label.setFont(font)
        self.entry2_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entry2_label.setObjectName("entry2_label")
        self.entry2 = QtWidgets.QTextEdit(self.frame_2)
        self.entry2.setGeometry(QtCore.QRect(105, 90, 230, 30))
        self.entry2.setObjectName("entry2")
        self.entry3 = QtWidgets.QTextEdit(self.frame_2)
        self.entry3.setGeometry(QtCore.QRect(105, 130, 230, 30))
        self.entry3.setObjectName("entry3")
        self.entry3_label = QtWidgets.QLabel(self.frame_2)
        self.entry3_label.setGeometry(QtCore.QRect(0, 130, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.entry3_label.setFont(font)
        self.entry3_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entry3_label.setObjectName("entry3_label")
        self.select_unit_combo_box = QtWidgets.QComboBox(self.frame_2)
        self.select_unit_combo_box.setGeometry(QtCore.QRect(105, 10, 230, 30))
        self.select_unit_combo_box.setObjectName("select_unit_combo_box")
        self.select_unit_label = QtWidgets.QLabel(self.frame_2)
        self.select_unit_label.setGeometry(QtCore.QRect(0, 10, 100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.select_unit_label.setFont(font)
        self.select_unit_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.select_unit_label.setObjectName("select_unit_label")
        self.output = QtWidgets.QLabel(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(30, 440, 340, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.output.setFont(font)
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setObjectName("output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect signals to slots
        self.choose_what_to_do_combo_box.currentIndexChanged.connect(self.updateSpecifyComboBox)
        self.specify_combo_box.currentIndexChanged.connect(self.updateParameterFields)

        # Initialize the combo box options
        self.initializeComboBoxes()

    def initializeComboBoxes(self):
        main_items = [("Area", 'area'), ("Surface Area", 'surface_area'), ("Volume", 'volume')]
        for item,data in main_items:
            self.choose_what_to_do_combo_box.addItem(item, data)

        units = ['mm', 'cm', 'm']
        for unit in units:
            self.select_unit_combo_box.addItem(unit)

        # Trigger the first update
        self.updateSpecifyComboBox()

    def updateParameterFields(self):
        self.clear_entries()
        selected_option = self.specify_combo_box.currentData()

        if selected_option == 'rectangle':
            self.entry1_label.setText('Length:')
            self.entry1_label.setVisible(True)
            self.entry2_label.setText('Width:')
            self.entry2_label.setVisible(True)
            self.entry3_label.setVisible(False)
            self.entry1.setVisible(True)
            self.entry2.setVisible(True)
            self.entry3.setVisible(False)

        elif selected_option == 'triangle':
            self.entry1_label.setText('Base:')
            self.entry1_label.setVisible(True)
            self.entry2_label.setText('Height:')
            self.entry2_label.setVisible(True)
            self.entry3_label.setVisible(False)
            self.entry1.setVisible(True)
            self.entry2.setVisible(True)
            self.entry3.setVisible(False)

        elif selected_option == 'circle' or selected_option == 'sphere' or selected_option == 'hemisphere':
            self.entry1_label.setText('Radius:')
            self.entry1_label.setVisible(True)
            self.entry2_label.setVisible(False)
            self.entry3_label.setVisible(False)
            self.entry1.setVisible(True)
            self.entry2.setVisible(False)
            self.entry3.setVisible(False)

        elif selected_option == 'trapezium':
            self.entry1_label.setText('Base a:')
            self.entry1_label.setVisible(True)
            self.entry2_label.setText('Base b:')
            self.entry2_label.setVisible(True)
            self.entry3_label.setText('Height:')
            self.entry3_label.setVisible(True)
            self.entry1.setVisible(True)
            self.entry2.setVisible(True)
            self.entry3.setVisible(True)

        elif selected_option == 'rhombus':
            self.entry1_label.setText('Diagonal a:')
            self.entry2_label.setText('Diagonal b:')
            self.entry3_label.setVisible(False)
            self.entry1.setVisible(True)
            self.entry2.setVisible(True)
            self.entry3.setVisible(False)
        
        elif selected_option == 'parallelogram':
            self.entry1_label.setText('Base:')
            self.entry1_label.setVisible(True)
            self.entry2_label.setText('Height:')
            self.entry2_label.setVisible(True)
            self.entry3_label.setVisible(False)
            self.entry1.setVisible(True)
            self.entry2.setVisible(True)
            self.entry3.setVisible(False)

        elif selected_option == 'square' or selected_option == 'cube':
            self.entry1_label.setText('Side:')
            self.entry1_label.setVisible(True)
            self.entry2_label.setVisible(False)
            self.entry3_label.setVisible(False)
            self.entry1.setVisible(True)
            self.entry2.setVisible(False)
            self.entry3.setVisible(False)

        elif selected_option == 'cuboid' or selected_option == 'pyramidrect':
            self.entry1_label.setText('Height:')
            self.entry1_label.setVisible(True)
            self.entry2_label.setText('Width:')
            self.entry2_label.setVisible(True)
            self.entry3_label.setText('Length:')
            self.entry3_label.setVisible(True)
            self.entry1.setVisible(True)
            self.entry2.setVisible(True)
            self.entry3.setVisible(True)

        elif selected_option == 'cylinder' or selected_option == 'cone':
            self.entry1_label.setText('Height:')
            self.entry1_label.setVisible(True)
            self.entry2_label.setText('Radius:')
            self.entry2_label.setVisible(True)
            self.entry3_label.setVisible(False)
            self.entry1.setVisible(True)
            self.entry2.setVisible(True)
            self.entry3.setVisible(False)

        elif selected_option == 'ellipsoid':
            self.entry1_label.setText('S.max (a):')
            self.entry1_label.setVisible(True)
            self.entry2_label.setText('S.min axis (b):')
            self.entry2_label.setVisible(True)
            self.entry3_label.setText('S.inter axis (c):')
            self.entry3_label.setVisible(True)
            self.entry1.setVisible(True)
            self.entry2.setVisible(True)
            self.entry3.setVisible(True)

    def get_float_value(self, entry):
        """Helper function to convert entry to float and validate it."""
        try:
            return float(entry)
        except ValueError:
            return None     
    
    def clear_entries(self):
        self.entry1.clear()
        self.entry2.clear()
        self.entry3.clear()    

    def show_input_error_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("Input Error")
        msg.setText("The input fields are either empty or contain invalid data. Please enter valid numeric values.")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    def calculate(self):
        selected_main_option = self.choose_what_to_do_combo_box.currentData()
        selected_option = self.specify_combo_box.currentData()
        unit = self.select_unit_combo_box.currentText()

        entry1 = self.entry1.toPlainText()
        entry2 = self.entry2.toPlainText()
        entry3 = self.entry3.toPlainText()

        # Initialize pi
        pi = math.pi

        # Convert entries to floats
        value1 = self.get_float_value(entry1)
        value2 = self.get_float_value(entry2)
        value3 = self.get_float_value(entry3)

        if selected_option == 'rectangle':
            if value1 is not None and value2 is not None:
                area = value1 * value2
                self.output.setText(f"{area} {unit}²")
            else:
                self.show_input_error_message()

        elif selected_option == 'square':
            if value1 is not None:
                area = value1 ** 2
                self.output.setText(f"{area} {unit}²")
            else:
                self.show_input_error_message()

        elif selected_option == 'parallelogram':
            if value1 is not None and value2 is not None:
                area = value1 * value2
                self.output.setText(f"{area} {unit}²")
            else:
                self.show_input_error_message()

        elif selected_option == 'rhombus':
            if value1 is not None and value2 is not None:
                area = value1 * value2
                self.output.setText(f"{area} {unit}²")
            else:
                self.show_input_error_message()

        elif selected_option == 'trapezium':
            if value1 is not None and value2 is not None and value3 is not None:
                area = 0.5 * (value1 + value2) * value3
                self.output.setText(f"{area} {unit}²")
            else:
                self.show_input_error_message()

        elif selected_option == 'circle':
            if value1 is not None:
                area = pi * (value1 ** 2)
                self.output.setText(f"{area} {unit}²")
            else:
                self.show_input_error_message()

        elif selected_option == 'triangle':
            if value1 is not None and value2 is not None:
                area = 0.5 * value1 * value2
                self.output.setText(f"{area} {unit}²")
            else:
                self.show_input_error_message()

        elif selected_option == 'cube' and selected_main_option == 'surface_area':
            if value1 is not None:
                surface_area = 6 * (value1**2)
                self.output.setText(f"{surface_area} {unit}²")
            else:
                self.show_input_error_message()

        elif selected_option == 'cube' and selected_main_option == 'volume':
            if value1 is not None:
                volume = value1**3
                self.output.setText(f"{volume} {unit}³")
            else:
                self.show_input_error_message()

        elif selected_option == 'cylinder' and selected_main_option == 'surface_area':
            if value1 is not None and value2 is not None:
                surface_area = 2 * pi * value2 * (value2 + value1)
                self.output.setText(f"{surface_area} {unit}²")
            else:
                self.show_input_error_message()

        elif selected_option == 'cylinder' and selected_main_option == 'volume':
            if value1 is not None:
                volume = pi * (value2**2) * value1
                self.output.setText(f"{volume} {unit}³")
            else:
                self.show_input_error_message()

        elif selected_option == 'sphere' and selected_main_option == 'surface_area':
            if value1 is not None:
                surface_area = 4 * pi * value1**2
                self.output.setText(f"{surface_area} {unit}²")
            else:
                self.show_input_error_message()

        elif selected_option == 'sphere' and selected_main_option == 'volume':
            if value1 is not None:
                volume = (4/3) * pi * value1**3
                self.output.setText(f"{volume} {unit}³")
            else:
                self.show_input_error_message()

        if selected_option == 'cone' and selected_main_option == 'surface_area':
            if value1 is not None and value2 is not None:
                surface_area = pi * value2 * (value2 + (value1**2 + value2**2)**0.5)
                self.output.setText(f"{surface_area} {unit}²")
            else:
                self.show_input_error_message()

        elif selected_option == 'cone' and selected_main_option == 'volume':
            if value1 is not None:
                volume = (1/3) * pi * (value2**2) * value1
                self.output.setText(f"{volume} {unit}³")
            else:
                self.show_input_error_message()

        elif selected_option == 'hemisphere' and selected_main_option == 'surface_area':
            if value1 is not None:
                surface_area = 3 * pi * value1**2
                self.output.setText(f"{surface_area} {unit}²")
            else:
                self.show_input_error_message()

        elif selected_option == 'hemisphere' and selected_main_option == 'volume':
            if value1 is not None:
                volume = (2/3) * pi * value1**3
                self.output.setText(f"{volume} {unit}³")
            else:
                self.show_input_error_message()

        elif selected_option == 'ellipsoid' and selected_main_option == 'surface_area':
            p = 1.6075
            if value1 is not None and value2 is not None and value3 is not None:
                term1 = (value1 * value2) ** p
                term2 = (value2 * value3) ** p
                term3 = (value3 * value1) ** p
                average = (term1 + term2 + term3) / 3
                surface_area = 4 * math.pi * (average ** (1/p))
                self.output.setText(f"{surface_area:.2f} {unit}²")
            else:
                self.show_input_error_message()

        elif selected_option == 'ellipsoid' and selected_main_option == 'volume':
            if value1 is not None:
                volume = (4/3) * pi * value1 * value2 * value3
                self.output.setText(f"{volume} {unit}³")
            else:
                self.show_input_error_message()

        elif selected_option == 'pyramidrect' and selected_main_option == 'surface_area':
            if value1 is not None and value2 is not None and value3 is not None:
                surface_area = value3 * value2 + value3 * (((value2 / 2) ** 2 + value1 ** 2) ** 0.5) + value2 * (((value3 / 2) ** 2 + value1 ** 2) ** 0.5)
                self.output.setText(f"{surface_area} {unit}²")
            else:
                self.show_input_error_message()

        elif selected_option == 'pyramidrect' and selected_main_option == 'volume':
            if value1 is not None:
                volume = 1/3 * value3 * value2 * value1
                self.output.setText(f"{volume} {unit}³")
            else:
                self.show_input_error_message() 

    def updateSpecifyComboBox(self):
        self.specify_combo_box.clear()
        selected_option = self.choose_what_to_do_combo_box.currentData()

        if selected_option == 'area':
            sub_main_items = [('Rectangle', 'rectangle'), ('Triangle', 'triangle'), ('Circle', 'circle'), ('Trapezium', 'trapezium'), ('Rhombus', 'rhombus'), ('Parallelogram', 'parallelogram'), ('Square', 'square')]
        else:
            sub_main_items = [('Cube', 'cube'), ('Cylinder', 'cylinder'), ('Sphere', 'sphere'), ('Cone', 'cone'), ('Hemisphere', 'hemisphere'), ('Ellipsoid', 'ellipsoid'), ('Pyramid (with a rectangular base)', 'pyramidrect')]

        for item,data in sub_main_items:
            self.specify_combo_box.addItem(item, data)

        # Trigger the parameter field update for the first item
        self.updateParameterFields()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Area, surface area and Volume Finder"))
        self.choose_what_to_do_label.setText(_translate("MainWindow", "Choose what to find:"))
        self.specify_label.setText(_translate("MainWindow", "Specify:"))
        self.calculate_button.setText(_translate("MainWindow", "Calculate"))
        self.entry1_label.setText(_translate("MainWindow", "label 1:"))
        self.entry2_label.setText(_translate("MainWindow", "label 2:"))
        self.entry3_label.setText(_translate("MainWindow", "label 3:"))
        self.select_unit_label.setText(_translate("MainWindow", "Units:"))
        self.output.setText(_translate("MainWindow", "_________"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
