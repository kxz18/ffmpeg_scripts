import os, sys


src, dst = sys.argv[1:]

c = 'ffmpeg -i {} -codec copy {}'

os.system(c.format(src, dst))
