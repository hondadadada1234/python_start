import sys

try:
  a = float(sys.argv[1])
  b = float(sys.argv[2])
  print(a+b)
except:
  print('error')

print('end')
