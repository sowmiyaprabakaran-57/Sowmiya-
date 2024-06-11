1. Write a program to create a new string made of an input string’s first, middle, and last character. Eg: str1= ”PRADEEP” Output: PDP

def get_first_middle_last(input_str):
    length = len(input_str)
    middle_index = length // 2
    result = input_str[0] + input_str[middle_index] + input_str[-1]
    return result
str1 = "PRADEEP"
output = get_first_middle_last(str1)
print("Output:", output)

Output: PDP

2. Write a program to create a new string made of the middle three characters of an input string. Eg: str1= “PRADEEP”
Output: ADE

def get_middle_three(input_str):
    length = len(input_str)
    middle_index = length // 2
    result = input_str[middle_index - 1 : middle_index + 2]
    return result
str1 = "PRADEEP"
output = get_middle_three(str1)
print("Output:", output)

Output: ADE

3. Given two strings, str1 and str2. Write a program to create a new string str3 by appending str2 in the middle of str1. Eg: str1= ”STAR” str2= “SUPER” Output: STSUPERAR

def append_middle(str1, str2):
    middle_index = len(str1) // 2
    result = str1[:middle_index] + str2 + str1[middle_index:]
    return result
str1 = "STAR"
str2 = "SUPER"
output = append_middle(str1, str2)
print("Output:", output)

Output: STSUPERAR

4. Count all letters, digits, and special symbols from a given string str1 = "P@#yn26at^&i5ve" Outcome: Total counts of chars, digits, and symbols Chars = 8 Digits = 3 Symbol = 4

def count_chars_digits_symbols(input_str):
    chars = 0
    digits = 0
    symbols = 0
    for char in input_str:
        if char.isalpha():
            chars += 1
        elif char.isdigit():
            digits += 1
        else:
            symbols += 1
    return chars, digits, symbols
str1 = "P@#yn26at^&i5ve"
chars, digits, symbols = count_chars_digits_symbols(str1)
print("Total counts of chars, digits, and symbols:")
print("Chars =", chars)
print("Digits =", digits)
print("Symbols =", symbols)

Total counts of chars, digits, and symbols:
Chars = 8
Digits = 3
Symbols = 4

5.Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result. s1 = "Abc" s2 = "Xyz" Output: AzbycX

def create_new_string(s1, s2):
    result = ''
    len_s1 = len(s1)
    len_s2 = len(s2)
    i, j = 0, len_s2 - 1
    while i < len_s1 and j >= 0:
        result += s1[i] + s2[j]
        i += 1
        j -= 1
    while i < len_s1:
        result += s1[i]
        i += 1
    while j >= 0:
        result += s2[j]
        j -= 1
    return result
s1 = "Abc"
s2 = "Xyz"
output = create_new_string(s1, s2)
print("Output:", output)]

Output: AzbycX

6.Write a program to calculate Employee’s bonus calculation for the details given below Experience Bonus (%) More than 8 years 10 % More than 4 years 7% More than 2 years 4%

def calculate_bonus(experience):
    bonus_percentage = 0
    if experience > 8:
        bonus_percentage = 10
    elif experience > 4:
        bonus_percentage = 7
    elif experience > 2:
        bonus_percentage = 4
    return bonus_percentage
experience = float(input("Enter the number of years of experience: "))
bonus_percentage = calculate_bonus(experience)

if bonus_percentage:
    print("Employee's bonus percentage:", bonus_percentage, "%")
else:
    print("No bonus for this level of experience.")

Enter the number of years of experience: 6
Employee's bonus percentage: 7 %

7.Write a program to calculate the electricity bill (accept number of units from user) according to the following criteria:Units Price First 100 units No charge Next 100 units Rs.5 per unit After 200 units Rs.10 per unit

def calculate_electricity_bill(units):
    total_bill = 0
    if units <= 100:
        total_bill = 0
    elif units <= 200:
        total_bill = (units - 100) * 5
    else:
        total_bill = (100 * 5) + (units - 200) * 10
    return total_bill
units = float(input("Enter the number of units consumed: "))
bill_amount = calculate_electricity_bill(units)
print("Electricity bill amount: Rs.", bill_amount)


Enter the number of units consumed: 150
Electricity bill amount: Rs. 250.0

8.Accept the marked price from the user and calculate the Net amount as (Marked Price - Discount) to pay according to following criteria: Marked Price Discount

10000 20% 7000 and <=10000 15% <=7000 10%

def calculate_net_amount(marked_price):
    net_amount = 0
    if marked_price > 10000:
        net_amount = marked_price - (marked_price * 0.20)
    elif marked_price > 7000:
        net_amount = marked_price - (marked_price * 0.15)
    else:
        net_amount = marked_price - (marked_price * 0.10)
    return net_amount
marked_price = float(input("Enter the marked price: "))
net_amount = calculate_net_amount(marked_price)
print("Net amount to pay: Rs.", net_amount)

Enter the marked price: 5000
Net amount to pay: Rs. 4500.0
5. 
