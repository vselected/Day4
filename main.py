# # Methods and the Python Documentation
# my_list = [1,2,3]
# my_list.append(4)
# print(my_list)
# my_list.pop()
# print(my_list)

# # Introduction to Functions
# def say_hello():
#     name = input("What's your name? ")
#     print("Hello {}".format(name))
#
# say_hello()

# def add_num(num1, num2):
#     return num1+num2
#
# result = add_num(2,10)
# print(result)
#
# def sum_numbers(num1, num2):
#     return num1+num2
# print(sum_numbers("10","20"))

# # Logic with Python Functions
# def even_check(number):
#
#     return number % 2 == 0
#
# print(even_check(4))
# print(even_check(7))

# #Return true if any number is even inside a list
# def check_even_list(num_list):
#     #return all the even numbers in a list
#
#     #placeholder variables
#     even_numbers = []
#
#     for number in num_list:
#         if number % 2 == 0:
#             even_numbers.append(number)
#         else:
#             pass
#
#     return even_numbers
#
# print(check_even_list([3,2,5,4,9,778,4532]))

# stock_prices = [("APPL", 200), ("GOOG", 400), ("MSFT", 100)]
#
# for item in stock_prices:
#     print(item)
#
# for ticker,price in stock_prices:
#     print(ticker)

work_hours = [("Abby",100), ("Billy",400), ("Cassie",900)]
def employee_check(work_hours):

    #Placeholders
    current_max = 0
    employee_of_month = ""

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    #Return
    return(employee_of_month,current_max)

name,hours = employee_check(work_hours)
print(name)