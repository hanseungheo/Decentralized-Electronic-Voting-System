from PyQt5.QtWidgets import *
import sys


class GUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('제목')

        self.line_edit = QLineEdit()

        self.button = QPushButton('버튼')
        self.button.clicked.connect(self.button_click)

        self.text_label = QLabel()

        self.vbox_Layout = QVBoxLayout()
        self.vbox_Layout.addWidget(self.line_edit)
        self.vbox_Layout.addWidget(self.button)
        self.vbox_Layout.addWidget(self.text_label)

        self.setLayout(self.vbox_Layout)

    def button_click(self):
        self.text_label.setText(self.line_edit.text())

def exception_hook(except_type, value, traceback):
    print(except_type, value, traceback)
    exit(1)

if __name__ == '__main__':
    sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    gui = GUI()
    gui.show()
    sys.exit(app.exec())