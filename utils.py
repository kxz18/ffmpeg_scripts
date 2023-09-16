import os
import shutil


def get_suffix(path: str):
	return os.path.splitext(path)[-1]


def change_suffix(path: str, target_suffix: str):
	filename = os.path.splitext(path)[0]
	return ''.join([filename, target_suffix])


def remove(path):
	if os.path.isdir(path):
		shutil.rmtree(path)
	else:
		os.remove(path)
