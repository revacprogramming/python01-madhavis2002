# Functions

def computepay(h,r):
    if h>40:
        rate1=(r*1.5)*(h-40)
    return((40*r)+rate1)
hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Rate:"))
p = computepay(hrs,rate)
print("pay",p)
