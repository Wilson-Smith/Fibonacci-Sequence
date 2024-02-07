def fibonacci_prodotti(n):
	a, b = 0, 1 # I passo Base
	r, v = 0, 1 # II passo Base

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
		return b * v

print(fibonacci_prodotti(int(input("Quale numero di Fibonacci vuoi? "))))

# È stato usato il metodo con le addizioni ricorsive, che con la funzione ricorsiva per un problema nell'eccessivo Ricorsione da parte del PC nelle Funzioni.
# La funzione associata alla formula che abbiamo visto è la seguente:

"""
def fibonacci(n):
    if n < 1:
	    return 1
	return fibonacci(n-1) + fibonacci(n-2)
"""
# Le addizioni ricorsive, d'altro canto, non hanno un limite di esecuzione (escludendo limiti fisici dell'Hardware).
# In conclusione, si è preferito il metodo delle addizioni ricorsive e non delle funzioni ricorsive per discorsi legati alla struttura del linguaggio Python.
