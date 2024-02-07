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
	
x = fibonacci_divisioni(5)
print(x)

# È stato usato lo stesso metodo di Iterazione precedentemente spiegato.
# La variazione è nella creazione di una lista (o vettore dir si voglia) che itera con gli elementi già presenti nella lista u.
# È stata usata la tecnica F(n)/F(n-1) rispetto alla tecnica F(n+1)/F(n) per errori in compilazione e velocità.
# Tale soluzione propone un risultato in tempi mediamente accettabili con una compilazione semplice, ma complessità esponenziale (principalmente dall'algoritmo di Fibonacci)
# La complessità temporale dell'algoritmo di Fibonacci è: T(n)=T(n−1)+T(n−2)+1≤O(2^n), quindi complessivamente a O(2^n)+n.
