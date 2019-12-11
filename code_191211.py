with open('/Users/tetyos/Downloads/input.txt', 'r') as f:
    mass  = []
    for line in f:
        line=int(line.rstrip())
        line//=3
        line-=2
        mass.append(line)
    print(sum(mass))

