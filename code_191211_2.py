with open('/Users/tetyos/Downloads/input.txt', 'r') as f:
    mass_total = []
    for line in f:
        line=int(line.rstrip())
        mass=0
        print(line)
        while line>0:
            line//=3
            line-=2
            print(line)
            if line>0:
                mass+=line
        mass_total.append(mass)
    print(sum(mass_total))

