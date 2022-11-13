# sujet A

def premier(n):
	if n > 1:
		for i in range(2, n):
			if n % i == 0 :
				return False
		return True		
	else:
		return False	

def superPremiere(n):
	q = n
	while(q != 0):
		if premier(q):
			q //= 10
		else:
			return False	
	return True

# ---------------------------------------------- #

print("saiser deux numero")

n = int(input("[n =  "))

m = int(input("m] = "))

while( n <= 4000 or n >= m or m > 10000):
	print("4000 < bi < bs <= 10000")
	n = int(input("[n =  "))
	m = int(input("m] = "))

for i in range(n, m+1):
	if superPremiere(i):
		print(i)



""" coded by zakaria akziz """