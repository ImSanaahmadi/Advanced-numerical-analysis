import math

# Initial value
E = math.exp(-1)

# Number of decimal places
digits = 6

# Calculate E_n for n from 1 to 9
for n in range(1, 10):
    print(f"E{n} = {E:.{digits}f}")
   
    # Calculate E_n using the recursive formula
    E_next = 1 - (n + 1) * E
   
    # If E_next is negative, set it to zero
    if E_next < 0:
        E_next = 0
   
    # Update E for the next iteration
    E = E_next