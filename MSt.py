# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 18:05:56 2021

@author: Sriram Prasad S
"""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit





class MachSettings(QWidget):
    def __init__(self):
        super().__init__()
      
        
        self.setGeometry(900,400,500,500)
        self.setWindowTitle('Machine Settings')
        layout1 = QFormLayout()


        self.cou = QLineEdit()
        self.tp = QLineEdit()
        self.sps = QLineEdit()
        self.mpm = QLineEdit()



        laylb1 = QLabel('Count: ')
        laylb1.setFont(QFont('Times',10))
        layout1.addRow(laylb1, self.cou)


        laylb2 = QLabel('TPI: ')
        laylb2.setFont(QFont('Times',10))
        layout1.addRow(laylb2, self.tp)


        laylb3 = QLabel('Spindle Speed: ')
        laylb3.setFont(QFont('Times',10))
        layout1.addRow(laylb3, self.sps)

        laylb4 = QLabel('MPM: ')
        laylb4.setFont(QFont('Times',10))
        layout1.addRow(laylb4, self.mpm)

        self.initialSet()

        button3 = QPushButton('Clear')
        button1 = QPushButton('Calculate')
        button2 = QPushButton('SAVE')

        button1.setFont(QFont('Times',10))
        button2.setFont(QFont('Times',10))
        button3.setFont(QFont('Times',10))

        
        layout1.addWidget(button1)
        layout1.addWidget(button2)
        layout1.addWidget(button3)



        button1.clicked.connect(self.Onprez)
        button2.clicked.connect(self.Onprez1)
        button3.clicked.connect(self.clearSet)


        self.setLayout(layout1)


              
       
    
    def Onprez(self):
    
        tps = self.tp.text()
        sp = self.sps.text()
    
    
        self.mpx = (float(sp)/(float(tps) * 39.37)) * 2
        self.mpx = float("{:.2f}".format(self.mpx))
        self.mpz = str(self.mpx)
        self.mpm.setText(self.mpz)
        
        
        
    def Onprez1(self):
        fo = open("mset.txt","w")
        
       
        fo.write(self.cou.text()+'\n')
        fo.write(self.tp.text()+'\n')
        fo.write(self.sps.text()+'\n')
        fo.write(self.mpm.text()+'\n')
    
        fo.close()
        self.close()
        
        
    def initialSet(self):
        fo = open("mset.txt","r")
        a1 = fo.readline()
        a2 = fo.readline()
        a3 = fo.readline()
        a4 = fo.readline()
        self.cou.setText(a1)
        self.tp.setText(a2)
        self.sps.setText(a3)
        self.mpm.setText(a4)
        fo.close()
        
    def clearSet(self):
        fo = open("mset.txt","w").close()
        self.initialSet()
        
