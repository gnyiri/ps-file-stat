import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class PsFileMainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(PsFileMainWindow, self).__init__(parent)

        self.m_log_list_widget = QListWidget()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(400, 400)
        self.setWindowTitle("PsFile")

        exitAction = QAction(QIcon('quit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QApplication.quit)

        l_menubar = self.menuBar()
        l_file_menu = l_menubar.addMenu('&File')
        l_file_menu.addAction(exitAction)

        log_dock_widget = QDockWidget("Log", self)
        log_dock_widget.setObjectName("log_dock_widget")
        log_dock_widget.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        log_dock_widget.setWidget(self.m_log_list_widget)

        self.addDockWidget(Qt.RightDockWidgetArea, log_dock_widget)

        self.statusBar().showMessage("Ready")
        self.show()

    def closeEvent(self, p_event):
        l_reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if l_reply == QMessageBox.Yes:
            p_event.accept()
        else:
            p_event.ignore()



