# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desires_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(582, 523)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.table_desire = QtWidgets.QTableView(Form)
        self.table_desire.setObjectName("table_desire")
        self.verticalLayout.addWidget(self.table_desire)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.del_desires_btn = QtWidgets.QPushButton(Form)
        self.del_desires_btn.setObjectName("del_desires_btn")
        self.horizontalLayout.addWidget(self.del_desires_btn)
        self.add_desires_btn = QtWidgets.QPushButton(Form)
        self.add_desires_btn.setObjectName("add_desires_btn")
        self.horizontalLayout.addWidget(self.add_desires_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Список ваших желаний"))
        self.del_desires_btn.setText(_translate("Form", "Удалить"))
        self.add_desires_btn.setText(_translate("Form", "Добавить"))
