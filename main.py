import sys

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 250, 381, 81))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Круг"))


class MyWidget(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dr = False
        self.pushButton.clicked.connect(self.on_click)

    def paintEvent(self, e):
        super().paintEvent(e)
        if self.dr:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        pos = [random.randint(0, 100) for i in range(2)]
        size = [random.randint(10, 100)] * 2
        color = [random.randint(0, 256) for i in range(3)]
        qp.setBrush(QBrush(QColor(*color), Qt.SolidPattern))
        qp.drawEllipse(*pos, *size)
        pos = [random.randint(100, 200) for i in range(2)]
        size = [random.randint(10, 100)] * 2
        color = [random.randint(0, 256) for i in range(3)]
        qp.setBrush(QBrush(QColor(*color), Qt.SolidPattern))
        qp.drawEllipse(*pos, *size)
        pos = [random.randint(200, 300) for i in range(2)]
        size = [random.randint(10, 100)] * 2
        color = [random.randint(0, 256) for i in range(3)]
        qp.setBrush(QBrush(QColor(*color), Qt.SolidPattern))
        qp.drawEllipse(*pos, *size)

    def on_click(self):
        self.pushButton.setVisible(False)
        self.dr = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
