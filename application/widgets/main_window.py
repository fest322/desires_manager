import sys
from PyQt5 import QtWidgets
from .ui.desires_widget import Ui_Form
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QStandardItemModel,
    QStandardItem,
)
from PyQt5.QtWidgets import (
    QHeaderView,
    QAbstractItemView,
    QMessageBox,
    QTableView,
)

from .add_desire_widget import DesireWindow
from application.dataBase.DataBase import DataBase


class MainWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.index_row = {}
        self.parent = parent
        self.add_desire_widget = None
        self.setWindowFlag(Qt.WindowCloseButtonHint, True)
        self.show()
        self.__create_table()
        self.__make_connects()
        self.show_desire()

    def __make_connects(self):
        self.add_desires_btn.clicked.connect(self.add_desires_window)
        self.del_desires_btn.clicked.connect(self.delete_desire)
        self.model_desire.itemChanged.connect(self.changed_item)

    def __create_table(self):
        self.model_desire = QStandardItemModel()
        self.model_desire.setHorizontalHeaderLabels(['Название', 'Стоимость', 'Ссылка', 'Прочее'])
        self.table_initialization(self.table_desire, self.model_desire)

    def table_initialization(self, table: QTableView, model: QStandardItemModel):
        table.verticalHeader().hide()
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        table.setModel(model)
        table.setSelectionBehavior(QAbstractItemView.SelectRows)

    def add_desires_window(self):
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)
        self.show()
        self.add_desire_widget = DesireWindow(self)
        self.add_desire_widget.show()

    def add_desire(self):
        db = DataBase()
        db.connect_to_bd()
        query = 'Select * from desire;'
        desire = db.query(query)[-1]
        db.close()
        number_row = self.model_desire.rowCount()
        self.model_desire.appendRow([QStandardItem(desire['name']),
                                     QStandardItem(str(desire['cost'])),
                                     QStandardItem(desire['link']),
                                     QStandardItem(desire['note'])])
        self.index_row[number_row] = desire['id_desire']

    def show_desire(self):
        db = DataBase()
        db.connect_to_bd()
        query = 'Select * from desire;'
        desires = db.query(query)
        db.close()
        for desire in desires:
            number_row = self.model_desire.rowCount()
            self.model_desire.appendRow([QStandardItem(desire['name']),
                                         QStandardItem(str(desire['cost'])),
                                         QStandardItem(desire['link']),
                                         QStandardItem(desire['note'])])
            self.index_row[number_row] = desire['id_desire']

    def delete_desire(self):
        rows = self.table_desire.selectionModel().selectedRows()
        if rows:
            index = rows[0].row()
            self.model_desire.removeRow(index)
            query = f'Delete from desire where id_desire = {self.index_row[index]}'
            if index in self.index_row:
                del self.index_row[index]
            db = DataBase()
            db.connect_to_bd()
            db.query(query)
            db.commit()
            db.close()

    def changed_item(self, item: QStandardItem):
        index_row = item.row()
        id_desire = self.index_row[index_row]
        name = self.model_desire.index(index_row, 0).data()
        cost = self.model_desire.index(index_row, 1).data()
        link = self.model_desire.index(index_row, 2).data()
        note = self.model_desire.index(index_row, 3).data()
        try:
            float(cost)
            if name and link and note:
                query = f"Update desire set name = \'{name}\', cost = {cost}, link = \'{link}\', note = \'{note}\' " \
                        f"where id_desire = {id_desire}"
                db = DataBase()
                db.connect_to_bd()
                db.query(query)
                db.commit()
                db.close()
            else:
                self.message_box('Не все поля заполнены')
                self.model_desire.clear()
                self.__create_table()
                self.show_desire()
        except ValueError:
            self.message_box('Данные заполнены не корректно')
            self.model_desire.clear()
            self.__create_table()
            self.show_desire()

    def message_box(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle('Ошибка')
        msg.setText(text)
        msg.addButton('Ок', QMessageBox.AcceptRole)
        msg.exec()


def show_window():
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    sys.exit(app.exec_())
