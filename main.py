import os, sys
import datetime
import argparse


from funcs import cut, convert
from utils import get_suffix, change_suffix, remove


def parse():
	parser = argparse.ArgumentParser(description='python interface for ffmpeg')
	parser.add_argument('-a', '--action', type=str, required=True,
			    choices=['cut', 'convert'], help='action to do')

	# for cut
	parser.add_argument('-s', '--start', type=str, help='start')
	parser.add_argument('-t', '--to', type=str, help='to')

	# input and output
	parser.add_argument('-i', '--input', type=str, required=True, help='input file')
	parser.add_argument('-o', '--output', type=str, required=True, help='output file')

	return parser.parse_args()
	

def main(args):
	action = args.action
	input_suffix, output_suffix = get_suffix(args.input), get_suffix(args.output)
	if action == 'convert':
		assert input_suffix != output_suffix, 'Video type not changed!'
		convert(args.input, args.output)
	elif action == 'cut':
		i, o = args.input, args.output
		need_convert = False
		if input_suffix != output_suffix:
			need_convert = True
			o = change_suffix(o, input_suffix)
		cut(args.start, args.to, i, o)
		if need_convert:
			convert(o, args.output)
			remove(o)

if __name__ == '__main__':
	main(parse())
