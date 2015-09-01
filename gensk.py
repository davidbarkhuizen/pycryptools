import os
import binascii

def gen_urandom_hex_str(byte_length):
	byte_array = os.urandom(byte_length)
	hex_string = binascii.hexlify(byte_array)
	return hex_string

# ----------------------------

import argparse

def get_key_length_from_command_line():
	"""returns None on failure"""

	parser = argparse.ArgumentParser()
	parser.add_argument("length")
	args = parser.parse_args()

	length_str = args.length
	length = None
	try:
		length = int(length_str) 
		print('{0} byte key'.format(length))
	except Exception as e:
		print('invalid key length: {0}', length_str)

	return length

def run():
	key_length = get_key_length_from_command_line()
	if (key_length is None): return
	
	key_str = gen_urandom_hex_str(key_length).upper()
	print(key_str)

if __name__ == '__main__':
	run()