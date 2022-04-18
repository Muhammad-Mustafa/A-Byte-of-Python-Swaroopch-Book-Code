# if/else statements
'''
if True:
  print('True')

number = 23
running  = True

while running == True:
  
  guess = int(input('Enter an integer : '))

  if guess == number:
    #New block start here
    print('Congratulations you guessed it !')
    running = False
    #Block ends here
  elif guess < number:
    #Another block start here
    print('Its a little higher than that')
    #block ends here
  else:
    #block starts here
    print('No its a little lower than that')
  
print('done')
'''

'''
for i in range(1,5):
  print(i)
'''
'''
while True:
  s = input('Enter anything: ')
  if s == 'quite':
    break
  print('the length of the string is: ', len(s))

print('done')
'''