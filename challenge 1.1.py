def factorial(n):
  if n < 0:
    print("Enter a valid number!")
  elif (n == 1 or n == 0):
    return 1
  else:
    return (n * factorial(n - 1))
num = int(input("Enter a number to find it's factorial: "))
print("Number : ", num)
print("Factorial : ", factorial(num))