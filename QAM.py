'''
This is a generic QAM mudulator. It can modulate any QAM where M=2^2k, k=1,2,3...

Input:
	data: 			input data array
	M: 				QAM type
	code:			modulation code. can be "gray" or "binary"
	data_type:		input data type. can be "binary" or "numbers"

Output:
	S:				QAM modulated signal
'''

from numpy import log2, arange, sqrt, flip, concatenate, zeros, array, floor, sqrt, array, bitwise_xor

def modulator(data, M, code='gray', data_type='binary'):
	# Constants
	sqrt_M = sqrt(M).astype(int)
	k = log2(M).astype(int)

	# Binary to Gray code constelation convertor
	vect = array(range(sqrt_M))
	gray_constallation = bitwise_xor(vect, floor(vect/2).astype(int))

	# Gray code constelation to symbols convertor
	vect = arange(1, sqrt(M), 2)
	symbols = concatenate((flip(-vect, axis=0), vect)).astype(int)

	# Modulation
	if data_type == 'binary':
		# Data handling
		data_input = data.reshape((-1,k))
		I = zeros((data_input.shape[0],))
		Q = zeros((data_input.shape[0],))
		for n in range(int(data_input.shape[1] / 2)):
			I = I + data_input[:,n] * 2 ** n
		for n in range(int(data_input.shape[1]/2),int(data_input.shape[1])):
			Q = Q + data_input[:,n] * 2 ** (n - int(data_input.shape[1]/2))
	elif data_type == 'numbers':
		tmp = data / sqrt_M
		Q = floor(tmp)
		I = (tmp - Q) * 4
	else:
		return 0

	I = I.astype(int)
	Q = Q.astype(int)

	if code == 'gray':
		I = gray_constallation[I]
		Q = gray_constallation[Q]

	I = symbols[I]
	Q = symbols[Q]

	S = I + 1j * Q

	return S