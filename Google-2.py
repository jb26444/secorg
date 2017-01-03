import sys

def Hel(name):
  name = name + '!!!!!'
  print 'hello' + name

def he():
  print Hel(sys.argv[1])


if __name__ == '__main__':
 he()

