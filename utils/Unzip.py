import pyautogui
import time
import os
import zipfile

'''
After download - file unzip
This is an auto-unzip script to unzip Geo-data, downloaded from HaitiData by Google Chrome
Before run this script: Rename the compressed packages to 'lidar_clipped_1.zip', 'lidar_clipped_2.zip','lidar_clipped_3.zip' etc.

After run this script: All the GeoTiff will be stored inside one folder
'''

# Change WD
print(os.getcwd())
os.chdir('/PATH/TO/THE/DOWNLOADED/DATA') #chaneg wd to the folder which stored the downloaded data
print(os.getcwd())

print(os.listdir()) # list file
FileNum = len(os.listdir()) # file number
print(FileNum) # check file number

for i in range(1,FileNum+1):
    with zipfile.ZipFile('lidar_clipped_' + str(i) + '.zip', "r") as zip_ref:
        zip_ref.extractall() #unzip
        # rename unzipped file
        # os.chdir('/Volumes/ZWL_Drive/File/data/Lidar/Merge3/lidar_clipped') #change wd to unzip file
        # time.sleep(5)
        # rename_file = os.listdir()[0] # collect the first item in the list
        # os.rename(rename_file, 'lidar_clipped_' + str(i) + '.tif') # rename target file
        # os.chdir('/Volumes/ZWL_Drive/File/data/Lidar/Merge3') #change to the parent folder