# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 16:04:45 2019

@author: nwkeith
"""

from PyQt5 import QtGui, QtCore
import pyqtgraph as pg
app=QtGui.QApplication([])
w= QtGui.QWidget()
btn=QtGui.QPushButton('press me')
text=QtGui.QLineEdit('enter text')
listw = QtGui.QListWidget()
pg.setConfigOption('background','w')
plt=pg.PlotWidget()
penn=pg.mkPen('k', width=2, style=QtCore.Qt.SolidLine)
plt.plot([1,2,3],[1,2,3], pen=penn, title='The first pyqtgraph plot', symbol='t', symbolSize=20)
labelStyle={'color':'#100', 'font-size':'30px'}
plt.setLabel('bottom','Time','s',**labelStyle)
plt.setLabel('left','Voltage','V',**labelStyle)
plt.setYRange(0,5)
plt.setXRange(0,5)
layout=QtGui.QGridLayout()
w.setLayout(layout)
layout.addWidget(btn, 0,0)
layout.addWidget(text,1,0)
layout.addWidget(listw,2,0)
layout.addWidget(plt,0,1,3,1)
w.show()
app.exec_()

