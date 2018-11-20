import os
from secrets import randbelow

def gen_urandom_pin_seq(length):
	return [randbelow(10) for _ in range(length)]

# ----------------------------

import argparse

def get_pin_length_from_command_line():
	"""returns None on failure"""

	parser = argparse.ArgumentParser()
	parser.add_argument("length")
	args = parser.parse_args()

	length_str = args.length
	length = None
	try:
		length = int(length_str) 
		print('{0} digit pin'.format(length))
	except Exception as e:
		print('invalid key length: {0}', length_str)

	return length

def run():
	pin_length = get_pin_length_from_command_line()
	if (pin_length is None): return
	
	pin_seq = gen_urandom_pin_seq(pin_length)

	pin_str = ''.join([str(n) for n in pin_seq])
	print(pin_str)

if __name__ == '__main__':
	run()
