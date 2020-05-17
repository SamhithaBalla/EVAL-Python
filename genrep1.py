import sys
import os
#import xlsxwriter
from genrep import *
from reportlab import platypus
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.platypus import SimpleDocTemplate
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
     self.ui.pushButton_2.clicked.connect(self.pdformat)


  def pdformat(self):
    with con:
      items = []
      cur = con.cursor()
      qpaper = str(self.ui.lineEdit.text())
      with open(qpaper) as fp:
        for line in fp:
          words = line.split()
          for word in words:
            cur.execute('SELECT * from kywrds WHERE kywrd like ?',[word])
            result = cur.fetchall()
            if result:
              for row in result:
                result1 = row[0]
                result2 = row[1]
                result3 = row[2]
                address = 'Level: '+ str(result1) + ' '+ ' '+ ' '+ ' ' + 'Percentage: '+ str(result3) +'%' + '    '+ 'Keyword: ' + result2 
                items.append(platypus.Paragraph(address, PS('body')))
              doc = SimpleDocTemplate('report1.pdf')
              doc.multiBuild(items)


if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())