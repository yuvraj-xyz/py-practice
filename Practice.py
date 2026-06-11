# 39. Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    
    return n + sum(n-1)

n = int(input("Enter the Number: "))
print(sum(n))



# # 38. Write a python program using function to convert Celsius to Fahrenheit.

# def func(c):
#     f = (c*1.8) + 32
#     return f

# celc = int(input("Enter the temperature in Celcius: "))

# print(func(celc), "F")




# # 37. Write a program using functions to find greatest of three numbers.

# def greatest():
#     a = int(input("Enter first Number: "))
#     b = int(input("Enter second Number: "))
#     c = int(input("Enter third Number: "))

#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c
    
# print(greatest())





# # 36. Write a program to print multiplication table of n using for loops in reversed order.

# n = int(input("Enter the number: "))

# i = 10;
# while(i>0):
#     print(n*i)
#     i-=1;




# # 35. Write a program to print the following star pattern.
# # * * *
# # *   * for n = 3
# # * * *

# n = int(input("Enter the number: "))

# for i in range(1, n+1):
#     if(i%2!=0):
#         print("*" * (n), end="")

#     else:
#         print("*", end="")
#         print(" " * (n-2), end="")
#         print("*", end="")

#     print("")




# # 34. Write a program to print the following star pattern:
# # *
# # **
# # *** for n = 3

# n = int(input("Enter the number: "))

# for i in range(1, n+1):
#     print("*" * (i), end="")
#     print("")



# # 33. Write a program to print the following star pattern.
# #   *
# #  ***
# # ***** for n = 3

# n = int(input("Enter the number: "))

# for i in range(1, n+1):
#     print(" " * (n-i), end="")
#     print("*" * (2*i-1), end="")
#     print("")



# # 32. Write a program to calculate the factorial of a given number using for loop.

# num = int(input("Enter Your Number: "))

# fact = 1
# for i in range(1, num+1):
#     fact*=i

# print(fact)



# # 31. Write a program to find the sum of first n natural numbers using while loop

# num = int(input("Enter the number: "))

# sum=0
# i=1
# while(i<=num):
#     sum+=i
#     i+=1

# print(sum)



# # 30. Write a program to find whether a given number is prime or not

# num = int(input("Enter your number: "))

# for i in range(2, int(num/2)+1):
#     if(num%i==0):
#         print("Not a Prime Number!")
#         break;

# else:
#     print("Prime No. found!")



# # 29. Attempt problem 27 using while loop.

# inp = input("Enter the Number: ")

# num = int(inp)

# i=1
# while(i<11):

#     print(i*num)
#     i+=1


# # 28. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# name = input("Enter your name: ")

# for i in range(0, len(l)):
#     if(name==l[i] and l[i][0]=="S"):
#         print("Hey, Nice to meet you!")


# # 27. Write a program to print multiplication table of a given number using for loop

# inp = input("Enter the Number: ")

# num = int(inp)

# for i in range(1, 11):

#     print(i*num)



# # 26. Write a program to calculate the grade of a student from his marks from the following
# # scheme:
# # 90 – 100 => S+
# # 80 – 90 => A
# # 70 – 80 => B
# # 60 – 70 => C
# # 50 – 60 => D
# # <50 => F

# x = input("Enter your marks: ")
# marks = int(x)

# if(marks>=90):
#     print("You got a S+")
# elif(marks>=80 and marks<90):
#     print("You got a A")
# elif(marks>=70 and marks<80):
#     print("You got a B")
# elif(marks>=60 and marks<70):
#     print("You got a C")
# elif(marks>=50 and marks<60):
#     print("You got a D")
# elif(marks<50):
#     print("You got a F")





# # 25. Write a program which finds out whether a given name is present in a list or not

# li = ["Yuvraj", "Paliwal"]

# name = input("Type the name to find it: ")

# for i in range (0, len(li)):
#     if(li[i]==name):
#         print("Found it!!!")
#         break

#     if(i == len(li)-1 and li[i]!=name):
#         print("Name doen't exist in the list.")



# # 24. Write a program to find whether a given username contains less than 10 characters or not

# username = input("Enter your username: ")


# if(len(username)<=10):
#     print("Yes, Its less than or equal to 10")

# else:
#     print("NO, Its more than 10")




# # 23. A spam comment is defined as a text containing following keywords: “Make a lot of
# # money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams

# keywords = [
#     "Make a lot of money",
#     "buy now",
#     "subscribe this",
#     "click this"
# ]

# comment = input("Enter your comment: ")

# for i in range (0, len(keywords)):
#     if (comment == keywords[i]):
#         print("This is Spam!!!!!")
#         break

#     if(i==len(keywords)-1):
#         print ("All Good!!!")


# # 22. Write a program to find out whether a student has passed or failed if it requires a total of
# # 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# # input from the user.

