import copy 

class Keccak():

	def __init__(self, state):
		self.state = state 
		self.perm = 400
	

	def __getitem__(self, i):
		return self.state[i]
		
	
	def theta(self):
		parity = [[0 for i in range(16)] for j in range(5)]
		for i in range(5):
			for k in range(16):
				for j in range(5):
					parity[i][k] = parity[i][k] ^ self.state[i][j][k]
		for i in range(5):
			for k in range(16):
				for j in range(5):
					self.state[i][j][k] = self.state[i][j][k] ^ parity[(i-1)%5][k] ^ parity[(i+1)%5][(k-1)%16]
		
	def rho(self):	
		
		rho_val = [[0, 36, 3, 105, 210], [1, 300, 10, 45, 66], [190, 6, 171, 15, 253], [28, 55, 153, 21, 120], [91, 276, 231, 136, 78]]
		tmp = [[[0 for i in range(16)] for i in range(5)] for i in range(5)]
		for i in range(5):
			for j in range(5):
		 		for k in range(16):
			 		tmp[i][j][(k+rho_val[i][j])%16] = self.state[i][j][k]
				
		self.state = copy.deepcopy(tmp)
	
	def pi(self):
		tmp = [[[0 for i in range(16)] for i in range(5)] for i in range(5)]
		for i in range(5):
			for j in range(5):
		 		for k in range(16):
			 		tmp[j][(2*i+3*j)%5][k] = self.state[i][j][k]
				
		self.state = copy.deepcopy(tmp)
	

	def chi(self):
		tmp = [[[0 for i in range(16)] for i in range(5)] for i in range(5)]
		
		for k in range(16):
			for j in range(5):
				for i in range(5):
					tmp[i][j][k] = self.state[i][j][k] ^ ((self.state[(i+1)%5][j][k]^1)&(self.state[(i+2)%5][j][k]))
		self.state = copy.deepcopy(tmp)
	
	def show(self):
		display = [[0 for i in range(5)] for i in range(5)]
		t_state = copy.deepcopy(self.state)
		for i in range(5):
			for j in  range(5):
				for k in range(16):
					t_state[i][j][k] = str(t_state[i][j][k])
		for j in range(5):
			for i in range(5):
				display[i][j] = hex(int(''.join(t_state[i][j]),2))
		for j in range(5):
			for i in range(5):
				print(f"{display[i][j]} ", end="")
			print("")
