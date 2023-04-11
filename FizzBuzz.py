num1 = int(input("Ingresa el primer numero: "))

def FizzBuzz(num1):
    if num1 % 3 == 0 and num1 % 5 == 0:
        return 'FizzBuzz'
    elif num1 % 3 == 0:
        return 'Fizz' 
    elif num1 % 5 == 0:
        return 'Buzz'
    else:
      return num1
  
print(FizzBuzz(num1))  





