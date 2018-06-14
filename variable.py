# we don't declare variable in python. Directly initialise the value of
# variable. e.g. String, integer etc.
a = 'Hello World'
int = 2
int = 2+1 

c = 35

# use %d to tell the compiler to print the result from an integer variable.
# if there are more than 2 variable values to be displayed, make sure they
# are inside brackets () separated by comma (,)
print ('Hello students, welcome to first program'
       + '\n' +
       a + '%d\n%d' %(int, c))