# # Assuming Each exam is of 100 Marks

# total_marks = 0
# x = 0

# for i in range(1,4):
#     n = input(f"Enter Marks of Subject {i} : ")
#     marks = int(n)

#     total_marks += marks
#     total_marks_percent = round((total_marks*100)/300, 1)

#     if(marks>=33):
#         x = x+1

#         if(i==3):
#             if(x==3 and total_marks_percent >=40):
#                 print("Congratulations, You have Passed the exam!")
#                 print("Total Marks :", total_marks, "\nTotal Marks Percentage :", total_marks_percent, "%", f"\nYou Passed in {x} out of 3 Subjects")
#                 break

#             else:
#                 print("You have Failed the Exam!")
#                 print("Total Marks :", total_marks, "\nTotal Marks Percentage :", total_marks_percent, "%", f"\nYou Passed in {x} out of 3 Subjects")
#                 break





# # 21. Write a program to find the greatest of four numbers entered by the user.

# greatest = 0;
# for i in range(1,5):
#     n = input(f"{i} Enter the Number :")
#     num = (int(n))

#     if(num>greatest):
#         greatest = num

# print(greatest)




# # 20. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# # use key as their names. Assume that the names are unique.

# dict = {}

# for i in range (0, 4):
#     dict.update({(input("Enter Your Name : ")):input("Enter Your Favorite Language : ")})

# print(dict)



# # 19. What will be the length of following set s:

# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

# print(s, len(s))



# # 18. Can we have a set with 18 (int) and '18' (str) as a value in it?

# s = {18, "18"}

# print(s, type(s))


# # 17. Write a program to input eight numbers from the user and display all the unique numbers
# # (once).

# s = set()

# for i in range (0,8):
#     n= input("Please Enter a Number : ")
#     s.add(int(n))

# print(s)


# # 16. Write a program to create a dictionary of Hindi words with values as their English
# # translation. Provide user with an option to look it up!

# language = {
#     "Thanda":"Cool",
#     "Zameen":"Ground",
#     "Ambar":"Sky",
#     "Garam":"Hot"
# }

# key = input("Please Enter one of these - Thanda/Garam/Zameen/Ambar :")

# print(language[key])



# # 15. Write a program to count the number of zeros in the following tuple:

# a = (7, 0, 8, 0, 0, 9)

# print(a.count(0))



# # 14. Write a program to sum a list with 4 numbers.

# num = [1, 22, 13, 10]

# # new_num = 0
# # for i in range(0, 4):
# #     new_num += num[i]

# # print(new_num)

# print(sum(num))


# # 13. Check that a tuple type cannot be changed in python.

# num = (1, 2, 33, 11)

# num[2] = 22

# print(num)


# # 12. Write a program to accept marks of 6 students and display them in a sorted manner.
# marks = []

# for i in range (1,8):
#     mark = input(f"Enter Student marks {i}:")
#     marks.append(mark)

# marks.sort()

# print(marks)



# # 11. Write a program to store seven fruits in a list entered by the user.

# fruits = []

# for i in range (1,8):
#     fruit = input(f"Name fruit {i}:")
#     fruits.append(fruit)

# print fruits()


# # 10. Write a program to format the following letter using escape sequence characters

# letter = "Hey, I am Yuvraj"

# print("Hey,\nI am \"Yuvraj\"")


# # 9. Write a program to detect double space in a string and Replace the double space  with single spaces.


# str = "Double  Trouble"

# rep = str.replace("  ", " ")

# print(rep)


# # 8.  Write a program to fill in a letter template given below with name and date.

# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
# print(letter.replace("<|Name|>", input("Enter ur name : ")).replace("<|Date|>", "11 June" ))


# # 7. Write a python program to display a user entered name followed by Good Afternoon using
# # input() function

# Name = input("Enter your name ")
# print("Good Morning,", Name)




# # 6. Write a python program to calculate the square of a number entered by the user.

# num = int(input("Enter the number : "))

# print(num*num)


# # 5. Write a python program to find an average of two numbers entered by the user.

# a = 22
# b = 10

# print((a+b)/2)

# print("The remainder of a divided by b is ", a%b)


# # 4. Use comparison operator to find out whether ‘a’ given variable is greater than ‘b’ or not.
# # Take a = 34 and b = 80

# a = 34
# b = 80
# print(a>b)


# # 3. Check the type of variable assigned using input() function.

# a = input("Enter something ")
# print("The type of a is ", type(a))


# # 2. Write a python program to add two numbers.

# # a = int(input("Enter Number 1 "))
# # b = int(input("Enter Number 2 "))
# a = 43
# b = 5


# # 1. Write a python program to add two numbers.

# # a = int(input("Enter Number 1 "))
# # b = int(input("Enter Number 2 "))
# a = 10
# b = 20

# print("The sum of a and b is ", a+b)