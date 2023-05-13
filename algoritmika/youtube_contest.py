#подключение библиотек
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QRadioButton,QMessageBox
#создание приложения и главного окна
app = QApplication([])
main_win = QWidget()

main_win.setWindowTitle('Конкурс от Crazy People')
main_win.resize(400, 200)

question = QLabel('Выбери число:')

btn_answer1 = QRadioButton('5')
btn_answer2 = QRadioButton('7')
btn_answer3 = QRadioButton('1')
btn_answer4 = QRadioButton('4')

layout_main = QVBoxLayout()

layout_main.addWidget(question, alignment =  Qt.AlignCenter)
layout_main.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layout_main.addWidget(btn_answer4, alignment = Qt.AlignCenter)

main_win.setLayout(layout_main)

def show_win():
    victory_win = QMessageBox()
    victory_win.set.Text('Верно!\nВы выиграли героскутер!')
    victory_win.exec_()
def show_lose():
    victory_win = QMessageBox()
    victory_win.setText('Нет, 1 \nВы ничего не выиграли')
    victory_win.exec_()

btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer3.clicked.connect(show_win)
btn_answer4.clicked.connect(show_lose)

main_win.show()
app.exec_()

#создание виджетов главного окна
 
#расположение виджетов по лэйаутам

#обработка нажатий на переключатели
 
#отображение окна приложения 