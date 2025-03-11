for row in range(7): #B
    for col in range(5):
        if (col==0 or col==4) or (row==0 or row==3 or row==6) and (col>0 and col<4):
            print("*", end="")
        else:
            print(end=" ")
    print()


for row in range(6): #I
    for col in range(5):
        if (col==0):
            print("*", end="")
        else:
            print(en d=" ")
    print()    


for row in range(7): #D
  for col in range(5):
    if (col==0 or col==4) and (row!=0 or row!=6)or ((row==0 or row==6)and (col>0 and col<4)):
      print("*",end="")
    else:
      print(end=" ")
  print()

    
for row in range(7): #H
    for col in range(5):
        if (col==0 or col==4) or (row==3 and (col>0 and col<4)):
            print("*", end="")
        else:
            print(end=" ")
    print()


for row in range(6): #I
    for col in range(5):
        if (col==0):
            print("*", end="")
        else:
            print(end=" ")
    print()


    







# 5
# def find_pair_with_sum(nums, target):
#     seen = set()   
    
#     for num in nums:
#         complement = target - num       
        
#         if complement in seen:
#             return [complement, num]        
#         seen.add(num)    
#     return None

# nums = [2, 7, 11, 15]
# target = 9
# result = find_pair_with_sum(nums, target)

# if result:
#     print(f"Pair with sum {target}: {result}")
# else:
#     print(f"No pair found with sum {target}")

# #PALINDROME
# def is_palindrome_slicing(s):
   
#     return s == s[::-1]

# def is_palindrome_normal(s):
#     left, right = 0, len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
#     return True


# input_string = "racecar"

# is_palindrome_s = is_palindrome_slicing(input_string)
# is_palindrome_n = is_palindrome_normal(input_string)

# print(f"Palindrome check using string slicing: {is_palindrome_s}")
# print(f"Palindrome check using normal loop: {is_palindrome_n}")
