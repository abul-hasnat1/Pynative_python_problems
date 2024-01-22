def octal(n):
    oct=''
    r=1
    while r!=0:
        r=n%8
        n=n//8
        oct+=str(r)
    print(oct[::-1])
octal(89)