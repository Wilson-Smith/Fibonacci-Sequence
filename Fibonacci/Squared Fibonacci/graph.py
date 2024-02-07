# importing the required module 
import matplotlib.pyplot as plt 
import modulo_fibonacci

# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 

# giving a title to my graph 
plt.title('My first graph!') 

# x axis values
x = modulo_fibonacci.fibonacci_prodotti(int(input("Quale numero di Fibonacci vuoi? ")))
# corresponding y axis values 
y = list(range(1, len(x)+1))

# plotting the points 
plt.plot(x, y) 

# function to show the plot 
plt.show() 
