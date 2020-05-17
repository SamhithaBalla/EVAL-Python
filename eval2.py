import sys
import os 
import sqlite3
from qpaper import *
from PyQt5 import QtWidgets, QtGui, QtCore
con = sqlite3.connect('atbt1')


class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.checkfile)


  def checkfile(self):        
    fname = str(self.ui.lineEdit.text())
    with con:
      cur = con.cursor()
      with open(str(self.ui.lineEdit.text())) as fp:
        for line in fp:
          words = line.split()
          for word in words:
            cur.execute('SELECT * from kywrds WHERE kywrd like ?',[word])
            result = cur.fetchall()
            if result:
              print(line,result)


if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())