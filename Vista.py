#%% Librerias
from Modelo import DICOM
#Qfiledialog es una ventana para abrir y guardar archivos
#Qvbox es un organizador de widget en la ventana, este en particular los apila en vertical
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFileDialog
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
#contenido para graficos de matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# clase con el lienzo (canvas=lienzo) para mostrar en la interfaz los graficos matplotlib, el canvas mete la grafica dentro de la interfaz
class MyGraphCanvas(FigureCanvas):
    #constructor
    def __init__(self, parent= None,width=10, height=8, dpi=300):
        
        #se crea un objeto figura
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        #el axes en donde va a estar mi grafico debe estar en mi figura
        self.axial = self.fig.add_subplot(131)
        self.coronal = self.fig.add_subplot(132)
        self.sagital = self.fig.add_subplot(133)
        
        #se inicializa la clase FigureCanvas con el objeto fig
        FigureCanvas.__init__(self,self.fig)
        
    #hay que crear un metodo para graficar un corte
    def graficar_axial(self,datos):
        #primero se necesita limpiar la grafica anterior
        self.axial.clear();
        #ingresamos los datos a graficar
        self.axial.imshow(datos,cmap='gray');
        #ordenamos que dibuje
        self.axial.figure.canvas.draw();
    def graficar_coronal(self,datos):
        #primero se necesita limpiar la grafica anterior
        self.coronal.clear();
        #ingresamos los datos a graficar
        self.coronal.imshow(datos,cmap='gray');
        #ordenamos que dibuje
        self.coronal.figure.canvas.draw();
    def graficar_sagital(self,datos):
        #primero se necesita limpiar la grafica anterior
        self.sagital.clear();
        #ingresamos los datos a graficar
        self.sagital.imshow(datos,cmap='gray');
        #ordenamos que dibuje
        self.sagital.figure.canvas.draw();
#%%
class InterfazGrafico(QMainWindow):
    #condtructor
    def __init__(self):
        #siempre va
        super(InterfazGrafico,self).__init__()
        #se carga el diseno
        loadUi ('anadir_grafico.ui',self)
        #se llama la rutina donde configuramos la interfaz
        self.setup()
        #se muestra la interfaz
        self.show()
        #voy a crear un atributo que sea el indice
        self.__indice = 0;
    
    def setup(self):
        #los layout permiten organizar widgets en un contenedor
        #esta clase permite añadir widget uno encima del otro (vertical)
        layout = QVBoxLayout()
        #se añade el organizador al campo grafico
        self.campo_grafico.setLayout(layout)
        #se crea un objeto para manejo de graficos
        self.__sc = MyGraphCanvas(self.campo_grafico, width=6, height=5, dpi=100)
        #se añade el campo de graficos
        layout.addWidget(self.__sc)
        #se organizan las senales 
        self.boton_cargar.clicked.connect(self.cargar_dicom);
#        self.boton_atras.clicked.connect(self.atras);
        self.SliderAxial.valueChanged.connect(self.slider_axial);
        self.SliderCoronal.valueChanged.connect(self.slider_coronal);
        self.SliderSagital.valueChanged.connect(self.slider_sagital);
        
    def asignar_Controlador(self,controlador):
        self.__coordinador=controlador

    def slider_axial (self):
        self.__valsa = self.SliderAxial.value()
        self.__sc.graficar_axial(
                self.__coordinador.returnSliceAxial(self.__valsa));
                
    def slider_coronal (self):
        self.__valsc = self.SliderCoronal.value()
        self.__sc.graficar_coronal(
                self.__coordinador.returnSliceCoronal(self.__valsc));
    
    def slider_sagital (self):
        self.__valss = self.SliderSagital.value()
        self.__sc.graficar_sagital(
                self.__coordinador.returnSliceSagital(self.__valss));
 
    
#    def atras(self):
#        #disminuyo el indice
#        self.__indice = self.__indice - 1;
#        #le digo al controlador que le diga al modelo que me devuelva
#        #el corte en esa posicion
#        self.__sc.graficar_axial(
#                self.__coordinador.returnSliceAxial(self.__indice));
#        self.__sc.graficar_coronal(
#                self.__coordinador.returnSliceCoronal(self.__indice));
#        self.__sc.graficar_sagital(
#                self.__coordinador.returnSliceSagital(self.__indice));
    
    def cargar_dicom(self):
        #se abre el cuadro de dialogo para cargar un directorio
        directorio = QFileDialog.getExistingDirectory(
                self,
                "Seleccione un directorio",
                ".",
                QFileDialog.ShowDirsOnly);
        if directorio != "":
            print(directorio)
            
            resultado = self.__coordinador.recibirCarpetaDICOM(directorio);
            if resultado == True:
                #actualizo el indice
                self.__indice = 0;
                self.__sc.graficar_axial(
                        self.__coordinador.returnSliceAxial(self.__indice));
                self.__sc.graficar_coronal(
                        self.__coordinador.returnSliceCoronal(self.__indice));
                self.__sc.graficar_sagital(
                        self.__coordinador.returnSliceSagital(self.__indice));
                self.name.setText(
                        str(self.__coordinador.returnPatientName()));
                self.id.setText(
                        str(self.__coordinador.returnPatientID()));
                self.sex.setText(
                        str(self.__coordinador.returnPatientSex()));
                self.age.setText(
                        str(self.__coordinador.returnPatientAge()));
                self.study.setText(
                        str(self.__coordinador.returnStudyDescription()));
                self.date.setText(
                        str(self.__coordinador.returnStudyDate()));        
                self.idstudy.setText(
                        str(self.__coordinador.returnStudyID()));
                self.protocol.setText(
                        str(self.__coordinador.returnProtocolName()));
        
        
        
        
        