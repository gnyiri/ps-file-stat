import sys

from PyQt4.QtGui import *
from ui.main_window import *


def main():
    l_app = QApplication(sys.argv)

    l_main_window = PsFileMainWindow()
    l_main_window.show()
    l_app.exec_()


if __name__ == '__main__':
    main()