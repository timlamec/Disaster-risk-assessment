import pyautogui
import time
import os

'''
This is an auto-download script for Haiti geo-data Lidar(DTM)/Orthophotos from the website HaitiData (https://haitidata.org/)
Users can use this script starts from checking the start and end point of the research area
Then set the coordinates to the x,y start,end parts in the script
By running the script, the selected area will be downloaded to the local machine
'''

# print(pyautogui.position()) # use this line to check coordinate (ie. download button, research area)


# Coordinates
# start point: Upper left corner
# ending point: Bottom right corner
x_start = -474
x_end = -445
y_start = 521
y_end = 701

# Divisors
total_x = x_start - x_end
total_y = y_start - y_end
pixel_x = 25
pixel_y = 25
# Set the download area each time, should be about 60-70 MB based on the server requirements
x_sections = abs(total_x//pixel_x)
y_sections = abs(total_y//pixel_y)

# # Check map position
# pyautogui.moveTo(x_start, y_start, duration=1)  # move to start position
# time.sleep(3)
# pyautogui.moveTo(x_end, y_end, duration=1)  # move to end position

# Data download
pyautogui.moveTo(-957, 813, duration=1)  # move to website page
pyautogui.click(-957, 813) # click download website
time.sleep(1)

pyautogui.size()
for row in range(1,y_sections):
    for col in range(1,x_sections):
        x1 = x_start + (col-1) * pixel_x-3
        # -1 overlap pixel, to make sure the figure is coverlaped with the previous one
        y1 = y_start + (row-1) * pixel_y-1
        x2 = x_start + col * pixel_x
        y2 = y_start + row * pixel_y
        print(x1,y1,x2,y2)
        pyautogui.moveTo(-1320, 365, duration=1)  # move to 'rectangle selection'
        pyautogui.click(-1320, 365)  # select 'rectangle' button
        pyautogui.moveTo(x1, y1, duration=1)  # move to map site 1
        pyautogui.dragTo(x2, y2, duration=1, button='left')  # drag to map site 2
        pyautogui.moveTo(-957, 813, duration=1) # move to download
        pyautogui.click(-957, 813)  # click download
        time.sleep(12) # time buffer to let browser finish downloading
