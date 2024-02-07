def fibonacci_sequenza(n):
	a = 0 # I passo Base
	b = 1 # II passo Base
	
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
		return b

print(fibonacci_sequenza(int(input("Quale numero di Fibonacci vuoi? "))))

# È stato usato il metodo con le addizioni ricorsive, che con la funzione ricorsiva per un problema nell'eccessivo Ricorsione da parte del PC nelle Funzioni.
# La funzione associata alla formula che abbiamo visto è la seguente:

"""
def fibonacci(n):
    if n < 1:
	    return 1
	return fibonacci(n) + fibonacci(n + 1)
"""
# Le addizioni ricorsive, d'altro canto, non hanno un limite di esecuzione (escludendo limiti fisici dell'Hardware).
# In conclusione, si è preferito il metodo delle addizioni ricorsive e non delle funzioni ricorsive per discorsi legati alla struttura del linguaggio Python.
