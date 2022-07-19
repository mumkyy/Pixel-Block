# generates blocks.csv, matching blocks to their corresponding dominant colors
# all wrapped up in a nice CSV file
from colorthief import ColorThief
import os
import csv

header = ['block','R','G','B']

f = open('blocks.csv','w',newline='')

writer = csv.writer(f)

writer.writerow(header)

for file in os.listdir('block'):
    f = os.path.join('block',file)
    if os.path.isfile(f):
        color_thief = ColorThief(f)
        dominant_color = color_thief.get_color(quality=1)
        writer.writerow([file[:-4],dominant_color[0],dominant_color[1],dominant_color[2]])




