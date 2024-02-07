# importing the required module 
import matplotlib.pyplot as plt 
import modulo_fibonacci

# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 

# giving a title to my graph 
plt.title('Grafico Divisioni') 

# x axis values
y = modulo_fibonacci.fibonacci_prodotti_divisioni(int(input("Quanti numeri di Fibonacci vuoi? ")))
# corresponding y axis values 
x = list(range(1, len(y)+1))

# plotting the points 
plt.plot(x, y) 

# function to show the plot 
plt.show() 
