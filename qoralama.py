# def sum1(x):
#     y = 0
#     while x > 0:
#         y += x%10
#         x = x//10
#     z = 0
#     while y > 0:
#         z += y%10
#         y = y//10
#     return z
# a = int(input())
# b = map(int,a.split())
# print(sum(b))

# def ekub(x,y):
#     for i in range(x+y//2,1,-1):
#         if x % i == 0 and y % i == 0:
#             return i
# x, y = map(int,input().split())
# print(ekub(x,y))

# a,b = map(int, input().split())
# def sum_1(a):
#     while True:
#         b = [int(i) for i in str(a)]
#         if len(str(sum(b))) >1:
#             a = sum(b)
#         else:
#             return sum(b)
# print(sum_1(a),sum_1(b))

# a, b = map(int, input().split())
# while a != 0 and b != 0:
#     if a>b:
#         a%=b
#     else:
#         b%=a
# print(a+b)
# from math import pi
# x,y,z =map(int, input().split())
# r1 = x**2*pi
# r2 = y**2*pi
# r3 = z**2*pi
# print(format(r1,".2f"), format(r2,".2f"),format(r3, ".2f"))