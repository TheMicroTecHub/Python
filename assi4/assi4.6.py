def computepay():
    if h <= 40:
        x = h * r
    else:
        x = (40 * r + (h-40) * 1.5 * r)
    return x

hrs = input("Enter Hours:")
h = int(hrs)
rate = input("Enter Rate:")
r = float(rate)
p = computepay()
print("Pay", p)