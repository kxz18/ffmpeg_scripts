import os, sys
import datetime

file, start, end, target = sys.argv[1:]
c = 'ffmpeg -ss {} -to {} -i {} -c:v libx264 -c:a aac -strict experimental -b:a 98k {} -y'

os.system(c.format(start, end, file, target))
