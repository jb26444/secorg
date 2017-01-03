a = 6       ## set a variable in this interpreter session
a           ## entering an expression prints its value
6
a + 2
8
a = 'hi'    ## 'a' can hold a string just as well
a
'hi'
len(a)      ## call the len() function on a string
2
a + len(a)  ## try something that doesn't work
Traceback (most recent call last):
  File "", line 1, in 
TypeError: cannot concatenate 'str' and 'int' objects
a + str(len(a))  ## probably what you really wanted
'hi2'
foo         ## try something else that doesn't work
Traceback (most recent call last):
  File "", line 1, in 
NameError: name 'foo' is not defined
^D          ## type CTRL-d to exit (CTRL-z in Windows/DOS terminal)
