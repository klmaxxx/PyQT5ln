from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
QApplication,
QHBoxLayout,
QMessageBox,
QRadioButton,
QVBoxLayout,
QWidget,
)


def show_win():
    victory_win = QMessageBox( )
    victory_win.setText("BipHo!\nBu Burpanu ripocKkyTep")
    victory_win.exec_()



def show_lose():
    victory_win = QMessageBox( )
    victory_win.setText("Hi, 2015 poky\nBu Burpanu dipmoBui nnakat" )
    victory_win.exec_()



app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle("KonKypc Big Crazy People")
main_win.resize(400, 200)


question = QLabel("Akoro poky KaHan OTpymMaB «30nOTy KHONKy» Big YouTube?" )
btn_answer1 = QRadioButton( "2005" )
btn_answer2 = QRadioButton("2010" )
btn_answer3 = QRadioButton("2015")
btn_answer4 = QRadioButton( "2020" )


layout_main = QVBoxLayout()

LayoutH1 = QHBoxLayout()

layoutH2 = QHBoxLayout()

LayoutH3 = QHBoxLayout()

LayoutH1.addWidget(question, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment=Qt.AlignCenter)
LayoutH3.addWidget(btn_answer3, alignment=Qt.AlignCenter)
LayoutH3.addWidget(btn_answer4, alignment=Qt.AlignCenter)

layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
main_win.setLayout(layout_main)


btn_answer3.clicked.connect(show_win)

btn_answer1.clicked.connect(show_lose)
btn_answer2.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)


main_win.show()