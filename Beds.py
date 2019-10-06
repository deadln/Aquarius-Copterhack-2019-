

def flyby_beds(a, b, c, d): #c -расстояние между лунками d - расстояние между полосами
    beds = []
    x = 0
    y = 0
    fly_from_zero = 1
    beds.append(Point(0, 0))
    while y <= b:
        if fly_from_zero == 1:
            while x < a:
                x += c
                beds.append(Point(x, y))
        else:
            while x > 0:
                x -= c
                beds.append(Point(x, y))

        y+=d
        fly_from_zero*=-1
        if y<=b:
            beds.append(Point(x, y))
    return beds

