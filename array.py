
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
