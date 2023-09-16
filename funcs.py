import os, sys
import datetime


def cut(start, end, input, output):
	c = 'ffmpeg -ss {} -to {} -i {} -c:v libx264 -c:a aac -strict experimental -b:a 98k {} -y'
	os.system(c.format(start, end, input, output))


def convert(src, dst):
	c = 'ffmpeg -i {} -codec copy {}'
	os.system(c.format(src, dst))
