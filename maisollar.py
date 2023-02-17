import math
## ** 1-misol **
# a = int(input("Enter a>> "))
# P = 4*a
# print("P = ", P)

## ** 2-misol ** 
# a = int(input("Enter a>> "))    
# S = math.pow(a,2)
# print("S = ", S)

## ** 3-misol **
# a = int(input("Enter a>> "))   
# b = int(input("Enter b>> "))
# S = a*b
# P = 2*(a+b)
# print("S= ", S)
# print("P= ", P)

## ** 4-misol **
# d = int(input("Enter d>> "))  
# L= math.pi * d
# print("L= ", L)

## 5-misol
# a = int(input("Enter a>> "))
# V = math.pow(a, 3)
# S = 6*a*a
# print("V= ", V)
# print("S= ", S)

##6-mislol
# a = int(input("Enter a>> "))  
# b = int(input("Enter b>> "))  
# c = int(input("Enter c>> "))  
# V = a*b*c
# S = 2*(a*b + b*c + a*c)
# print("V= ", V)
# print("S= ", S)

##7-misol
# R = int(input("Enter R>> "))  
# L = 2*math.pi*R
# S = math.pi*R*R
# print("L= ", L)
# print("S= ", S)

##8-misol
# a = int(input("Enter a>> "))  
# b = int(input("Enter b>> "))
# c = (a+b)/2
# print("Solved: ", c)  

##9-misol
# a = int(input("Enter a>> "))
# b = int(input("Enter b>> "))
# if a>0 | b>0:
#     c=(a*b)*1/2
#     print("Solved: ", c)
# else:
#     print("Musbat son kiriting !...")

##10-misol
# def add(a,b):
#     print(a+b)
# def mul(a,b):
#     print(a*b)
# def kv(a,b):
#     print(f"a2= {a*a}, b2={b*b}")
# add(2,21)
# mul(2,21)
# kv(2,21)

# ======= 1-amaliy ish =============================================
# # 22.Aylana uzunligi l berilgan. Bu aylananing radiusini va aylana chegaralagan doiraning yuzasini hisoblash dasturi tuzilsin.pi =3,14 ga teng deb olinsin.

# l = int(input("Enter the length of circle>> "))
# # l = pi*2R
# R = (l)/2*math.pi
# S = math.pi * R*R
# print("Radius:  ", R)
# print("Area:  ", S)

# ============== the end of first task =======================

# ================ 2-Amaliy ish ==============================
# 22.	x, y sonlari berilgan. Ularni tekislikdagi nuqta koordinatalari deb hisoblab, shu nuqtaning 2-chorakda yotishi aniqlansin

#   coordinate and quarters
#            y
#            |
#            |
#       2    |   1
#            |
# <---------------------> x
#            |
#      3     |   4
#            |

# x = int(input("x>> "))
# y = int(input("y>> "))
# if x>0 and y>0:
#     print("1-quarter")
# elif x<0 and y>0:
#     print("2-quarter")
# elif x<0 and y<0:
#     print("3-quarter")
# elif x>0 and y<0:
#     print("4-quarter")
# else:
#     print("0")

# ========= the ending of 2-task ==============

# ========== 3-task ===========================
x = int(input("x>> "))
y = 2.5*math.sqrt(math.pow(x,4)) + math.sin(4/x)
print("y:  ", y)
