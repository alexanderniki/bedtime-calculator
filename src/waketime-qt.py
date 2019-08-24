import sys

# Waketime calculator:
from waketime_calc import SleepTimeCalculator

# PyQt:
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QPushButton, QToolTip, QMessageBox, QDesktopWidget, QLabel, QLineEdit, QTextEdit


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setGeometry(350, 350, 350, 220)
        self.setWindowTitle('Bedtime calculator') # Show window title
        self.setWindowIcon(QIcon('ic_application.png')) # Show window icon
        self.statusBar().showMessage('Ready')

        self.timewidget = WakeUpTimeWidget()
        self.setCentralWidget(self.timewidget)

        # self.setStyleSheet("QWidget { background-color: #f0f0f0 }") # Set background color

        self.center()
        self.show()

    def center(self):
        # A rectangle specifying the geometry of the main window.
        # This includes any window frame.
        qr = self.frameGeometry()
        # We figure out the screen resolution of our monitor.
        # And from this resolution, we get the center point.
        cp = QDesktopWidget().availableGeometry().center()
        # Our rectangle has already its width and height.
        # Now we set the center of the rectangle to the center of the screen.
        # The rectangle's size is unchanged.
        qr.moveCenter(cp)
        # We move the top-left point of the application window to the top-left
        # point of the qr rectangle, thus centering the window on our screen.
        self.move(qr.topLeft())

class WakeUpTimeWidget(QWidget):
    
    def __init__(self):
        self.calculator = SleepTimeCalculator()
        super().__init__()
        self.initUI()

    def initUI(self):
    
        # Window:
        self.createHeaderLabel()
        self.createLabel()
        self.createTimeBoxes()
        
        self.show()

    def createHeaderLabel(self):
        self.message_box = QLabel("Ubuntu", self)
        self.message_box.setText('Bedtime calculator')
        self.message_box.adjustSize()

    def createLabel(self):
        self.message_box = QLabel("Ubuntu", self)
        self.message_box.setText('If I go to bed right now, I should wake up at:')
        self.message_box.adjustSize()
        
    
    def createTimeBoxes_1(self): # It works somehow

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(okButton)
        vbox.addWidget(cancelButton)

        self.setLayout(vbox)
        self.show()


    def createTimeBoxes(self):

        wakeupTimes = self.calculator.calculateWakeupTimes(self.calculator.getCurrentTime())
        theTime = []

        for counter in range(0, len(wakeupTimes), 1):
            theTime.append(wakeupTimes[counter])
            print(wakeupTimes[counter])

        for counter in range(0, len(wakeupTimes), 1):
            theTime[counter] = QLabel("Ubuntu", self)
            theTime[counter].setText(str(wakeupTimes[counter]))
            # self.vbox.addWidget(oneTime[counter])

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        for counter in range(0, len(wakeupTimes), 1):
            vbox.addWidget(theTime[counter])
        self.setLayout(vbox)
        self.show()

    def createTimeList(self):
        self.time_list = QLabel("Ubuntu", self)
        timesText = self.calculator.calculateWakeupTimes(self.calculator.getCurrentTime())
        self.time_list.setText(str(timesText[0]) + "\n" + str(timesText[1]) + "\n" + str(timesText[2]) + "\n" + str(timesText[3]) + "\n" + str(timesText[4]) + "\n" + str(timesText[5]))
        self.time_list.adjustSize()

# ---------- New classes ----------

class CentralWidget (QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout() # Place all the widgets here
        self.vbox.addWidget(AppHeader)
        self.vbox.addWidget(WakeupWidget)
        self.vbox.addWidget(GotoBedNow)

class AppHeader:
    def __init__(self):
        self.app_header = QLabel("Ubuntu", self)
        self.app_header.setText("Bedtime calculator")
        self.app_header.adjustSize()

class WakeupWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()

class GotoBedNow(QWidget):
    def __init__(self):
        super().__init__()
        # self.createTimeList()
        self.createTimeBoxes()

    # def createTimeList(self):
    #     self.time_list = QLabel("Ubuntu", self)
    #     timesText = self.calculator.calculateWakeupTimes(self.calculator.getCurrentTime())
    #     self.time_list.setText(str(timesText[0]) + "\n" + str(timesText[1]) + "\n" + str(timesText[2]) + "\n" + str(timesText[3]) + "\n" + str(timesText[4]) + "\n" + str(timesText[5]))
    #     self.time_list.adjustSize()

    def createTimeBoxes(self):

        wakeupTimes = self.calculator.calculateWakeupTimes(self.calculator.getCurrentTime())
        theTime = []

        for counter in range(0, len(wakeupTimes), 1):
            theTime.append(wakeupTimes[counter])
            print(wakeupTimes[counter])

        for counter in range(0, len(wakeupTimes), 1):
            theTime[counter] = QLabel("Ubuntu", self)
            theTime[counter].setText(str(wakeupTimes[counter]))

        vbox = QVBoxLayout()
        vbox.addStretch(1)

        for counter in range(0, len(wakeupTimes), 1):
            vbox.addWidget(theTime[counter])

        self.setLayout(vbox)
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())        
        
if __name__ == '__main__':
    main()
