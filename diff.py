def get_diff(filename):
	fp = open(filename, 'r')
	raw_file = fp.readlines()
	A_list = [[0 for i in range(16)] for i in range(5)] # indexed A[j][k]
	x_list = [[[0 for i in range(16)]for i in range(5)] for i in range(5)]
	y_list = [[[0 for i in range(16)]for i in range(5)] for i in range(5)]
	z_list = [[[0 for i in range(16)]for i in range(5)] for i in range(5)]
	#parse sol file
	for i in raw_file:
		p = i.split(' ')[0].split('_')
		if p[0] == 'x':
			x_list[int(p[2])][int(p[3])][int(p[4])] = int(i.split(' ')[1][:-1])
		if p[0] == 'A':
			A_list[int(p[2])][int(p[3])] = int(i.split(' ')[1][:-1])
		if p[0] == 'y':
			y_list[int(p[2])][int(p[3])][int(p[4])] = int(i.split(' ')[1][:-1])
		if p[0] == 'z':
			z_list[int(p[2])][int(p[3])][int(p[4])] = int(i.split(' ')[1][:-1])	
						
	return (x_list, y_list, z_list, A_list)
