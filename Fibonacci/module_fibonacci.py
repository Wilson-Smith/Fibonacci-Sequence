def fibonacci_sequenza(n):
	a = 0 # I passo Base
	b = 1 # II passo Base
	m = [1]
	
    # Controllo Numero sia Naturale
	if n < 0:
		raise ValueError("Il numero inserito deve essere maggiore di 0")
		
    # Controllo numero con Risultato Speciale
	elif n == 0:
		return a
	elif n == 1:
		return b
	
    # Codice di Fibonacci
	else:
		for i in range(2, n+1):
			c = a + b
			a = b
			b = c
			m.append(b)
		return m
	
def fibonacci_prodotti(n):
	a, b = 0, 1 # I passo Base
	r, v = 0, 1 # II passo Base
	m = [1]

    # Controllo Numero sia Naturale
	if n < 0:
		raise ValueError("Il numero inserito deve essere maggiore di 0")
		
    # Controllo numero con Risultato Speciale
	elif n == 0:
		return a
	elif n == 1:
		return b
	
    # Codice di Fibonacci
	else:
		for i in range(2, n + 1):
			c = a + b
			a = b
			b = c

		for j in range(2, n + 2):
			p = r + v
			r = v
			v = p
			m.append(b)
		return m

def fibonacci_divisioni(n):
	a = 0 # I passo Base
	b = 1 # II passo Base
	u = [1]
	v = []
	l = 0

    # Controllo Numero sia Naturale
	if n < 0:
		raise ValueError("Il numero inserito deve essere maggiore di 0")
		
    # Controllo numero con Risultato Speciale
	elif n == 0:
		return a
	elif n == 1:
		return b
	
    # Codice di Fibonacci
	else:
		for i in range(2, n+1):
			c = a + b
			a = b
			b = c
			u.append(b)
		
        # Iterazione per: F(n)/F(n-1)
		for j in range(1, len(u)):
			l = u[j]/u[j-1]
			v.append(l)
			l = 0
		return v

def fibonacci_prodotti_divisioni(n):
	a, b = 0, 1 # I passo Base
	r, k = 0, 1 # II passo Base
	u = [1]
	v = []
	l = 0

    # Controllo Numero sia Naturale
	if n < 0:
		raise ValueError("Il numero inserito deve essere maggiore di 0")
		
    # Controllo numero con Risultato Speciale
	elif n == 0:
		return a
	elif n == 1:
		return b
	
    # Codice di Fibonacci
	else:       
		for i in range(2, n + 1):
			c = a + b
			a = b
			b = c

		for j in range(2, n + 2):
			p = r + k
			r = k
			k = p
			u.append(k)
			
        # Iterazione per: F(n)/F(n-1)
		for j in range(1, len(u)):
			l = u[j]/u[j-1]
			v.append(l)
			l = 0
		return v
	
