from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1480, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1780, 720))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(
            "C:\\Users\\YASH SINGH\\OneDrive\\Documents\\SIYA\\512679.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.nouse1 = QtWidgets.QLabel(self.centralwidget)
        self.nouse1.setGeometry(QtCore.QRect(750, 0, 371, 91))
        self.nouse1.setText("")
        self.nouse1.setPixmap(QtGui.QPixmap(
            "C:\\Users\\YASH SINGH\\OneDrive\\Documents\\SIYA\\fram_prev_ui.png"))
        self.nouse1.setScaledContents(True)
        self.nouse1.setObjectName("nouse1")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(800, 10, 250, 65))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
                                      "border-color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(245, 255, 238);\n"
                                      "alternate-background-color: rgb(255, 220, 19);\n"
                                      "font: bold 25pt \"Times New Roman\";")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "C:\\Users\\YASH SINGH\\OneDrive\\Documents\\SIYA\\images_prev_ui.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(35, 35))
        self.pushButton.setCheckable(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.nouse1_2 = QtWidgets.QLabel(self.centralwidget)
        self.nouse1_2.setGeometry(QtCore.QRect(1060, 0, 351, 91))
        self.nouse1_2.setText("")
        self.nouse1_2.setPixmap(QtGui.QPixmap(
            "C:\\Users\\YASH SINGH\\OneDrive\\Documents\\SIYA\\fram_prev_ui.png"))
        self.nouse1_2.setScaledContents(True)
        self.nouse1_2.setObjectName("nouse1_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1100, 10, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
                                        "border-color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(245, 255, 238);\n"
                                        "alternate-background-color: rgb(255, 220, 19);\n"
                                        "font: bold 23pt \"Times New Roman\";")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(
            "C:\\Users\\YASH SINGH\\OneDrive\\Documents\\SIYA\\off-button-round-symbol-isolated-white-off-button-round-white-icon-115332222_prev_ui.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, -90, 771, 281))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(
            "C:\\Users\\YASH SINGH\\OneDrive\\Documents\\SIYA\\BigheartedVagueFoal-size_restricted.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(570, 100, 801, 681))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(
            "C:\\Users\\YASH SINGH\\OneDrive\\Documents\\SIYA\\b709477ff0a3f94d94ace66c49c63e23.gif"))
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 110, 681, 661))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(
            "C:\\Users\\YASH SINGH\\OneDrive\\Documents\\SIYA\\dribbb.gif"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_2.setIndent(-1)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", " Activate"))
        self.pushButton_2.setText(_translate("MainWindow", "Quit SIYA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
