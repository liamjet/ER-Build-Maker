from PyQt6.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        combobox1 = QComboBox()
        combobox1.addItems(['Helmet1', 'Helmet2', 'Helmet3', 'Helmet4'])

        combobox2 = QComboBox()
        combobox2.addItems(['Armor1', 'Armor2', 'Armor3', 'Armor4'])

        combobox3 = QComboBox()
        combobox3.addItems(['Gauntlets1', 'Gauntlets2', 'Gauntlets3', 'Gauntlets4'])

        combobox4 = QComboBox()
        combobox4.addItems(['Leggings1', 'Leggings2', 'Leggings3', 'Leggings4'])

        

        layout = QVBoxLayout()
        layout.addWidget(combobox1)
        layout.addWidget(combobox2)
        layout.addWidget(combobox3)
        layout.addWidget(combobox4)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.setWindowTitle('Elden Ring Build Calculator')

    def current_text_changed(self, s):
        print("Current text: ", s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()