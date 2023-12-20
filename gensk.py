import os
import binascii

KEY_TYPE_HEX = 'hex'
KEY_TYPE_BASE64 = 'b64'
SUPPORTED_KEY_TYPES = [KEY_TYPE_HEX, KEY_TYPE_BASE64]

KEY_LENGTH_MIN_BYTES=8
KEY_LENGTH_MAX_BYTES=64
KEY_LENGTH_REQS_DESCRIPTION=f'key length >= {KEY_LENGTH_MIN_BYTES} and <= key length <= {KEY_LENGTH_MAX_BYTES}'

def gen_urandom_hex_str(byte_length):
	byte_array = os.urandom(byte_length)
	hex_string = binascii.hexlify(byte_array)
	return hex_string

# ----------------------------

import argparse

def get_key_length_from_command_line():
	'''returns None on failure'''

	parser = argparse.ArgumentParser()
	
	parser.add_argument("key_type")	
	parser.add_argument("key_length")
	args = parser.parse_args()

	key_type = None
	try:
		key_type = args.key_type 
		print(f'{key_type} type key')
	except Exception as e:
		print(f'invalid key type: {args.key_type}, must be one of {SUPPORTED_KEY_TYPES}')
		raise

	key_length = None
	try:
		key_length = int(args.key_length)
		print(f'{key_length} byte key')
	except Exception as e:
		print(f'invalid key length: {args.key_length}. {KEY_LENGTH_REQS_DESCRIPTION}')
		raise
	if key_length < KEY_LENGTH_MIN_BYTES or key_length > KEY_LENGTH_MAX_BYTES:
		raise Exception(f'invalid key length. required: {KEY_LENGTH_REQS_DESCRIPTION}')

	return key_type, key_length

def chunks(l, n):
    '''yield successive n-sized chunks from l.'''
    for i in range(0, len(l), n):
        yield l[i:i+n]

def run():
	key_type, key_length = get_key_length_from_command_line()
	

	key_str = None
	key_str_readable = None

	if key_type == KEY_TYPE_HEX:
		key_str = gen_urandom_hex_str(key_length).upper()
		key_str_readable = '-'.join(bytes.decode(x) for x in chunks(key_str, 4))
	elif key_type == KEY_TYPE_BASE64:
		pass

	print(bytes.decode(key_str))
	print(key_str_readable)

if __name__ == '__main__':
	run()
