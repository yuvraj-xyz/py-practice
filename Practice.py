




# 20. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# use key as their names. Assume that the names are unique.

dict = {}

for i in range (0, 4):
    dict.update({(input("Enter Your Name : ")):input("Enter Your Favorite Language : ")})

print(dict)



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
#     s.add(input("Please Enter a Number : "))

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