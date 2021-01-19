import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("test1.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.pushButtonA.clicked.connect(self.buttonAFunction)
        self.pushButtonB.clicked.connect(self.buttonBFunction)
        self.radioButtonA.clicked.connect(self.groupboxRadFunction)
        self.radioButtonB.clicked.connect(self.groupboxRadFunction)


        self.changeTextCounter = 0
        self.changeLabelButton.clicked.connect(self.changeTextFunction)
        self.printLabelButton.clicked.connect(self.printTextFunction)
        

    def buttonAFunction(self):
        if self.checkBoxA.isChecked() : print("check A")
        if self.checkBoxB.isChecked() : print("check B")
        print("buttonA pushed")
    
    def buttonBFunction(self):
        print("buttonB pushed")

    def groupboxRadFunction(self):
        if self.radioButtonA.isChecked() : print("A")
        elif self.radioButtonB.isChecked() : print("B")


    def changeTextFunction(self):
        self.changeTextCounter += 1
        if self.changeTextCounter % 2:
            self.labelA.setText("changed")
        else : self.labelA.setText("Changable text")


    def printTextFunction(self):
        print(self.labelA.text())

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()