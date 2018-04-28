# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\set_detector_ip_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(351, 199)
        font = QtGui.QFont()
        font.setPointSize(14)
        Dialog.setFont(font)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.ledt_buero = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ledt_buero.setFont(font)
        self.ledt_buero.setObjectName("ledt_buero")
        self.gridLayout.addWidget(self.ledt_buero, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.ledt_garage = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ledt_garage.setFont(font)
        self.ledt_garage.setObjectName("ledt_garage")
        self.gridLayout.addWidget(self.ledt_garage, 2, 1, 1, 1)
        self.ledt_werkstatt = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ledt_werkstatt.setFont(font)
        self.ledt_werkstatt.setObjectName("ledt_werkstatt")
        self.gridLayout.addWidget(self.ledt_werkstatt, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Setze IP-Adressen"))
        self.ledt_buero.setText(_translate("Dialog", "http://192.168.188.177"))
        self.label.setText(_translate("Dialog", "Büro"))
        self.ledt_garage.setText(_translate("Dialog", "http://192.168.188.179"))
        self.ledt_werkstatt.setText(_translate("Dialog", "http://192.168.188.178"))
        self.label_2.setText(_translate("Dialog", "Werkstatt"))
        self.label_3.setText(_translate("Dialog", "Garage"))

