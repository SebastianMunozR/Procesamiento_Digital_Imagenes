#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 10:37:41 2018

@author: john ochoa
"""
from Modelo import DICOM
from Vista import InterfazGrafico
import sys
from PyQt5.QtWidgets import QApplication
#%% INICIALIZACION CLASES
class Principal(object):
    def __init__(self):        
        self.__app = QApplication(sys.argv);
        
        self.__mi_vista = InterfazGrafico();
        self.__mi_dicom = DICOM()
        
        self.__mi_controlador=Coordinador(self.__mi_vista,self.__mi_dicom)
        self.__mi_vista.asignar_Controlador(self.__mi_controlador)
    
    def main(self):
        self.__mi_vista.show()
        sys.exit(self.__app.exec_())

#%% ENLACE ENTRE CLASES    
class Coordinador(object):
    def __init__(self, vista, dicom):
        self.__mi_vista = vista;
        self.__mi_dicom = dicom;
        
    def recibirCarpetaDICOM(self, path):
        return self.__mi_dicom.loadDICOM(path);
    
    def returnSliceAxial(self,position1):
        return self.__mi_dicom.returnSliceAxial(position1);
    
    def returnSliceSagital(self,position3):
        return self.__mi_dicom.returnSliceSagital(position3);    
    
    def returnSliceCoronal(self,position2):
        return self.__mi_dicom.returnSliceCoronal(position2);
    
    def returnPatientName(self):
        return self.__mi_dicom.returnPatientName();
    
    def returnPatientID(self):
        return self.__mi_dicom.returnPatientID();
    
    def returnPatientSex(self):
        return self.__mi_dicom.returnPatientSex();
    
    def returnPatientAge(self):
        return self.__mi_dicom.returnPatientAge();
    
    def returnStudyDescription(self):
        return self.__mi_dicom.returnStudyDescription();
    
    def returnStudyDate(self):
        return self.__mi_dicom.returnStudyDate();
    
    def returnProtocolName(self):
        return self.__mi_dicom.returnProtocolName();
    
    def returnStudyID(self):
        return self.__mi_dicom.returnStudyID();
    
    
    
    
    
    
    
    
    
p=Principal()
p.main()