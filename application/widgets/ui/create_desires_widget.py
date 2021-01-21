# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_desires_widget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(473, 209)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(5, -1, 5, -1)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 5, -1, 0)
        self.verticalLayout_2.setSpacing(17)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.name_line = QtWidgets.QLineEdit(Form)
        self.name_line.setObjectName("name_line")
        self.verticalLayout_2.addWidget(self.name_line)
        self.cost_line = QtWidgets.QLineEdit(Form)
        self.cost_line.setObjectName("cost_line")
        self.verticalLayout_2.addWidget(self.cost_line)
        self.link_line = QtWidgets.QLineEdit(Form)
        self.link_line.setObjectName("link_line")
        self.verticalLayout_2.addWidget(self.link_line)
        self.note_line = QtWidgets.QLineEdit(Form)
        self.note_line.setObjectName("note_line")
        self.verticalLayout_2.addWidget(self.note_line)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.add_desires_btn = QtWidgets.QPushButton(Form)
        self.add_desires_btn.setObjectName("add_desires_btn")
        self.verticalLayout_3.addWidget(self.add_desires_btn)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Название"))
        self.label_2.setText(_translate("Form", "Цена"))
        self.label_3.setText(_translate("Form", "Ссылка"))
        self.label_4.setText(_translate("Form", "Примечание"))
        self.add_desires_btn.setText(_translate("Form", "Добавить"))
