from __future__ import division
import sys
from radiobtn import *
class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.ComputeButton, QtCore.SIGNAL('clicked()'),self.calculate)
        self.ui.radioAdd.setChecked(1)

    def calculate(self):
        if len(self.ui.lineFirstNumber.text())!=0:
            a=int(self.ui.lineFirstNumber.text())
        else:
            a=0
            if len(self.ui.lineSecondNumber.text())!=0:
                b=int(self.ui.lineSecondNumber.text())
            else:
                b=0
                if self.ui.radioAdd.isChecked()==True:
                    result=a+b
                if self.ui.radioSubtract.isChecked()==True:
                    result=a-b
                if self.ui.radioMultiply.isChecked()==True:
                    result=a*b
                if self.ui.radioDivide.isChecked()==True:
                    result=a/b

                    
                self.ui.labelResult.setText("Result: " +str(result))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())
