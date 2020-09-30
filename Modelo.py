# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 12:56:57 2018

@author: john ochoa
"""
#%%
import numpy as np;
import pydicom as dicom;
import os;
class DICOM(object):
    def __init__(self):
        self.__dcm = None;
        self.__data = None;
        
        self.__slices = 0;
        self.__rows = 0;
        self.__columns = 0;
        
        self.__x_space = 0;
        self.__y_space = 0;
        self.__x_thickness = 0;
        
        self.__patient_name = '';
        self.__patient_id = '';
        self.__patient_sex = '';
        self.__patient_age = '';
        self.__study_description = '';
        self.__study_date = '';
        self.__study_id = '';
        self.__protocol_name = '';
    #%%    
    def loadDICOM(self, PathDicom):               
        lstFilesDCM = []  # create an empty list
        
        for dirName, subdirList, fileList in os.walk(PathDicom):
            for filename in fileList:
                # check whether the file's DICOM
                if ".dcm" in filename.lower():  
                    lstFilesDCM.append(os.path.join(dirName,filename))
        if len(lstFilesDCM) == 0:
            return False;        
        # Get ref file
        ref = dicom.read_file(lstFilesDCM[0])
        # Load dimensions based on the number of rows, columns, and slices (along the Z axis)
        self.__rows = int(ref.Rows);
        self.__columns = int(ref.Columns);
        self.__slices = len(lstFilesDCM);    
        # Load spacing values (in mm)
        self.__x_space = float(ref.PixelSpacing[0]);
        self.__y_space = float(ref.PixelSpacing[1]);
        self.__thickness = float(ref.SliceThickness);                
        self.__data = np.zeros((self.__rows, self.__columns, self.__slices), 
                               dtype=ref.pixel_array.dtype);
                               
        self.__patient_name = ref.PatientName;
        print(self.__patient_name);   
        self.__patient_id = ref.PatientID;
        print(self.__patient_id);
        self.__patient_sex = ref.PatientSex;
        print(self.__patient_sex);
        self.__patient_age = ref.PatientAge;
        print(self.__patient_age);
        self.__study_description = ref.StudyDescription;
        print(self.__study_description);
        self.__study_date = ref.StudyDate;
        print(self.__study_date);
        self.__study_id = ref.StudyID;
        print(self.__study_id);
        self.__protocol_name = ref.ProtocolName;
        print(self.__protocol_name);
        
                          
        # loop through all the DICOM files
        counter = 0
        for filenameDCM in lstFilesDCM:
            # read the file
            ds = dicom.read_file(filenameDCM)
            # store the raw image data
            self.__data[:, :, counter] = ds.pixel_array;
            counter = counter + 1;        
        return True;
    #%%  
    def returnPatientName(self):
        return self.__patient_name;
    
    def returnPatientID(self):
        return self.__patient_id;
    
    def returnPatientSex(self):
        return self.__patient_sex;
    
    def returnPatientAge(self):
        return self.__patient_age;
    
    def returnStudyDescription(self):
        return self.__study_description;
    
    def returnStudyDate(self):
        return self.__study_date;
    
    def returnStudyID(self):
        return self.__study_id;
    
    def returnProtocolName(self):
        return self.__protocol_name;
    
              
    def returnSliceAxial(self,position1):
#        print (position1)
        return self.__data[:,:,position1];
            
    def returnSliceCoronal(self,position2):
#        print (position2)
        return self.__data[position2,:,:];
    
    def returnSliceSagital(self,position3):
#        print (position3)
        return self.__data[:,position3,:];
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
