##exrcise 1.5
# salary = int(input("Enter salary: "))
# precentge = float(input("Enter presantage: "))
# print("current salary is:",salary*precentge)

# #exrecise 1.6
# R = float(input("Enter R: "))
# PI = 3.141
# print("P: ",R*2*PI,"\t","S: ", R*R*PI)

# #exresice 2.1
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# city = input("Enter your city: ")
# print("your name is:",name,"\nyour age is:",age,"\nyour city is:",city)

# #exrecise 2.2
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# city = input("Enter your city: ")
# print("your name is %s, your age is %d, your city is %s" %(name,age,city))

# #exrecise 2.3 ******** need guidence here
# all_info = input("Enter all your address info: ")
# print(all_info.split(" "))
# print(all_info[slice(13)])

# #exrecise 2.4 ************* need guidence here
# string = input("enter a string: ")
# print(len(string))
# print(string[2:7])
# print(string.split(" ")[0]*3)
# print(str.title(string))

# exercise 3.1
# # exercise 1
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# if (num1+num2)%2==0:
#     print("very good")
# else:
#     print("no good at all")

# # exercise 3.2
# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# num3 = int(input("enter a number: "))
# if num1 > num2 and num1 > num3:
#     print(num1)
# elif num2 > num1 and num2 > num3:
#     print(num2)
# else:
#     print(num3)

# # exercise 3.3
# num_comp = input("enter a number: ")
# if num_comp == "":
#     num_comp = 15
# print("the number of computers you will need to fix is:",int(num_comp) * 2)

# exercise 4.1

# num1 = int(input("enter a number: "))
# num2 = int(input("enter a number: "))
# for i in range(num1,num2):
#     if i % 2 == 0:
#         print(i)

# # exercise 4.2
# num = int(input("enter a number: "))
# for i in range(2,num):
#     if num % i == 0:
#         print("ths is not a primary number")
#         break
#     else:
#         print("this is a primary number")
#         break

# # # exercise 4.3
# import random
# n = random.randint(1, 9)
# num = 0
# while n != num:
#     n = random.randint(1, 9)
#     num = int(input("enter a number: "))
#     if n > num:
#         print("the number tou guessed is lower")
#     elif n < num:
#         print("the number you guessed is higher")
#     elif n == num:
#         print("you guessed the right number!!!")
#         break

# exersice 4.4

# import random
# num = 1
# ran = 0
# count = 0
# while num != ran:
#     num = int(input("enter a number between 1-100: "))
#     ran = n = random.randint(1,100)
#     if num > ran:
#         massage = input("write higher: ")
#         count += 1
#     elif num < ran:
#         massage = input("write lower: ")
#         count += 1
#     elif num == ran:
#         massage = input("write exactly: ")
#         break
# print("counts until the exact number:",count)

# # exercise 4.5
# nterms = int(input("How many terms? "))
# n1, n2 = 0, 1
# count = 0
# print("Fibonacci sequence:")
# while count < nterms:
#     print(n1)
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
#     count += 1

# # exercise 4.6
# string = input("enter a string: ")
# char = input("enter a char: ")
# count = 0
# for i in string:
#     if i == char:
#         count += 1
# print(count)

