# use this for loop to execute the result in the following manner
# 011222
for i in range(0,3):
    for j in range(0,3):
        print(i)

# use this for loop to execute the result in the following manner
# 000111222
for i in range(0,3):
    for j in range(0,3):
        print(i, end='')

# use this for loop to execute the result in the following manner
# *
# * *
# * * *
for i in range(0,3):
    for j in range(0,i+1):
        print('*', end=' ')
    print('\n')

# use this for loop to execute the result in the following manner
#    *
#   ***
#  *****
for i in range(1, 4):
    for j in range(i, 4):
        print(" ", end='')
    for k in range(0, i):
        print('*', end='')
    for m in range(1, i):
        print('*', end='')
    print('\n')
