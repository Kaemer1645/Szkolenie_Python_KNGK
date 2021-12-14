#1.Utworzenie projektu w Pycharm
#2.Utworzenie venv - automatycznie albo z cmd
#3.Instalacja bibliotek - pip install PyQt5 - pip install pyinstaller - sqlite3 jest juz zainstalowany
# -pip install qt-material
# pip install geopandas -- wheelz!!!!!
# pip install matplotlib - zeby plotowac w geopandas

#edycja key-map dla run oraz zmiana powershell na cmd file/setting/tools/terminal
#stworzenie okienka UI
#alternatywy dla PyQt5 - Kivy, KivyMD, Tkinter i wiele wiele innych

#import bibliotek
from PyQt5 import uic #zaimportowana biblioteka do wczytywania plikow UI
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.Qt import pyqtSlot #zaimportowny dekorator
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

cls, wnd = uic.loadUiType('okno.ui')
#cls i wnd jest to klasa oraz okno zapisane w dwoch zmiennych
#zapisanie w jednej zmiennej wyrzuci nam krotke w ktorej beda te dwie zmienne
#print(cls)

class Basic(wnd, cls):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.graph_window.hide()  # schowanie widgetu

    # PUNKT 1 hello world
    @pyqtSlot() #do metody clicked musimy uzyc dekoratora, zeby raz klikala
    #zdefiniowane sygnału
    def on_pbHello_clicked(self):
        print('Hello World')

    # PUNKT 2 wczytanie pliku
    @pyqtSlot() #tak samo jak wyzej, ale nie jest to w kazdej metodzie
    def on_pbLoad_clicked(self):
        load_file = QFileDialog.getOpenFileName(self, "Wybierz plik", "", "Images (*.png *.xpm *.jpg)") #nazwa
        #sciezka, typ plikow
        print(load_file) # wyzej mozna dac load_file, _

    # PUNKT 3 zrobienie przycisku na dodawanie i wyswietlanie wyniku z dwoch okienek
    @pyqtSlot()
    def on_pbCalculate_clicked(self):
        a = self.leA.text()
        b = self.leB.text()
        c = float(a) + float(b)
        self.leResult.setText(str(c))

    # PUNKT 4 generowanie mapy z wgraniem punktow csv
    @pyqtSlot()
    def on_pbShp_clicked(self):
        """wczytanie sciezki pliku shape"""
        filename, extension = QFileDialog.getOpenFileName(self, "Wybierz plik shapefile", "", "Shapefile (*.shp)")
        self.shp_path = filename

    def read_shapefile(self, shp_path):
        """wczytywanie pliku shape"""
        if shp_path != '':
            shapefile = gpd.read_file(shp_path)
        return shapefile

    @pyqtSlot()
    def on_pbGraph_clicked(self):
        """stworzenie wykresu w oparciu o shapefile"""
        self.shapefile = self.read_shapefile(shp_path=self.shp_path)
        #print(self.shapefile.columns)
        self.graph_window.read_graph(self.shapefile)  # odwolanie sie do widgetu!
        self.graph_window.show()
        self.crs = self.shapefile.crs  # pobranie ukladu wspolrzednych
        self.leCrs.setText(str(self.crs.name))

    @pyqtSlot()
    def on_pbCsv_clicked(self):
        """wczytanie sciezki pliku csv"""
        filename, extension = QFileDialog.getOpenFileName(self, "Wybierz plik csv", "", "csv (*.csv)")
        self.csv_path = filename

    def add_points(self, path):
        """dodanie punktow z csv do wykresu"""
        df = pd.read_csv(path, sep=' ')
        geometry = [Point(xy) for xy in zip(df.iloc[:, 0], df.iloc[:, 1])]
        gdf = gpd.GeoDataFrame(df, geometry=geometry, crs=self.crs)
        colours = ['#00ff00']*len(geometry)  # nadanie koloru dla kazdego punktu
        gdf['colour'] = colours
        #gdf = gdf.to_crs(self.crs)
        return gdf

    @pyqtSlot()
    def on_pbShowPoints_clicked(self):
        """wyswietlenie punktow z csv na wykresie"""
        points = self.add_points(path=self.csv_path)
        self.graph_window.read_graph(self.shapefile, add_points=points)

    @pyqtSlot()
    def on_pbClear_clicked(self):
        self.graph_window.clear_graph()
        self.leCrs.clear()  # wyczyszczenie line edit z ukladem wsp

    #wczytywanie pliku ze wspolrzednymi i wyswietlenie ich na
    #fancy map https://melaniesoek0120.medium.com/data-visualization-how-to-plot-a-map-with-geopandas-in-python-73b10dcd4b4b
    #https://geopandas.org/en/stable/docs/user_guide/mapping.html

    # PUNKT 5 wygenerowanie .exe
#otwarcie aplikacji - utworzenie obiektu
app = QApplication([])
#utworzenie obiektu naszej klasy
calc = Basic()
calc.show() #wywowalie funkcji show ktora jest dziedziczona z wnd
app.exec()
