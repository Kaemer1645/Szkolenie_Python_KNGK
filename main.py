#1.Utworzenie projektu w Pycharm
#2.Utworzenie venv - automatycznie albo z cmd
#3.Instalacja bibliotek - pip install PyQt5 - pip install pyinstaller - sqlite3 jest juz zainstalowany
# -pip install qt-material
# pip install geopandas -- wheelz!!!!!
# pip install matplotlib - zeby plotowac w geopandas

#edycja key-map dla run oraz zmiana powershell na cmd
#stworzenie okienka UI
#alternatywy dla PyQt5 - Kivy, KivyMD, Tkinter i wiele wiele innych

#import bibliotek
from PyQt5 import uic #zaimportowana biblioteka do wczytywania plikow UI
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.Qt import pyqtSlot #zaimportowny dekorator
import matplotlib.pyplot as plt
import geopandas as gpd
cls, wnd = uic.loadUiType('okno.ui')
#cls i wnd jest to klasa oraz okno zapisane w dwoch zmiennych
#zapisanie w jednej zmiennej wyrzuci nam krotke w ktorej beda te dwie zmienne
#print(cls)

class Basic(wnd, cls):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    @pyqtSlot() #do metody clicked musimy uzyc dekoratora, zeby raz klikala
    #zdefiniowane sygnału
    def on_pbHello_clicked(self):
        print('Hello World')

    #wczytanie pliku
    @pyqtSlot() #tak samo jak wyzej, ale nie jest to w kazdej metodzie
    def on_pbLoad_clicked(self):
        load_file = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "Images (*.png *.xpm *.jpg)") #nazwa
        #sciezka, typ plikow
        print(load_file) # wyzej mozna dac load_file, _

    #zrobienie przycisku na dodawanie i wyswietlanie wyniku z dwoch okienek
    @pyqtSlot()
    def on_pbCalculate_clicked(self):
        a = self.leA.text()
        b = self.leB.text()
        c = float(a) + float(b)
        self.leResult.setText(str(c))


    def read_graph(self, shapefile):
        map = gpd.read_file(shapefile)
        print(map)
        #fig, ax = plt.subplots(figsize=(12, 10))
        #map.plot(ax=ax)
        map.plot()

    @pyqtSlot()
    def on_pbGraph_clicked(self):
        self.read_graph(r'D:\STUDIA\Kolo_naukowe\Szkolenie_PYTHON\Shapefiles\Województwa.shp')
        #zeby rysowalo D:\STUDIA\Programowanie\MGR_SEM_I\Jezyk_Python_Na_Potrzeby_Gis\aplikacja_5

    #wczytywanie pliku ze wspolrzednymi i wyswietlenie ich na
    #fancy map https://melaniesoek0120.medium.com/data-visualization-how-to-plot-a-map-with-geopandas-in-python-73b10dcd4b4b
    #https://geopandas.org/en/stable/docs/user_guide/mapping.html

#otwarcie aplikacji - utworzenie obiektu
app = QApplication([])
print(app)
#utworzenie obiektu naszej klasy
calc = Basic()
calc.show() #wywowalie funkcji show ktora jest dziedziczona z wnd
app.exec()
