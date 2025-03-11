from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QIcon, QPixmap

from app.viewDataWin import ViewDataWin


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ZOVberries')
        self.resize(300, 200)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('resources/zov.ico'))


        wid = QWidget()
        main_vl = QVBoxLayout()


        self.label_image = QLabel(self)
        pixmap = QPixmap("resources/main.jpg")
        self.label_image.setPixmap(pixmap)
        self.label_image.setScaledContents(True)
        self.label_image.setFixedSize(240, 100)
        self.label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.view_data_btn = QPushButton('Просмотреть товары')
        self.cls_btn = QPushButton('Выйти')

        main_vl.addWidget(self.label_image, alignment=Qt.AlignmentFlag.AlignCenter)
        main_vl.addStretch()
        main_vl.addWidget(self.view_data_btn)
        main_vl.addWidget(self.cls_btn)

        wid.setLayout(main_vl)
        self.setCentralWidget(wid)


        self.view_data_btn.clicked.connect(self.show_view_data_win)

        self.cls_btn.clicked.connect(self.close)

    def show_view_data_win(self):
        self.win_v = ViewDataWin()
        self.win_v.show()


    def closeEvent(self, event):
        QApplication.quit()
