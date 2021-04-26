#-------------------------------------------------------------------------------
"""
Converts raster formats
"""
#-------------------------------------------------------------------------------
import os
import arcpy
def main(parent_folder, output_folder, type):
    #arcpy.env.workspace = 'H:\ReformatTest'
    # Set the workspace to the raster folder
    arcpy.env.workspace = parent_folder

    # Produce a list of all tifs in the parent folder
    rast_list = arcpy.ListRasters()
    list_len = len(rast_list)
    arcpy.SetProgressor('step', "Converting raster", 0, list_len, 1)
    for item in rast_list:
        #arcpy.RasterToOtherFormat_conversion(item, output_folder, type)
        arcpy.SetProgressorPosition()
        arcpy.AddMessage(item)

################################################################################
if __name__ == '__main__':
    parent_folder = arcpy.GetParameterAsText(0)
    output_folder = arcpy.GetParameterAsText(1)
    type = arcpy.GetParameterAsText(2)

    main(parent_folder, output_folder, type)
