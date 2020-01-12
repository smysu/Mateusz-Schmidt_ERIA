from queue import PriorityQueue

class Element:

	def __init__(self, dystans_calkowity, heurystyka, pozycja):
		
		self.dystans_calkowity = dystans_calkowity
		self.heurystyka = heurystyka
		self.pozycja = pozycja
		
	def __lt__(self, E):
		
		return self.dystans_calkowity + self.heurystyka < E.dystans_calkowity + E.heurystyka
		
		
def euklid(x, y):
	
	return (((x[0] - y[0]) ** 2) + (x[1] - y[1]) ** 2) ** 0.5


def zamkniete(x, mapka, n, m):
	
	C = []
	
	if x[0] + 1 <  n and mapka[x[0] + 1][x[1]] == '0':
		C.append((x[0] + 1, x[1]))
	if x[0] - 1 >= 0 and mapka[x[0] - 1][x[1]] == '0':
		C.append((x[0] - 1, x[1]))
	if x[1] + 1 <  m and mapka[x[0]][x[1] + 1] == '0':
		C.append((x[0], x[1] + 1))
	if x[1] - 1 >= 0 and mapka[x[0]][x[1] - 1] == '0':
		C.append((x[0], x[1] - 1))
		
	return C
	

def gwiazda():
	
	mapka = open('plik.txt').read()
	mapka = mapka.split()
	
	n, m = len(mapka), len(mapka[0])
	meta = (n - 1, m - 1)

	Q = PriorityQueue()
	Q.put(Element(0, 0, (0, 0)))
	pre = dict()
	pre[(0, 0)] = None
	solved = False
	
	while not Q.empty() and not solved:
		e = Q.get()
		dist = e.dystans_calkowity
		pozycja = e.pozycja 
		
		if meta == pozycja:
			solved = True
		else:
			for a in zamkniete(pozycja, mapka, n, m):
				if a not in pre:
					pre[a] = pozycja
					Q.put(Element(dist + 1, euklid(a, meta), a))

	if not solved:
		print('Brak sciezki.')
	else:
		sciezka = set([(0, 0)])
		while pre[meta] != None:
			sciezka.add(meta)
			meta = pre[meta]
		
		for i in range(n):
			for j in range(m):
				if (i, j) in sciezka:
					print(3, end = ' ')
				else:
					print(mapka[i][j], end = ' ')
			print()
		
gwiazda()




