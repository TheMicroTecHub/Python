def computepay():
    return h * r if h <= 40 else (40 * r + (h-40) * 1.5 * r)

hrs = input("Enter Hours:")
h = int(hrs)
rate = input("Enter Rate:")
r = float(rate)
p = computepay()
print("Pay", p)