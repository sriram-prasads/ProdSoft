# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 11:35:38 2021

@author: Sriram Prasad S
"""




from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QCalendarWidget


class Window(QDialog):
    
    
    def __init__(self):
        super().__init__()


        #window requrements like geometry,icon and title
        self.setGeometry(200,200,400,200)
        self.setWindowTitle("PyQt5 QCalendar")
        

        vbox = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
       
        
     

        vbox.addWidget(self.calendar)


        self.setLayout(vbox)

        

         
         
         

      