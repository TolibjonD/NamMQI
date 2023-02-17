import math
startText = "----------------------------Answer---------------------------------\n"
finishText = "----------------------Run time finished---------------------------\n"
# =========== the beginning of 1-task ==========
# ------------ 1.1-task ---------
# 22.Aylana uzunligi l berilgan. Bu aylananing radiusini va aylana chegaralagan doiraning yuzasini hisoblash dasturi tuzilsin. pi=3,14 ga teng deb olinsin.
#Road map:
          # R = l/2*3.14
          # S = 3.14*R*R
#Implemention: ↷
l = int(input("l>> "))
R = l/2*3.14
S = 3.14*R*R
print(startText)
print("R>> ", R)
print("L>> ", S, "\n")
print(finishText)

# # ----------- 1.2-task ----------
# # 22.Sonlаr koordinаtа o’qidа uchtа nuqtа berilgаn А, B, C. АC vа BC kesmаlаri uzunliklаri vа ulаr yig’indisini toping.
# # Road Map:
#            # AC = math.sqrt( math.pow((Ax-Cx, 2)) + math.pow((Ay-Cy), 2) )
# # #Implemention: ↷
# Ax = int(input("Ax [ A(x,y) ]>> "))
# Ay = int(input("Ay [ A(x,y) ]>> "))
# Bx = int(input("Bx [ B(x,y) ]>> "))
# By = int(input("By [ B(x,y) ]>> "))
# Cx = int(input("Cx [ C(x,y) ]>> "))
# Cy = int(input("Cy [ C(x,y) ]>> "))
# AC = math.sqrt( math.pow((Ax-Cx), 2) + math.pow((Ay-Cy), 2) )
# BC = math.sqrt( math.pow((Bx-Cx), 2) + math.pow((By-Cy), 2) )
# total = AC+BC
# print(startText)
# print("AC>> ", AC)
# print("BC>> ", BC)
# print("Total>> ", total, "\n")
# print(finishText)

# # =========== the ending of 1-task ==========

## ---------------------------------------------------------------------------------------------------- >

# #  =========== the beginning of 2-task ==========
# #  ----------- 2.1-task -------------
# # 22. x, y sonlari berilgan. Ularni tekislikdagi nuqta koordinatalari deb hisoblab, shu nuqtaning 2-chorakda yotishi aniqlansin.
# # Road map:
#            # Cordinate axis and quarters:
#            #----------------------------------
#            #             y                   |
#            #             ↑                   |
#            #             |                   |
#            #        2    |   1               |
#            #             |                   |
#            #    -------------------> x       |
#            #             |                   |
#            #             |                   |
#            #        3    |   4               |
#            #             |                   |
#            #                                 |
#            #----------------------------------
# # #Implemention: ↷
# x = int(input("x>> "))
# y = int(input("y>> "))

# pattern = """
#                          y                   
#                          ↑                   
#                          |                   
#                     2    |   1               
#                          |                   
#                 -------------------> x       
#                          |                   
#                          |                   
#                     3    |   4               
#                          |  
# """
# print(pattern)
# if x<0 and y>0:
#     print("The point lies in the third quadrant")
# else:
#     print("The point does not lie in the third quadrant")

# # ---- 2.2-task ----
# # 22.	Hаqiqiy X (|X|<1) vа butun N>0 sonlаri berilgаn. Ifodа qiymаtini toping.                   
# # 1-X2/(2!)+X4/(4!)-.....+(-1) N*X2*N+1/((2* N)!)
# #Implemention: ↷
# # first of all I find factorial by the bellow function
# def fack(n):
#     f = 1
#     for i in range(1, n+1):
#         f = f*i
#         return f
# N = int(input("N>> "))
# X = float(input("X>> "))
# if N>0:
#     s = ( math.pow(-1, N) * math.pow(X, (2*N+1)) )  / fack(2*N)
#     print(startText)
#     print("Sum>>  ", s, "\n")
#     print(finishText)
# else:
#     print("Warning ... Please enter a postive number for N !...")

# # =========== the ending of 2-task ==========

## ------------------------------------------------------------------------------------------- >

# # =========== the beginning of 3-task ==========
# # ---- 3.1-task ------------
# # 22. 2.5*x*x + math.sin(4/x)
# #Implemention: ↷
# x = int(input("x>> "))
# y = 2.5*x*x + math.sin(4/x)
# print(startText)
# print("Answer>> ", y, "\n")
# print(finishText)

# # -------- 3.2-task -----------
# # 22. 2 ta satr berilgan. Ikkinchi satrdan birinchi satr bilan ustma-ust tushuvchi 1-qism satr o‘chirilsin. Agar ikkinchi satrda birinchi satr topilmasa  satr o‘zgarishsiz chop etilsin.
# #Implemention: ↷
# text1=input("text-1>>  ").lower()
# text2=input("text-2>>  ").lower()
# text1 = text1.split(" ")
# text2 = text2.split(" ")
# for text in text1:
#     if text in text2:
#         text2.remove(text)
# text2 = " ".join(map(str, text2))
# print(startText)
# print("Answer:  ", text2, "\n")
# print(finishText)