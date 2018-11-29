def primeNumbers(x):
	if type(x) is int:
		prime = []
		numbers = range(1,x)
		for i in numbers:
			if isprime(i):
				prime.append(i)

		return prime
	raise TypeError

def isprime (n):
	count = 0
	numbers = range(1,n+1)
	for i in numbers:
		# print("no:",n,"list",i)
		if n % i == 0:
			count = count+1
	if count == 2:
		return True
	return False
print(isprime())