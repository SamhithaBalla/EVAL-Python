import sys
import os
from atbt import *
from PyQt5 import QtWidgets, QtGui, QtCore


class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.storelevels)
     self.ui.pushButton_2.clicked.connect(self.storekywrds)
     self.ui.pushButton_3.clicked.connect(self.acceptqp)
     #self.ui.pushButton_4.clicked.connect(self.evaluateqp)
     self.ui.pushButton_6.clicked.connect(self.genreprt)


  def storelevels(self):
    os.system("python levels1.py")


  def storekywrds(self):
    os.system("python kywrds1.py")


  def acceptqp(self):
    os.system("python eval2.py")


  #def evaluateqp(self):
    #os.system("python eval1.py")


  def genreprt(self):
    os.system("python genrep1.py")


#  def gensugg(self):
#        os.system("python gensug1.py")
         
if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())