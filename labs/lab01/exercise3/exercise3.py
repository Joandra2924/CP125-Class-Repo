# Lab 01 Exercise 3: Secure Vault System
# Write your code below:

def validate_entry(name, pin):
   if name == "Director" and pin == 1122:
      return True
   elif name == "Security" and pin == 9900:
      return True
   else:
      return False

# Test your code here
print("Testing Secure Vault System...")
print(validate_entry("Director", 1122))
print(validate_entry("Director", 9900))
print(validate_entry("director", 1122))