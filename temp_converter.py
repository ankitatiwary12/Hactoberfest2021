print(" Enter 0 to convert Celsius to Farhenheit! ") 
print(" Enter 1 to convert Farhenheit to Celsius! ") 
x=(int(input()))

if x==0:
  print(" enter the temperature in Celsius : ") 
  c=(float(input()))
  print(" The temperature in Farhenheit is : ") 
  f = (9*c)/5 + 32
  print(" ", f)

elif x==1:
  print(" enter the temperature in Farhenheit : ")
  f=(float(input()))
  print(" The temperature in Celsius is : ")
  c = (f-32) * 5/9
  print(" ", c)

else:
  print(" Invalid Choice ")
