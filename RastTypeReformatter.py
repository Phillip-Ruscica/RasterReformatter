#!/usr/bin/env python2#-------------------------------------------------------------------------------
"""
Description: This is an ArcGIS tool used for reformatting a directory of
rasters

Created by: Phillip Ruscica

Date Created: April 28th 2021
"""
###############################################################################
import os
import arcpy
###############################################################################


def main(parent_folder, output_folder, rast_type):
    # Set the workspace to the raster folder
    arcpy.env.workspace = parent_folder

    # Produce a list of all tifs in the parent folder
    rast_list = arcpy.ListRasters()
    
    # Get the number of rasters in the directory
    list_len = len(rast_list)
    
    # Create a progressor
    arcpy.SetProgressor('default')

    # Iterate through all rasters and conver them
    for item in rast_list:
        # Convert the raster
        arcpy.RasterToOtherFormat_conversion(item, output_folder, rast_type)
        # Update the user to which raster was converted
        arcpy.AddMessage(item)


###############################################################################


if __name__ == '__main__':
    # Get the directory containing the original rasters
    parent_folder = arcpy.GetParameterAsText(0)
    # Get the directory for raster output
    output_folder = arcpy.GetParameterAsText(1)
    # Get the type of raster to output
    rast_type = arcpy.GetParameterAsText(2)

    # Run the script
    main(parent_folder, output_folder, rast_type)
