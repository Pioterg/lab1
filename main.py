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

# print('a = %(zm)d' % {'zm' : 12})
# print('a = {}'.format(12))
# napis = input('sprawdz liczbe: ')
# print(napis)
# print(type(napis))
# napis = int(napis)
# print(type(napis))

#instrukcja warunkowa
#if warunek:
    #instrukcja
#elif warunek
    #instrukcja
#else:
    #instrukcja

# a = input('podaj a: ')
# b = input('podaj b: ')
# a = int(a)
# b = int(b)
# c = input('podaj c:')
# d = input('podaj d: ')
# c = int(c)
# d = int(d)
#
# if (a > b) & (c > d):
#     print('a wieksze od b i c wieksze od d')
# else:
#     print('a nie jest wieksze od b lub c nie jest wieksze od d')

# if a > b:
#     print('a większe od b')
# elif a < b:
#     print('a mniejsze od b')
# else:
#     print('liczby sa rowne')

#for element in sekwencja
    #instrukcja
#else:
    #instrukcja po petli

# for x in range(1, 6, 1):
#     print(x)
# else:
#     print('koniec petli for')

list = [2, 5, 6, 8, 10]

# for x in list:
#     print(x)

# for x in range(0, len(list), 1):
#     print(x)

#while warunek:
    #instrukcje
#else:
    #instrukcje

licznik = 0
while licznik != len(list):
    print(listy[licznik])
    licznik += 1

# liczby = [2, 5, 6, 7, 3, 4]
# a = input('podaj a: ')
# a = int(a)
# licznik = 0
#
# while licznik != len(list):
#     if liczby[licznik] - a == 0:
#         print(str(a) + ' ' + str(liczby[licznik]) + ' = 0')
#
#     licznik += 1
# else:
#     print(licznik)
#
# usunac all ele z lisy o wartosci 2

list2 = [2, 1, 2, 3, 2, 4, 2, 5]
licznik = 0
while licznik != len(list2):
    if list2[licznik] == 2:
        list2.remove(2)
    licznik += 1
    print(list2)
