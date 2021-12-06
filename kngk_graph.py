from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class kngkGraph(FigureCanvasQTAgg):
    def __init__(self, parent, width=5, height=4, dpi=100):
        super().__init__(Figure(figsize=(width, height), dpi=dpi))
        self.setParent(parent)
        self.axes = self.figure.subplots(1, 1)
        self.axes.cla()

    def read_graph(self, shapefile, add_points=None):
        self.axes.clear()
        self.axes = shapefile.plot(ax=self.axes, color='cyan', edgecolor='white')
        if add_points is not None:
            add_points.plot(ax=self.axes, marker='o', color='red', markersize=5)
        self.draw()


    #dodac czyszcenie wykresu


