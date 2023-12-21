# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2023-12-21 10:04:04
"""
import arcpy
from arcpy.sa import *

def CreateMultispectralMosaics():  # CreateMultispectralMosaics

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Check out any necessary licenses.
    arcpy.CheckOutExtension("spatial")

    T11TPN_20230915T183009_B02_10m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TPN\\T11TPN_20230915T183009_B02_10m.jp2")
    T11TPN_20230915T183009_B03_10m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TPN\\T11TPN_20230915T183009_B03_10m.jp2")
    T11TPN_20230915T183009_B04_10m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TPN\\T11TPN_20230915T183009_B04_10m.jp2")
    T11TPN_20230915T183009_B05_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TPN\\T11TPN_20230915T183009_B05_20m.jp2")
    T11TPN_20230915T183009_B06_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TPN\\T11TPN_20230915T183009_B06_20m.jp2")
    T11TPN_20230915T183009_B07_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TPN\\T11TPN_20230915T183009_B07_20m.jp2")
    T11TPN_20230915T183009_B08_10m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TPN\\T11TPN_20230915T183009_B08_10m.jp2")
    T11TPN_20230915T183009_B8A_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TPN\\T11TPN_20230915T183009_B8A_20m.jp2")
    T11TPN_20230915T183009_B11_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TPN\\T11TPN_20230915T183009_B11_20m.jp2")
    T11TPN_20230915T183009_B12_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TPN\\T11TPN_20230915T183009_B12_20m.jp2")
    T11TQN_20230915T183009_B02_10m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TQN\\T11TQN_20230915T183009_B02_10m.jp2")
    T11TQN_20230915T183009_B03_10m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TQN\\T11TQN_20230915T183009_B03_10m.jp2")
    T11TQN_20230915T183009_B04_10m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TQN\\T11TQN_20230915T183009_B04_10m.jp2")
    T11TQN_20230915T183009_B05_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TQN\\T11TQN_20230915T183009_B05_20m.jp2")
    T11TQN_20230915T183009_B06_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TQN\\T11TQN_20230915T183009_B06_20m.jp2")
    T11TQN_20230915T183009_B07_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TQN\\T11TQN_20230915T183009_B07_20m.jp2")
    T11TQN_20230915T183009_B08_10m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TQN\\T11TQN_20230915T183009_B08_10m.jp2")
    T11TQN_20230915T183009_B8A_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TQN\\T11TQN_20230915T183009_B8A_20m.jp2")
    T11TQN_20230915T183009_B11_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TQN\\T11TQN_20230915T183009_B11_20m.jp2")
    T11TQN_20230915T183009_B12_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\TQN\\T11TQN_20230915T183009_B12_20m.jp2")
    T11UPP_20230915T183009_B02_10m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UPP\\T11UPP_20230915T183009_B02_10m.jp2")
    T11UPP_20230915T183009_B03_10m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UPP\\T11UPP_20230915T183009_B03_10m.jp2")
    T11UPP_20230915T183009_B04_10m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UPP\\T11UPP_20230915T183009_B04_10m.jp2")
    T11UPP_20230915T183009_B05_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UPP\\T11UPP_20230915T183009_B05_20m.jp2")
    T11UPP_20230915T183009_B06_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UPP\\T11UPP_20230915T183009_B06_20m.jp2")
    T11UPP_20230915T183009_B07_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UPP\\T11UPP_20230915T183009_B07_20m.jp2")
    T11UPP_20230915T183009_B08_10m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UPP\\T11UPP_20230915T183009_B08_10m.jp2")
    T11UPP_20230915T183009_B8A_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UPP\\T11UPP_20230915T183009_B8A_20m.jp2")
    T11UPP_20230915T183009_B11_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UPP\\T11UPP_20230915T183009_B11_20m.jp2")
    T11UPP_20230915T183009_B12_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UPP\\T11UPP_20230915T183009_B12_20m.jp2")
    T11UQP_20230915T183009_B02_10m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UQP\\T11UQP_20230915T183009_B02_10m.jp2")
    T11UQP_20230915T183009_B03_10m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UQP\\T11UQP_20230915T183009_B03_10m.jp2")
    T11UQP_20230915T183009_B04_10m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UQP\\T11UQP_20230915T183009_B04_10m.jp2")
    T11UQP_20230915T183009_B05_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UQP\\T11UQP_20230915T183009_B05_20m.jp2")
    T11UQP_20230915T183009_B06_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UQP\\T11UQP_20230915T183009_B06_20m.jp2")
    T11UQP_20230915T183009_B07_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UQP\\T11UQP_20230915T183009_B07_20m.jp2")
    T11UQP_20230915T183009_B08_10m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UQP\\T11UQP_20230915T183009_B08_10m.jp2")
    T11UQP_20230915T183009_B8A_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UQP\\T11UQP_20230915T183009_B8A_20m.jp2")
    T11UQP_20230915T183009_B11_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UQP\\T11UQP_20230915T183009_B11_20m.jp2")
    T11UQP_20230915T183009_B12_20m_jp2 = arcpy.Raster("C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Data\\Postfire_Sentinel_Rasters\\UQP\\T11UQP_20230915T183009_B12_20m.jp2")
    Flathead_Indices_gdb = "C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Flathead Indices.gdb"
    Flathead_Reservation = "Flathead_Reservation"

    # Process: Composite Bands (Composite Bands) (management)
    S2_TPN_Postfire_2_ = "C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Flathead Indices.gdb\\S2_TPN_Postfire"
    with arcpy.EnvManager(outputCoordinateSystem="PROJCS[\"WGS_1984_Web_Mercator_Auxiliary_Sphere\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Mercator_Auxiliary_Sphere\"],PARAMETER[\"False_Easting\",0.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",0.0],PARAMETER[\"Standard_Parallel_1\",0.0],PARAMETER[\"Auxiliary_Sphere_Type\",0.0],UNIT[\"Meter\",1.0]]", pyramid="PYRAMIDS -1 NEAREST DEFAULT 75 NO_SKIP NO_SIPS", resamplingMethod="NEAREST"):
        arcpy.management.CompositeBands(in_rasters=[T11TPN_20230915T183009_B02_10m_jp2, T11TPN_20230915T183009_B03_10m_jp2, T11TPN_20230915T183009_B04_10m_jp2, T11TPN_20230915T183009_B05_20m_jp2, T11TPN_20230915T183009_B06_20m_jp2, T11TPN_20230915T183009_B07_20m_jp2, T11TPN_20230915T183009_B08_10m_jp2, T11TPN_20230915T183009_B8A_20m_jp2, T11TPN_20230915T183009_B11_20m_jp2, T11TPN_20230915T183009_B12_20m_jp2], out_raster=S2_TPN_Postfire_2_)
        S2_TPN_Postfire_2_ = arcpy.Raster(S2_TPN_Postfire_2_)

    # Process: Composite Bands (2) (Composite Bands) (management)
    S2_TQN_Postfire = "C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Flathead Indices.gdb\\S2_TQN_Postfire"
    with arcpy.EnvManager(outputCoordinateSystem="PROJCS[\"WGS_1984_Web_Mercator_Auxiliary_Sphere\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Mercator_Auxiliary_Sphere\"],PARAMETER[\"False_Easting\",0.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",0.0],PARAMETER[\"Standard_Parallel_1\",0.0],PARAMETER[\"Auxiliary_Sphere_Type\",0.0],UNIT[\"Meter\",1.0]]", pyramid="PYRAMIDS -1 NEAREST DEFAULT 75 NO_SKIP NO_SIPS", resamplingMethod="NEAREST"):
        arcpy.management.CompositeBands(in_rasters=[T11TQN_20230915T183009_B02_10m_jp2, T11TQN_20230915T183009_B03_10m_jp2, T11TQN_20230915T183009_B04_10m_jp2, T11TQN_20230915T183009_B05_20m_jp2, T11TQN_20230915T183009_B06_20m_jp2, T11TQN_20230915T183009_B07_20m_jp2, T11TQN_20230915T183009_B08_10m_jp2, T11TQN_20230915T183009_B8A_20m_jp2, T11TQN_20230915T183009_B11_20m_jp2, T11TQN_20230915T183009_B12_20m_jp2], out_raster=S2_TQN_Postfire)
        S2_TQN_Postfire = arcpy.Raster(S2_TQN_Postfire)

    # Process: Composite Bands (3) (Composite Bands) (management)
    S2_UPP_Postfire = "C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Flathead Indices.gdb\\S2_UPP_Postfire"
    with arcpy.EnvManager(outputCoordinateSystem="PROJCS[\"WGS_1984_Web_Mercator_Auxiliary_Sphere\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Mercator_Auxiliary_Sphere\"],PARAMETER[\"False_Easting\",0.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",0.0],PARAMETER[\"Standard_Parallel_1\",0.0],PARAMETER[\"Auxiliary_Sphere_Type\",0.0],UNIT[\"Meter\",1.0]]", pyramid="PYRAMIDS -1 NEAREST DEFAULT 75 NO_SKIP NO_SIPS", resamplingMethod="NEAREST"):
        arcpy.management.CompositeBands(in_rasters=[T11UPP_20230915T183009_B02_10m_jp2, T11UPP_20230915T183009_B03_10m_jp2, T11UPP_20230915T183009_B04_10m_jp2, T11UPP_20230915T183009_B05_20m_jp2, T11UPP_20230915T183009_B06_20m_jp2, T11UPP_20230915T183009_B07_20m_jp2, T11UPP_20230915T183009_B08_10m_jp2, T11UPP_20230915T183009_B8A_20m_jp2, T11UPP_20230915T183009_B11_20m_jp2, T11UPP_20230915T183009_B12_20m_jp2], out_raster=S2_UPP_Postfire)
        S2_UPP_Postfire = arcpy.Raster(S2_UPP_Postfire)

    # Process: Composite Bands (4) (Composite Bands) (management)
    S2_UQP_Postfire = "C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Flathead Indices.gdb\\S2_UQP_Postfire"
    with arcpy.EnvManager(outputCoordinateSystem="PROJCS[\"WGS_1984_Web_Mercator_Auxiliary_Sphere\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Mercator_Auxiliary_Sphere\"],PARAMETER[\"False_Easting\",0.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",0.0],PARAMETER[\"Standard_Parallel_1\",0.0],PARAMETER[\"Auxiliary_Sphere_Type\",0.0],UNIT[\"Meter\",1.0]]", pyramid="PYRAMIDS -1 NEAREST DEFAULT 75 NO_SKIP NO_SIPS", resamplingMethod="NEAREST"):
        arcpy.management.CompositeBands(in_rasters=[T11UQP_20230915T183009_B02_10m_jp2, T11UQP_20230915T183009_B03_10m_jp2, T11UQP_20230915T183009_B04_10m_jp2, T11UQP_20230915T183009_B05_20m_jp2, T11UQP_20230915T183009_B06_20m_jp2, T11UQP_20230915T183009_B07_20m_jp2, T11UQP_20230915T183009_B08_10m_jp2, T11UQP_20230915T183009_B8A_20m_jp2, T11UQP_20230915T183009_B11_20m_jp2, T11UQP_20230915T183009_B12_20m_jp2], out_raster=S2_UQP_Postfire)
        S2_UQP_Postfire = arcpy.Raster(S2_UQP_Postfire)

    # Process: Mosaic To New Raster (Mosaic To New Raster) (management)
    S2_Flathead_Postfire_Mosaic = arcpy.management.MosaicToNewRaster(input_rasters=[S2_TPN_Postfire_2_, S2_TQN_Postfire, S2_UPP_Postfire, S2_UQP_Postfire], output_location=Flathead_Indices_gdb, raster_dataset_name_with_extension="S2_Flathead_Postfire_Mosaic", coordinate_system_for_the_raster="PROJCS[\"WGS_1984_Web_Mercator_Auxiliary_Sphere\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Mercator_Auxiliary_Sphere\"],PARAMETER[\"False_Easting\",0.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",0.0],PARAMETER[\"Standard_Parallel_1\",0.0],PARAMETER[\"Auxiliary_Sphere_Type\",0.0],UNIT[\"Meter\",1.0]]", number_of_bands=10)[0]
    S2_Flathead_Postfire_Mosaic = arcpy.Raster(S2_Flathead_Postfire_Mosaic)

    # Process: Extract by Mask (Extract by Mask) (sa)
    S2_Flathead_2023_Postfire_mosaic = "C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Flathead Indices.gdb\\S2_Flathead_2023_Postfire_mosaic"
    Extract_by_Mask = S2_Flathead_2023_Postfire_mosaic
    with arcpy.EnvManager(mask=Flathead_Reservation, outputCoordinateSystem="PROJCS[\"WGS_1984_Web_Mercator_Auxiliary_Sphere\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Mercator_Auxiliary_Sphere\"],PARAMETER[\"False_Easting\",0.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",0.0],PARAMETER[\"Standard_Parallel_1\",0.0],PARAMETER[\"Auxiliary_Sphere_Type\",0.0],UNIT[\"Meter\",1.0]]"):
        S2_Flathead_2023_Postfire_mosaic = arcpy.sa.ExtractByMask(S2_Flathead_Postfire_Mosaic, Flathead_Reservation, "INSIDE", "-12785204.5969 5942706.1043 -12653172.6677 6088110.57 PROJCS[\"WGS_1984_Web_Mercator_Auxiliary_Sphere\",GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]],PROJECTION[\"Mercator_Auxiliary_Sphere\"],PARAMETER[\"False_Easting\",0.0],PARAMETER[\"False_Northing\",0.0],PARAMETER[\"Central_Meridian\",0.0],PARAMETER[\"Standard_Parallel_1\",0.0],PARAMETER[\"Auxiliary_Sphere_Type\",0.0],UNIT[\"Meter\",1.0]]")
        S2_Flathead_2023_Postfire_mosaic.save(Extract_by_Mask)


if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace="C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Flathead Indices.gdb", workspace="C:\\Users\\Zach\\Documents\\ArcGIS\\Projects\\Flathead Indices\\Flathead Indices.gdb"):
        CreateMultispectralMosaics()
