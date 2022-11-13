
"""------------------ sujet B ------------------"""

# --------------- functions --------------------
def propre(n):
    d = n % 10
    return n * d


def reverse(n):
    num = n
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num  


# ------------ test -------------------
n = int(input("saiser votre numero : "))

if propre(n) == reverse(n) and reverse(n) == n:
    print(n, "est symetrique et propre")
elif propre(n) == n:
    print(n, "est propre")  
elif reverse(n) == n :
    print(n, "est symetrique")
else:
    print(n, "nether symetrique nor propre")



# _______________________________________________________________________________________________

""" coded by zakaria akziz """