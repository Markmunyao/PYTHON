def large_power(base, exponent):
    result= base**exponent
    if result>5000:
        return True
    else:
        return False

print(large_power(10,3))
print(large_power(3,3))

def divisible_10(num):
    remainder = num % 10
    if remainder==0:
        return True
    else:
        return False
print(divisible_10(341)) 
print(divisible_10(10))

def rich_enough(salary,month):
    income= salary*month
    if income>200000:
        return True
    else:
        return False
print(rich_enough(30000,12))
print(rich_enough(15000,12))    
       
    

 
