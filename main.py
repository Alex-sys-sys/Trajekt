import sys
from constructor import get_all_matching
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_file import Ui_MainWindow

"""Файл обрабатывающий приложение"""


class MyWidget(QMainWindow, Ui_MainWindow):  # Основное окно
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.generate)

    def generate(self):  # Функция действия кнопки
        if self.comboBox.currentText() == 'Неважно':
            res = get_all_matching(int(self.spinBox.text()), self.comboBox_2.currentText(),
                                   self.comboBox_3.currentText(), None)
        else:
            res = get_all_matching(int(self.spinBox.text()), self.comboBox_2.currentText(),
                                   self.comboBox_3.currentText(), self.comboBox.currentText())
        print(res)
        self.textEdit.setText('')
        if isinstance(res, list):
            for i in res:
                self.textEdit.append(str(i))  # Вывод результата функции отбора продуктов в UI
        else:
            self.textEdit.append(str(res))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
