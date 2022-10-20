# functions in use
# def number_digits(num):
#     digit = 0
#     Q = num
#     while Q != 0:
#         Q //= 10
#         digit += 1
#     return digit    

# sujet 1

# n = int(input("nombre n : "))
# m = int(input("nombre m : "))
# digit = 4
# test = False


# for k in range(n,m+1):
#     Q = k
#     test = False
#     for i in range(digit):
#         for j in range(2,Q // 2):
#             if Q % j == 0:
#                 test = True
#                 break
#         if test: 
#             break
#         Q //= 10

#     if  test==False:
#         print(k)    
    

# for k in range(n,m+1):
#     Q = k
#     test = False
#     for i in range(digit):
            
#         for j in range(2,Q // 2):
#             if Q % j == 0:
#                 test = True
#                 break
#         if test: 
#             break
#     if not test: 
#         print(Q)
#         Q //= 10

# else:
#     print("votre nombre doit etre entre 4000 et 10000")                

# ex 4

# n = int(input("donner n : "))
# a = int(input("u0 : "))
# u = a
# us = 0
# for i in range(n):
#     if u % 2:
#         us = 3 * u + 1
        
#     else:
#         us = u / 2
#     u = us
#     print(u)

# print("u",n," = ",us) 

# =============================================================================================================================
# ex1
"""
un entier distinc
12345 ==> distinct
12434 ==> non
"""
# n = input("you're number : ")
# l = len(n)
# n = int(n)
# Q = n
# loop for iteration and checking
# for i in range(l):
#     d = Q % 10
#     c = 1
#     for j in range(l):
#         if d == j:
#             c+=1
#     if c > 1:
#         print("this number is not \"distict\" ")
#         break
# if c == 1:
#     print("disrict")
# else:
#     print("not distinct")    

# ==============================================================================================================================================
# ex2
"""
les entiers positifs de trois chiffres de la forme cdu
cdu ==> c*d*u % c+d+u = 0
"""

"""==> in order to use while to get digits you can plan play with strings func and list "just to keep in mind\"
    maybe it will safe or decrease some lines .. (:
"""
# get number from the user
# n = int(input("your number : "))

# num = n
# for i in range(500,520):
#     c_m = 1
#     c_a = 0
#     num = i

    # while num != 0:
    #     d = num % 10
    #     c_a += d
    #     c_m *= d
    #     num //= 10
    # if not c_m % c_a:    
    #     print(i,"est un cdu")

# ===============================================================================================================================================
# ex3
"""reverse number"""

# n = int(input("num = "))
# Q = n
# c = 0
# while(Q != 0):
#     d = Q % 10
#     c += 1
#     Q //=10
# Q = n  
# rn = 0  
# for i in range(c-1,-1,-1):
#     d = Q % 10
#     rn += d*10**i
#     Q //=10

# print(rn)  

# ==========================================================================================================================
# ex4

""" 
un programme Python qui permet de déterminer si un entier N de quatre chiffres vérifie la relation suivante
N=somme des puissance Kème de ses chiffres, avec 1<=K<=5
"""
""" the same here you can play with strings converting and vice versa"""
# num = int(input("votre numbere : "))

# Q = num
# digit = 0
# while Q != 0:
#     Q //= 10
#     digit += 1

    # ==> by using fun

# digit = number_digits(num)

# for j in range(digit):
#     Q = num
#     snum = 0
#     for i in range(digit):
#         d = Q % 10
#         snum += d**(j+1)
#         Q //=10
#     if num == snum:
#         print("n= ",num,"et K=",j+1)  
#         break  
# ==========================================================================================================================
#  ex5
"""Super premiere"""




# ==========================================================================================================================
# ex6
"""
palindrome
rep-degit
11111 rep-digit
1112 not
"""

# def rep_number(num):
#     f = True
#     Q = num
#     d = Q % 10
#     Q //= 10
#     while Q != 0:
#         d1 = Q % 10
#         Q //= 10
#         if d1 != d:
#             f = False
#             break
#         # else:
#         #     Q //= 10
#     return f    
# n = int(input("your number : "))
# b = rep_number(n)
# if b:
#     print("rep")
# else:
#     print("not rep")
# ==========================================================================================================================
# ex7
"""palindrome"""
# inverse
# n = int(input("your number : "))
# Q = n
# digit = 3
# nv = 0
# while Q != 0:
#     d =Q % 10
#     Q //= 10
#     nv += d*(10**digit)
#     digit -= 1

# if nv == n:
#     print("palindrome")
# else:
#     print("not palindrome")    

# ==========================================================================================================================
# ex7
"""
to print this patter or diagram
  B 
  B 
  B C 
A B C 
A B C 
"""
#                                                                
# ============================================================================

# ============================================================================

# ============================================================================

# ============================================================================

# ============================================================================

# ============================================================================

# ============================================================================

# ============================================================================

# ============================================================================

# ============================================================================

# ============================================================================

# ============================================================================

# ============================================================================

# ============================================================================

