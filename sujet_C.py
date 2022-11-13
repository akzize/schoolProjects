"""------------ sujet C -----------------------------"""

# ------------------ functions ----------------------- #

def premier(n):
        for i in range(2, n // 2):
            if n % i == 0 :
                return False
        return True  

def premierCirculaire(n):
    if premier(n):
        test = str(n)
        digit = len(test)

        for i in range(digit - 1):
            test = test[-1] + test[:-1]
            if not premier(int(test)):
                return False
            else :
                test = test[-1] + test[:-1]   
    else:
        return False
    return True    
# ------------------ testing ----------------------- #

print("saiser deux numero")

bi = int(input("[bi =  "))

bs = int(input("bs] = "))

while( bi <= 10 or bi >= bs or bs > 10000):
    print("10 < bi < bs <= 500")
    bi = int(input("[bi =  "))
    bs = int(input("bs] = "))

for i in range(bi, bs+1):
	if premierCirculaire(i):
		print(i)
# _______________________________________________________________________________________________

""" coded by zakaria akziz """
