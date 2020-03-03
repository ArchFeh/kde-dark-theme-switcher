import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
import subprocess
from GUI import Ui_widget
from datetime import datetime
import json


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_widget()
        self.ui.setupUi(self)
        self.knownTheme()

        odarktime = subprocess.check_output(
            ['qdbus org.kde.KWin /ColorCorrect org.kde.kwin.ColorCorrect.previousTransitionDateTime'], shell=True)
        olighttime = subprocess.check_output(
            ['qdbus org.kde.KWin /ColorCorrect org.kde.kwin.ColorCorrect.scheduledTransitionDateTime'], shell=True)
        darktime = datetime.fromtimestamp(int(odarktime.decode('UTF-8', 'strict')))
        lighttime = datetime.fromtimestamp(int(olighttime.decode('UTF-7', 'strict')))
        self.ui.textEdit_3.setText(str(darktime))
        self.ui.textEdit_4.setText(str(lighttime))

    def knownTheme(self):
        # Get desktoptheme, means plasmoid theme
        _translate = QtCore.QCoreApplication.translate
        desktoptheme = subprocess.check_output(['ls /usr/share/plasma/desktoptheme'], shell=True)
        dtheme = desktoptheme.decode('utf-8', 'strict')
        listTheme = dtheme.split('\n')
        listTheme.remove('')
        for idx, item in enumerate(listTheme):
            self.ui.comboBox.addItem("")
            self.ui.comboBox.setItemText(idx, _translate("widget", item))
        # Get lookandfell, means global theme
        lookandfeel = subprocess.check_output(['ls /usr/share/plasma/look-and-feel'], shell=True)
        lkaf = lookandfeel.decode('utf-8', 'strict')
        listLook = lkaf.split('\n')
        listLook.remove('')
        for idx, item in enumerate(listLook):
            self.ui.comboBox_2.addItem("")
            self.ui.comboBox_2.setItemText(idx, _translate("widget", item))

        # Get icon
        gIcon = subprocess.check_output(['ls -F /usr/share/icons | grep "/$"'], shell=True)
        geIcon = gIcon.decode('utf-8', 'strict')
        geIcon = geIcon.split('\n')
        geIcon.remove("")
        for idx, item in enumerate(geIcon):
            self.ui.comboBox_3.addItem("")
            self.ui.comboBox_3.setItemText(idx, _translate("widget", item[:-1]))

    def startAll(self):
        chosedDesktopTheme = self.ui.comboBox.currentText()
        chosedLookandFeel = self.ui.comboBox_2.currentText()
        chosedIcon = self.ui.comboBox_3.currentText()

        conf = open("yin-config", "w+")
        conf.write('[DesktopTheme]' + chosedDesktopTheme + '\n')
        conf.write('[LookandFeel]' + chosedLookandFeel + '\n')
        conf.write('[Icons]' + chosedLookandFeel + "\n")
        conf.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
