import random

# Some random positive numbers to test
m = random.randint(0, 500)
n = random.randint(0, 500)

# Save original m and n variables before algoritm start to change them
original_m = m
original_n = n

r = -1 # r will store the reminder of the division of m and n each time

found = False

while not found:
	if m < n: # Extra: Exchange variables when m < n
		m, n = n, m # Unlike other programming languages, Python is able to exchange variables this way
	
	r = m % n # Step 1. Find reminder
	
	if r == 0: # Step 2. If reminder is zero then we break the loop
		found = True
		break
	else: # Step 3. Reduce
		m = n
		n = r
		
		
print(f"The greatest common divisor of {original_m} and {original_n} is {n}")