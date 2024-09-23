
G = int(input('group_order = '))
g = int(input('g = '))

ag = int(input('a*g = '))
bg = int(input('b*g = '))

print('a:')
for a in range(G):
    if (a * g) % G == ag:
        print(a)

print('b:')
for b in range(G):
    if (b * g) % G == bg:
        print(b)


