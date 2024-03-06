# 1. Large Power

def is_power_greater_than_5000(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False

# Test the function
print(is_power_greater_than_5000(10, 3))  
print(is_power_greater_than_5000(2, 10))  
print(is_power_greater_than_5000(3, 5))   



# CODING QUESTION

def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False

print(large_power(10, 3))  
print(large_power(2, 10))  
print(large_power(3, 5))   


# 2. Divide by Ten

def is_divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False

# Test the function
print(is_divisible_by_ten(20))   
print(is_divisible_by_ten(15))   
print(is_divisible_by_ten(100))  
print(is_divisible_by_ten(7))  


# CODING QUESTION

def divisible_by_ten(num):
    return num % 10 == 0

print(divisible_by_ten(20))   
print(divisible_by_ten(15))   
print(divisible_by_ten(100))  
print(divisible_by_ten(7))    