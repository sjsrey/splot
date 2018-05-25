import matplotlib.pyplot as plt
import libpysal.api as lp
from libpysal import examples
import geopandas as gpd
import esda

from splot._viz_bokeh import (plot_choropleth, lisa_cluster,
                              mplot, plot_local_autocorrelation)

def test_plot_choropleth():
    link = examples.get_path('columbus.shp')
    df = gpd.read_file(link)

    w = lp.Queen.from_dataframe(df)
    w.transform = 'r'

    TOOLS = "tap,help"
    fig = plot_choropleth(df, 'HOVAL', title='columbus',
                          reverse_colors=True, tools=TOOLS)
    plt.close(fig)


def test_lisa_cluster():
    link = examples.get_path('columbus.shp')
    df = gpd.read_file(link)

    y = df['HOVAL'].values
    w = lp.Queen.from_dataframe(df)
    w.transform = 'r'

    moran_loc = esda.moran.Moran_Local(y, w)

    TOOLS = "tap,reset,help"
    fig = lisa_cluster(moran_loc, df, p=0.05, tools=TOOLS)
    plt.close(fig)


def test_mplot():
    link = examples.get_path('columbus.shp')
    df = gpd.read_file(link)

    y = df['HOVAL'].values
    w = lp.Queen.from_dataframe(df)
    w.transform = 'r'

    moran_loc = esda.moran.Moran_Local(y, w)

    fig = mplot(moran_loc, p=0.05)
    plt.close(fig)


def test_plot_local_autocorrelation():
    link = examples.get_path('columbus.shp')
    df = gpd.read_file(link)

    y = df['HOVAL'].values
    w = lp.Queen.from_dataframe(df)
    w.transform = 'r'

    moran_loc = esda.moran.Moran_Local(y, w)

    fig = plot_local_autocorrelation(moran_loc, df, 'HOVAL')
    plt.close(fig)