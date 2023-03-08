c = 5
d = 5.3
print(c, d)
e = c+d
print(e)
f = 2+3j
print(f)
print(type(f))

print(c-d)
print(c//d)
print(c % d)
print(c ** d)
print(2**(1/2))
print(c+2)
c += 2
print(c)



#dodanie elementow do listy na danej pozycji
#usuwanie elementu z danej pozycji
#usunięcie elementu o danej wartości
#dodać sekwencję do listy
#odwrócić listy
#posortować elementy w liście

listy = ['2', 5, 6, 7, 6.5, [2, 3,4]]
print(listy)
listy.append(4)
print(listy)

listy.insert(1, 4)
print(listy)

del listy[0]
print(listy)

listy.remove(5)
print(listy)

listy.extend([1, 2])
print(listy)

listy.reverse()
print(listy)
listy.remove([2, 3,4])
listy.sort()
print(listy)

slownik = {1:'a', 2:2, 3:'klucz',1:3}
print(slownik)
print(slownik[2])
slownik['nowy'] = "wartosc"
print(slownik)
slownik.pop(2)
print(slownik)
del slownik[3]
print(slownik)
print(slownik.keys())
print(slownik.values())
