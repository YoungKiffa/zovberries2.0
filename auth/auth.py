from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from app.mainWin import MainWindow

true_username = "gus"
true_password = "123"

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.resize(270, 100)
        self.setWindowIcon(QIcon('resources/zov.ico'))

        layout = QVBoxLayout()

        self.label_image = QLabel(self)
        pixmap = QPixmap("resources/zzz.jpg")
        self.label_image.setPixmap(pixmap)
        self.label_image.setScaledContents(True)
        self.label_image.setFixedSize(240, 100)
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_image, alignment=Qt.AlignmentFlag.AlignCenter)

        self.label_username = QLabel("Логин:")
        self.entry_username = QLineEdit()
        layout.addWidget(self.label_username)
        layout.addWidget(self.entry_username)

        self.label_password = QLabel("Пароль:")
        self.entry_password = QLineEdit()
        self.entry_password.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.label_password)
        layout.addWidget(self.entry_password)

        self.button_login = QPushButton("Войти")
        self.button_login.clicked.connect(self.login)
        self.button_quit = QPushButton("Выйти из системы")
        self.button_quit.clicked.connect(self.close)
        layout.addWidget(self.button_login)
        layout.addWidget(self.button_quit)

        self.setLayout(layout)

    def login(self):
        username = self.entry_username.text()
        password = self.entry_password.text()

        if username == true_username and password == true_password:
            QMessageBox.information(self, "Все верно", "Вход выполнен")
            self.open_main_window()
        else:
            QMessageBox.critical(self, "Ошибка", "Неверный логин или пароль.")

    def open_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

