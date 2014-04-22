__author__ = "Andrew"

from . import gdal_module
import unittest
import os

#The DEM you want to use for gdal unit tests
#Use smaller DEM's if you want this to actually finish
dem1 = "C:\\Users\\Andrew\\Desktop\\DEMs\\DTEED_020492_1830_021481_1830_A01.IMG"
dem2 = "C:\\Users\\Andrew\\Desktop\\DEMs\\DTEEC_017569_1645_016857_1645_A01.IMG"
dem3 = ""

#Helpful variables for all tests
project_location = os.path.dirname(__file__)
color_destination = os.path.normpath("\""+project_location+"/maps/colorrelief.tiff\"")
hillshade_destination = os.path.normpath("\""+project_location+"/maps/hillshade.tiff\"")

# Assumptions
#1.) The gdal and hsv_merge utiltiies are assumed to be pre-tested for correctness
#2.) We will be looking for true to see if an executed test successfully passes
#3.) We will be looking for a false to see if an executed test fails

#All of these tests focus on the functions within the gdal driver
class TestGdalHillshade(unittest.TestCase):
    def test_gdal_hillshade(self):
        gdal = gdal_module.GDALDriver(dem1)

        gdal.gdal_clean_up(hillshade_destination, "")
        return_value = gdal.gdal_hillshade(hillshade_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(hillshade_destination, "")

    def test_gdal_hillshade_alt_file(self):
        gdal = gdal_module.GDALDriver(dem2)

        gdal.gdal_clean_up(hillshade_destination, "")
        return_value = gdal.gdal_hillshade(hillshade_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(hillshade_destination, "")

#All of these tests do not test for correctness of GDAL
#These tests check for correctness of our created color files by processing them through gdal
#If they process, the color file was formed correctly... there's better ways to do this
#But i'm lazy and this fufills the concept logically
class TestGdalColorrelief(unittest.TestCase):
    def test_gdal_color_relief_blue_steel(self):
        gdal = gdal_module.GDALDriver(dem1)
        color_relief = os.path.normpath("\""+project_location+"/color_maps/Blue_Steel.txt\"")

        gdal.gdal_clean_up(color_destination, "")
        return_value = gdal.gdal_color_relief(color_relief, color_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(color_destination, "")

    def test_gdal_color_relief_diverging_blue_red(self):
        gdal = gdal_module.GDALDriver(dem1)
        color_relief = os.path.normpath("\""+project_location+"/color_maps/Diverging_BlueRed.txt\"")

        gdal.gdal_clean_up(color_destination, "")
        return_value = gdal.gdal_color_relief(color_relief, color_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(color_destination, "")

    def test_gdal_color_relief_diverging_brown_blue(self):
        gdal = gdal_module.GDALDriver(dem1)
        color_relief = os.path.normpath("\""+project_location+"/color_maps/Diverging_BrownBlue.txt\"")

        gdal.gdal_clean_up(color_destination, "")
        return_value = gdal.gdal_color_relief(color_relief, color_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(color_destination, "")

    def test_gdal_color_relief_diverging_green_red(self):
        gdal = gdal_module.GDALDriver(dem1)
        color_relief = os.path.normpath("\""+project_location+"/color_maps/Diverging_GreenRed.txt\"")

        gdal.gdal_clean_up(color_destination, "")
        return_value = gdal.gdal_color_relief(color_relief, color_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(color_destination, "")

    def test_gdal_color_relief_diverging_red_blue(self):
        gdal = gdal_module.GDALDriver(dem1)
        color_relief = os.path.normpath("\""+project_location+"/color_maps/Diverging_RedBlue.txt\"")

        gdal.gdal_clean_up(color_destination, "")
        return_value = gdal.gdal_color_relief(color_relief, color_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(color_destination, "")

    def test_gdal_color_relief_diverging_red_brown(self):
        gdal = gdal_module.GDALDriver(dem1)
        color_relief = os.path.normpath("\""+project_location+"/color_maps/Diverging_RedBrown.txt\"")

        gdal.gdal_clean_up(color_destination, "")
        return_value = gdal.gdal_color_relief(color_relief, color_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(color_destination, "")

    def test_gdal_color_relief_diverging_red_gray(self):
        gdal = gdal_module.GDALDriver(dem1)
        color_relief = os.path.normpath("\""+project_location+"/color_maps/Diverging_RedGray.txt\"")

        gdal.gdal_clean_up(color_destination, "")
        return_value = gdal.gdal_color_relief(color_relief, color_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(color_destination, "")

    def test_gdal_color_relief_earth(self):
        gdal = gdal_module.GDALDriver(dem1)
        color_relief = os.path.normpath("\""+project_location+"/color_maps/Earth.txt\"")

        gdal.gdal_clean_up(color_destination, "")
        return_value = gdal.gdal_color_relief(color_relief, color_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(color_destination, "")

    def test_gdal_color_relief_rainbow_light(self):
        gdal = gdal_module.GDALDriver(dem1)
        color_relief = os.path.normpath("\""+project_location+"/color_maps/Rainbow_Light.txt\"")

        gdal.gdal_clean_up(color_destination, "")
        return_value = gdal.gdal_color_relief(color_relief, color_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(color_destination, "")

    def test_gdal_color_relief_rainbow_medium(self):
        gdal = gdal_module.GDALDriver(dem1)
        color_relief = os.path.normpath("\""+project_location+"/color_maps/Rainbow_Medium.txt\"")

        gdal.gdal_clean_up(color_destination, "")
        return_value = gdal.gdal_color_relief(color_relief, color_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(color_destination, "")

    def test_gdal_color_relief_rainbow_saturated(self):
        gdal = gdal_module.GDALDriver(dem1)
        color_relief = os.path.normpath("\""+project_location+"/color_maps/Rainbow_Saturated.txt\"")

        gdal.gdal_clean_up(color_destination, "")
        return_value = gdal.gdal_color_relief(color_relief, color_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(color_destination, "")

    def test_gdal_color_relief_sequential_blue(self):
        gdal = gdal_module.GDALDriver(dem1)
        color_relief = os.path.normpath("\""+project_location+"/color_maps/Sequential_Blue.txt\"")

        gdal.gdal_clean_up(color_destination, "")
        return_value = gdal.gdal_color_relief(color_relief, color_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(color_destination, "")

    def test_gdal_color_relief_sequential_bluegreen(self):
        gdal = gdal_module.GDALDriver(dem1)
        color_relief = os.path.normpath("\""+project_location+"/color_maps/Sequential_BlueGreen.txt\"")

        gdal.gdal_clean_up(color_destination, "")
        return_value = gdal.gdal_color_relief(color_relief, color_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(color_destination, "")

    def test_gdal_color_relief_sequential_green(self):
        gdal = gdal_module.GDALDriver(dem1)
        color_relief = os.path.normpath("\""+project_location+"/color_maps/Sequential_Green.txt\"")

        gdal.gdal_clean_up(color_destination, "")
        return_value = gdal.gdal_color_relief(color_relief, color_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(color_destination, "")

    def test_gdal_color_relief_sequential_red(self):
        gdal = gdal_module.GDALDriver(dem1)
        color_relief = os.path.normpath("\""+project_location+"/color_maps/Sequential_Red.txt\"")

        gdal.gdal_clean_up(color_destination, "")
        return_value = gdal.gdal_color_relief(color_relief, color_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(color_destination, "")

    def test_gdal_color_relief_sequential_yellowbrown(self):
        gdal = gdal_module.GDALDriver(dem1)
        color_relief = os.path.normpath("\""+project_location+"/color_maps/Sequential_YellowBrown.txt\"")

        gdal.gdal_clean_up(color_destination, "")
        return_value = gdal.gdal_color_relief(color_relief, color_destination)
        self.assertTrue(return_value)
        gdal.gdal_clean_up(color_destination, "")


class TestGdalHsvMerge(unittest.TestCase):
    def test_hsv_merge(self):
        pass


class TestGdalCleanup(unittest.TestCase):
    def test_gdal_cleanup(self):
        pass

