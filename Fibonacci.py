# x and y are the two starter numbers and the ones that will be added
x = 1
y = 1
z = 2
n = 0

#u_num is the number of times to perform the sequence
u_num = 0

#taking the input:
u = input("How much of the Fibonacci sequence would you like to see? \n")

while True:
    try:
        u_num = int(u) # this code makes sure that the person is entering an integer
        break
    except ValueError:
        u = input('Please enter an integer for the number of Fibonacci to generate \n') 


print("1 : 0")# this might change
print("2 : 1")


while (z < u_num): 
    n = x + y # this makes the Fibonacci principle work on X and Y
    x = y
    y = n 
    z = z + 1 # this makes sure that z will reach u_num so everything works
    
    print("")

    print(z , ":",  n) # this prints the next number in the sequence. 

    
    

