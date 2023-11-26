# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 21:11:11 2023

@author: jerem
"""

import pandas as pd

import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import xarray as xr


if __name__ == "__main__":
    
    topograph = xr.open_dataset('C:/Users/jerem/Downloads/ETOPO_2022_v1_60s_N90W180_bed.nc')
    topograph = topograph.to_dataframe()
    topograph = topograph.reset_index()
    lon = topograph['lon']
    lat = topograph['lat']
    df = pd.read_csv('C:/Users/jerem/Downloads/Meteorite_Landings.csv')
    df = df.dropna(subset=['reclong', 'reclat'])
    
    #print(topograph)
    #print(topograph.columns)
    #latitudes = df.index.get_level_values(0)
    #longitudes = df.index.get_level_values(1)
    # Initialize a Cartopy figure with Mercator projection
    #image_data = topograph['z']
    fig, ax = plt.subplots(figsize=(100, 100), subplot_kw={'projection': ccrs.Mercator()})

    #sc = ax.scatter(lon, lat, c=topograph['z'], transform=ccrs.PlateCarree())
    # Add features
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    
    ax.scatter(df['reclong'], df['reclat'],color='red', transform=ccrs.PlateCarree())
    # Set the extent of the map if needed
    ax.set_extent([-180, 180, -90, 90])

    plt.show()


    
    

    





