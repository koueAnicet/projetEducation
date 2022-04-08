from Widget.interface import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys



def main():
    
    app = QApplication(sys.argv)
    home = Ui_MainWindow()
    home.show()
    app.exec_()

if __name__ == '__main__':
    main()