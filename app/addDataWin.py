from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit, QMessageBox, QLabel

from database import SessionLocal
from services.services import ZovService

class AddDataWin(QWidget):
    def __init__(self, data=None):
        super().__init__()
        self.data = data
        self.db = SessionLocal()
        self.initUI()
        if data:
            self.upload_editable_data()
        self.show()

    def initUI(self):
        self.setWindowIcon(QIcon('resources/zov.ico'))
        self.setWindowTitle("Добавить новый товар")
        self.setGeometry(500, 200, 400, 200)

        self.name_label = QLabel("Имя товара:")
        self.name_input = QLineEdit()


        self.status_label = QLabel("Статус товара:")
        self.status_input = QLineEdit()


        self.add_button = QPushButton("Добавить товар")
        self.cls_1 = QPushButton("Выйти")

        self.add_button.clicked.connect(self.add_tovar)
        self.cls_1.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.status_label)
        layout.addWidget(self.status_input)

        layout.addWidget(self.add_button)
        layout.addWidget(self.cls_1)
        self.setLayout(layout)


    def upload_editable_data(self):
        self.tovar_id = int(self.data[0])
        self.name_input.setText(self.data[1])
        self.status_input.setText(self.data[2])


    def add_tovar(self):
        if self.data is None:
            ZovService(db=self.db).add_tovar(self.name_input.text(),
                                             self.status_input.text()
                                             )
            print(ZovService(db=self.db).get_all_tovars())
            QMessageBox.information(self, "Информация", "Товар добавлен успешно!")
            self.close()
        else:
            ZovService(db=self.db).update_data(self.tovar_id,
                                               self.name_input.text(),
                                               self.status_input.text()
                                               )

            QMessageBox.information(self, "Информация", "Товар изменен успешно!")
            self.close()
