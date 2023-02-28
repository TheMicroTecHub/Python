text = "X-DSPAM-Confidence:    0.8475"
x = text.find(':')
z = text[x+1:]
f = float(z)
print(f)