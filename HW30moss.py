# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 16:47:04 2019

@author: Nathan Keith
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import serial
#from PyQt5 import QtGui, QtCore
import sys
import numpy as np
import pyqtgraph
ser=serial.Serial('COM5', 9600)

class ExampleApp(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        pyqtgraph.setConfigOption('background', 'w')
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName('MainWindow')
        MainWindow.resize(900,900)
        self.centralwidget=QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(200,200,500,500))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        
    def update(self):
        points=100
        X=np.arange(points)
        n=0
        dataLst=[]
        while n<100:
            dataPoint=ser.readline()
            dataPoint=float(dataPoint)
            dataLst.append(dataPoint)
            n+=1
        Y=dataLst
        penn=pyqtgraph.mkPen('k', width=3, style=QtCore.Qt.SolidLine)
        self.graphicsView.setYRange(0,1200,padding=0)
        labelStyle={'color':'#000','font-size':'20px'}
        self.graphicsView.setLabel('bottom','Number of Points','',**labelStyle)
        self.graphicsView.setLabel('left','Voltage','',**labelStyle)
        self.graphicsView.plot(X,Y,pen=penn, clear=True)
        QtCore.QTimer.singleShot(1, self.update)
        
app =QtGui.QApplication(sys.argv)
form=ExampleApp()
form.show()
form.update()
app.exec_()
            