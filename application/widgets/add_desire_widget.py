from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt

from .ui.create_desires_widget import Ui_Form
from application.dataBase.DataBase import DataBase


class DesireWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.setWindowTitle("Добавление желания") 
        self.__make_connects()
        self.db = DataBase()

    def closeEvent(self, event):
        self.parent.setWindowFlag(Qt.WindowCloseButtonHint, True)
        self.parent.show()

    def __make_connects(self):
        self.add_desires_btn.clicked.connect(self.get_data_form)

    def get_data_form(self):
        name = str(self.name_line.text())
        cost = self.cost_line.text()
        link = self.link_line.text()
        note = self.note_line.text()
        try:
            if name and link and note:
                float(cost)
                query = 'Insert into desire VALUES (default, ' \
                        f'\'{name}\', ' \
                        f'{cost}, ' \
                        f"\'{link}\', " \
                        f"\'{note}\');"
                self.db.connect_to_bd()
                self.db.query(query)
                self.db.commit()
                self.db.close()
                self.close()
                self.parent.add_desire()
                del self.db
            else:
                self.message_box('Не все поля заполнены')
        except ValueError:
            self.message_box('Стоимость назначается только числами')

    def message_box(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle('Ошибка')
        msg.setText(text)
        msg.addButton('Ок', QMessageBox.AcceptRole)
        msg.exec()
