'''import sys

print('the command line arguments are: ')
for i in sys.argv:
  print(i)
  
print('---------------------')

print('\nThe pythonpath is', sys.path, '\n')'''

if __name__ == '__main__':
  print('the program is running by itself')
  
else:
  print('The program is running form a module')