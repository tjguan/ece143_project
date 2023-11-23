# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 21:11:11 2023

@author: jerem
"""

import pandas as pd

import matplotlib.pyplot as plt

# If you're using Basemap, you need to install it with `conda install basemap` or `pip install basemap`

import cartopy.crs as ccrs
import cartopy.feature as cfeature

if __name__ == "__main__":
    
    
    df = pd.read_csv('C:/Users/jerem/Downloads/Meteorite_Landings.csv')
    # Initialize a Cartopy figure with PlateCarree projection
    fig, ax = plt.subplots(figsize=(12, 8), subplot_kw={'projection': ccrs.PlateCarree()})

    # Add features for context
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    # Plot the meteorite locations on the map
    ax.scatter(df['reclong'], df['reclat'], s=10, color='red', marker='o', alpha=0.75)
    # Set the extent of the map if needed
    ax.set_extent([-180, 180, -90, 90])

    # Show the plot
    plt.show()


    
    

    





