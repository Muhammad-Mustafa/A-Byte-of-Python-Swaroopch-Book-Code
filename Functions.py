'''
def say_hello():
  print('hello world')
  
say_hello()
say_hello()
'''

#Find the Maximum Number

def max_number(num1, num2):
  if(num1 < num2):
    print(num2, ' is max number') 
  elif (num1 == num2):
    print('Both numbers are equal') 
  else:
    print(num1, 'is max number')

a = 12
b = 33

max_number(a,b)