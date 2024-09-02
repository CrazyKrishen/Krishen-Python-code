import sys
from PyQt5.QtWidgets import QApplication, QDialog, QCheckBox
from PyQt5.uic import loadUi

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        #uploading .ui file is loaded using the loadUi function
        self.ui=loadUi("drinks.ui",self)

        #when user selects a box
        self.ui.coke.stateChanged.connect(self.updateListView) #coke
        self.ui.sprite.stateChanged.connect(self.updateListView) #sprite
        self.ui.fanta.stateChanged.connect(self.updateListView) #fanta

    def updateListView(self):
        if self.ui.coke.isChecked():
            self.ui.listView.addItem("Coke")
            
        if self.ui.sprite.isChecked():
            self.ui.listView.addItem("Sprite")
            
        if self.ui.fanta.isChecked():
            self.ui.listView.addItem("Fanta")


if __name__=="__main__":
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.exec_()
    sys.exit(app.exec_())
