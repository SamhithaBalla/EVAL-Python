import sys
from levels import *
from PyQt5 import QtWidgets, QtGui, QtCore


#import MySQLdb as mdb
#con = mdb.connect('localhost', 'team1', 'test623', 'atbt1'); 



import sqlite3
con = sqlite3.connect('atbt1')


class MyForm(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
     QtWidgets.QWidget.__init__(self,parent)
     self.ui = Ui_MainWindow()
     self.ui.setupUi(self)
     self.ui.pushButton.clicked.connect(self.insertvalues)


  def insertvalues(self):
    with con:
      cur = con.cursor()
      lid = str(self.ui.lineEdit_3.text())
      ldesc = str(self.ui.lineEdit_4.text())
      cur.execute('INSERT INTO levels VALUES(?,?)',(lid,ldesc))
      con.commit()
        


if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())