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

# http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python
#
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i+n]

def run():
	key_length = get_key_length_from_command_line()
	if (key_length is None): return
	
	key_str = gen_urandom_hex_str(key_length).upper()

	print(bytes.decode(key_str))

	key_str_readable = '-'.join(bytes.decode(x) for x in chunks(key_str, 4))
	print(key_str_readable)

if __name__ == '__main__':
	run()
