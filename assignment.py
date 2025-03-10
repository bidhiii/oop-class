def print_bidhi():
    # Loop through each row (5 rows total)
    for row in range(5):
        # Print each letter's corresponding row in the same line horizontally
        # B pattern
        if row == 0 or row == 1 or row == 4:
            print("*   *", end=" ")
        elif row == 2:
            print("*****", end=" ")
        elif row == 3:
            print("*   *", end=" ")
        
        # I pattern
        if row == 0 or row == 4:
            print("*****", end=" ")
        elif row == 1 or row == 2 or row == 3:
            print("  *  ", end=" ")
        
        # D pattern
        if row == 0 or row == 4:
            print("*****", end=" ")
        elif row == 1 or row == 2 or row == 3:
            print("*   *", end=" ")
        
        # H pattern
        if row == 0 or row == 4:
            print("*   *", end=" ")
        elif row == 2:
            print("*****", end=" ")
        else:
            print("*   *", end=" ")
        
        # I pattern (second I)
        if row == 0 or row == 4:
            print("*****", end=" ")
        elif row == 1 or row == 2 or row == 3:
            print("  *  ", end=" ")
        
        # Move to the next line after printing the row
        print()

# Call the function to print the pattern
print_bidhi()

#FACTORIAL
def factorial(n):   
    if n == 0 or n == 1:
        return 1    
    else:
        return n * factorial(n - 1)
    
number = 5
result = factorial(number)
print(result)

# #FIBONACCI SERIES
# def fibonacci(n):
#     fib_series = []
#     a, b = 0, 1
#     for _ in range(n):
#         fib_series.append(a)
#         a, b = b, a + b
#     return fib_series

# # Input
# n = int(input("Enter the value of n: "))

# # Output
# result = fibonacci(n)
# print("Fibonacci series:", ", ".join(map(str, result)))

#5
def find_pair_with_sum(nums, target):
    seen = set()   
    
    for num in nums:
        complement = target - num       
        
        if complement in seen:
            return [complement, num]        
        seen.add(num)    
    return None

nums = [2, 7, 11, 15]
target = 9
result = find_pair_with_sum(nums, target)

if result:
    print(f"Pair with sum {target}: {result}")
else:
    print(f"No pair found with sum {target}")

#PALINDROME
def is_palindrome_slicing(s):
   
    return s == s[::-1]

def is_palindrome_normal(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


input_string = "racecar"

is_palindrome_s = is_palindrome_slicing(input_string)
is_palindrome_n = is_palindrome_normal(input_string)

print(f"Palindrome check using string slicing: {is_palindrome_s}")
print(f"Palindrome check using normal loop: {is_palindrome_n}")
