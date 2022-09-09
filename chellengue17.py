x = 0
a = [12,15,22]
b = [1,24,4]

a_lista = []
b_lista = []
longitud = len(a)
print(sum(a))
print(len(a))

for x in range(longitud):
    if a[x] > b[x]:
        a_lista.append(1)
    elif a[x] < b[x]:
        b_lista.append(1)
    elif a[x] == b[x]:
        print('')
    else:
        print('x')
    x=x+1
print(sum(a_lista), ',', sum(b_lista))
