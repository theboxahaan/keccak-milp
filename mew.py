import argparse
from copy import deepcopy

rho_val = [[0, 36, 3, 105, 210], [1, 300, 10, 45, 66], [190, 6, 171, 15, 253], [28, 55, 153, 21, 120], [91, 276, 231, 136, 78]]




def constraint(n, w, rounds, bs):
	print("Minimize")
	#Objective Function
	for r in range(rounds):
		for y in range(5):
			for z in range(16):
				if y==4 and z==15 and r==rounds-1:
					print(f'A_{r}_{y}_{z}')
				else:
					print(f"A_{r}_{y}_{z} + ", end="")

	print("\n\nSubject To")

	x_list = [[[ f'x_0_{k}_{j}_{i}' for i in range(16)] for j in range(5)] for k in range(5)]
	#print(len(i_list[0]))

	#for i in range(16):
	#	print(f'{i_list[0][1][i]}')
	for i in range(5):
		for j in range(5):
			for k in range(16):
				if i == 4 and j ==4 and k == 15:
					print(f'{x_list[i][j][k]} >= 1')
				else:
					print(f'{x_list[i][j][k]} + ', end="")
	for rnd in range(rounds) :

		y_list = [[[ f'y_{rnd}_{k}_{j}_{i}' for i in range(16)] for j in range(5)] for k in range(5)]
		##inequalities for Computing parity bits
		for i in range(5):
			for k in range(16):
				for j in range(5):
					if j ==4 : 
						print(f'{x_list[i][j][k]} + p_{rnd}_{i}_{k} - 2 d_{rnd}_{i}_{k} >= 0')
					else:
						print(f'{x_list[i][j][k]} + ', end="")
				#print('*'*100)	
		
		for i in range(5):
			for k in range(16):
				for j in range(5):
					if j == 4 :
						print(f'- {x_list[i][j][k]} - p_{rnd}_{i}_{k} + 2 d_{rnd}_{i}_{k} >= 0')
					else:
						print(f'- {x_list[i][j][k]} ', end="")

		for i in range(5):
			for k in range(16):
				for j in range(5):
					print(f'd_{rnd}_{i}_{k} - {x_list[i][j][k]} >= 0')
				print(f"d_{rnd}_{i}_{k} - p_{rnd}_{i}_{k} >= 0")		

		# parity bits inequality done, now for theta
		for i in range(5):
			for k in range(16):
				for j in range(5):
					print(f'{x_list[i][j][k]} + p_{rnd}_{(i-1)%5}_{k} + p_{rnd}_{(i+1)%5}_{(k-1)%16} + {y_list[i][j][k]} - 2 e_{rnd}_{i}_{j}_{k} >= 0')
					print(f'2 e_{rnd}_{i}_{j}_{k} - {x_list[i][j][k]} - p_{rnd}_{(i-1)%5}_{k} - p_{rnd}_{(i+1)%5}_{(k-1)%16} - {y_list[i][j][k]} >= 0')
					print(f'e_{rnd}_{i}_{j}_{k} - {x_list[i][j][k]} >= 0')
					print(f'e_{rnd}_{i}_{j}_{k} - p_{rnd}_{(i-1)%5}_{k} >= 0')
					print(f'e_{rnd}_{i}_{j}_{k} - p_{rnd}_{(i+1)%5}_{(k-1)%16} >= 0')
					print(f'e_{rnd}_{i}_{j}_{k} - {y_list[i][j][k]} >= 0')
		
		#for i in range(5):
		#	for j in range(5):
		#		for k in range(16):
		#			if i==4 and j==4 and k==15:
		#				print(f'{y_list[i][j][k]} >= 1')
		#			
		#			else:
		#				print(f'{y_list[i][j][k]} + ')

		# rho permutation

		tmp = [[[ f'0' for i in range(16)] for j in range(5)] for k in range(5)]
		
		for i in range(5):
			for j in range(5):
				for k in range(16):
					tmp[i][j][(k+rho_val[i][j])%16] = y_list[i][j][k]  
		y_list = deepcopy(tmp)
		



		#pi permutation

		tmp2 = [[[ f'0' for i in range(16)] for j in range(5)] for k in range(5)]
		
		for i in range(5):
			for j in range(5):
				for k in range(16):
					tmp2[j][(2*i + 3*j)%5][k] = y_list[i][j][k]  
		y_list = deepcopy(tmp2)
		#sbox chi
	
		z_list  = [[[ f'z_{rnd}_{k}_{j}_{i}' for i in range(16)] for j in range(5)] for k in range(5)]
		print("")
		for j in range(5):
			for k in range(16):
				for i in range(5):
					print(f'- {y_list[i][j][k]} + A_{rnd}_{j}_{k} >= 0')
		print("")
		for j in range(5):
			for k in range(16):
				for i in range(5):
					if i ==4:
						print(f'{y_list[i][j][k]} - A_{rnd}_{j}_{k} >= 0')
					else:
						print(f'{y_list[i][j][k]} + ', end="")
		print("")
		for k in range(16):
			for j in range(5):
				print(f'5 {z_list[0][j][k]} + 5 {z_list[1][j][k]} + 5 {z_list[2][j][k]} + 5 {z_list[3][j][k]} + 5 {z_list[4][j][k]} - {y_list[0][j][k]} - {y_list[1][j][k]} - {y_list[2][j][k]} - {y_list[3][j][k]} - {y_list[4][j][k]} >= 0 ')
				print(f'5 {y_list[0][j][k]} + 5 {y_list[1][j][k]} + 5 {y_list[2][j][k]} + 5 {y_list[3][j][k]} + 5 {y_list[4][j][k]} - {z_list[0][j][k]} - {z_list[1][j][k]} - {z_list[2][j][k]} - {z_list[3][j][k]} - {z_list[4][j][k]} >= 0 ')

		print("")
		for k in range(16):
			for j in range(5):
				print(f'{y_list[0][j][k]} + {y_list[1][j][k]} + {y_list[2][j][k]} + {y_list[3][j][k]} + {y_list[4][j][k]} + {z_list[0][j][k]} + {z_list[1][j][k]} + {z_list[2][j][k]} + {z_list[3][j][k]} + {z_list[4][j][k]} - {bs} f_{rnd}_{j}_{k} >= 0')
				for i in range(5):
					print(f'f_{rnd}_{j}_{k} - {z_list[i][j][k]} >= 0')
					print(f'f_{rnd}_{j}_{k} - {y_list[i][j][k]} >= 0')
		
		
		
		x_list = deepcopy(z_list)

#		print("*"*100)
	
	print("Binary\n\n")
	for i in range(5):
		for  j in range(5):
			for k in range(16):
				print(f"x_0_{i}_{j}_{k}")
	
	for r in range(rounds):
		for i in range(5):
			for k in range(16):
				print(f'p_{r}_{i}_{k}')

	for r in range(rounds):
		for j in range(5):
			for k in range(16):
				print(f'f_{r}_{j}_{k}')

	for r in range(rounds):
		for i in range(5):
			for j in range(5):
				for k in range(16):
					print(f'y_{r}_{i}_{j}_{k}\nz_{r}_{i}_{j}_{k}')
	print("General\n\n")
	for r in range(rounds):
		for i in range(5):
			for j in range(5):
				for k in range(16):
					print(f'e_{r}_{i}_{j}_{k}')
	
		
	for r in range(rounds):
		for i in range(5):
			for k in range(16):
				print(f'd_{r}_{i}_{k}')

	print("End")


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--r', dest='round')
	args = parser.parse_args()
	constraint(64, 4, int(args.round), 2)

