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
import argparse as ap
###############################################################################


def main(parent_folder, output_folder, rast_type):
    #set the workspace to the raster folder
    arcpy.env.workspace = parent_folder

    # get a list of all files
    file_list = os.listdir(parent_folder)

    # prompt warning if file format not supported
    for f in file_list:
      if not f.endswith(('.bmp', '.gif', '.img', '.jp2', '.jpg', '.png', '.tif')):
      	arcpy.AddWarning(f + ' is not supported.')
		
		# produce a list of all tifs in the parent folder
    rast_list = arcpy.ListRasters()

		# get the number of rasters in the directory
    list_len = len(rast_list)
    
    # step progressor
    arcpy.SetProgressor('step', 'Converting...', 0, list_len, 1)

    # iterate through all rasters and conver them
    for item in rast_list:
        # Convert the raster
        arcpy.RasterToOtherFormat_conversion(item, output_folder, rast_type)
        # Update the user to which raster was converted
        arcpy.AddMessage(item + ' is converted.')


###############################################################################


if __name__ == '__main__':
    # get the directory containing the original rasters
    parent_folder = arcpy.GetParameterAsText(0)
    # get the directory for raster output
    output_folder = arcpy.GetParameterAsText(1)
    # get the type of raster to output
    rast_type = arcpy.GetParameterAsText(2)

    # run the script
    main(parent_folder, output_folder, rast_type)
