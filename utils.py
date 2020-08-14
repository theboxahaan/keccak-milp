from keccak import Keccak
import re

def parse(filename, verbose = None):
	'''
	Parses r/+_{rnd}_+/ in .sol files into different lists
	Entries should strictly be of the form x_0_0_1_0 = 1\\n
	'''
	fp = open(filename, 'r')
	buf = fp.readlines()
	dic = {}

	for str in buf:
		if re.match(r'^(\D+_\d+)(_\d+)+ (\d+)\n', str) is None:
			continue	
		i, j = str.split(' ')

		mo = re.match(r'^(\D+_\d+)', i)
		tmp = re.split(mo.group()+'_', i)[1].split('_')
		if len(tmp) is 3:
			if mo.group() not in dic:
				dic[mo.group()] = [[[0 for i in range(16)] for i in range(5)] for i in range(5)]
			dic[mo.group()][int(tmp[0])][int(tmp[1])][int(tmp[2])] = int(j[:-1])

		else:
			if mo.group() not in dic:
				dic[mo.group()] = [[0 for i in range(16)] for i in range(5)]
			dic[mo.group()][int(tmp[0])][int(tmp[1])] = int(j[:-1])
	
	if verbose is 'v':
		print('Done Parsing File')
		print(list(dic))
	return dic	
	

def gen_ddt(sbox, w):
	ddt = [[0 for i in range(2**w)] for i in range(2**w)]
	for pt1 in range(2**w):
		for diff in range(2**w):
			pt2 = pt1 ^ diff
			ddt[diff][sbox[pt1]^sbox[pt2]] += 1
	return ddt




def diff_prob(s1, s2):
	'''
	Calculate the differential probability of s1 and s2 over chi
	'''
	sbox = [0,5,10,11,20,17,22,23,9,12,3,2,13,8,15,14,18,21,24,27,6,1,4,7,26,29,16,19,30,25,28,31]
	ddt = gen_ddt(sbox, 5)
	
	#s1 and s2 are keccak states
	prob = 1
	for i in range(5):
		for k in range(16):
			tmp1 = 0
			tmp2 = 0
			for j in range(5):
				tmp1 |= (s1[i][j][k] << j)&(2**5 -1)
				tmp2 |= (s2[i][j][k] << j)&(2**5 -1)
			prob *= (ddt[tmp1][tmp2]/32)
	print(prob)		
	return prob


if __name__ == '__main__':
	parse('Round1.sol', 'v')
