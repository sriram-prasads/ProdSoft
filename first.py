# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:38:58 2021

@author: Sriram Prasad S


"""

import sys
import MSt
import DatEntry

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QFont


class window():
    
   
    
    def __init__(self): 
        super().__init__()
            
        
        self.Window  = QWidget()
        self.Window.setGeometry(700,200,500,500)
        self.Window.setWindowTitle('Production software')

        layout = QVBoxLayout()
        
        
        button1 = QPushButton('Data Entry Services')
        button2 = QPushButton('Machine Setting Changes')
        self.button3 = QPushButton('Report Generation')
        
        button1.setFont(QFont('Times',13))
        button2.setFont(QFont('Times',13))
        self.button3.setFont(QFont('Times',13))
        
        
        button1.setMinimumHeight(75)
        button2.setMinimumHeight(75)
        self.button3.setMinimumHeight(75)
        

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(self.button3)
   
        
       
       
        self.Window.setLayout(layout)
       
        self.Window.show()
        
        
        button1.clicked.connect(self.showWin1)
        button2.clicked.connect(self.showWin2)
    
    def showWin2(self):
        self.w2 = MSt.MachSettings()
        self.w2.show()
        
    
    def showWin1(self):
        self.w1 = DatEntry.DataEntry()
        self.w1.show()
   
if __name__ == '__main__':
    app = QApplication(sys.argv)
    zx = window()
   
    
    app.exec()

        
      
        

   