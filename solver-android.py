#!/bin/python3
"""
"""

def calcAll(*values,seen=None):
    seen = seen or set()
    if len(values) == 2:
        a,b  = values
        a,sa = (a[0],f"({a[1]})") if isinstance(a,tuple) else (a,str(a))
        b,sb = (b[0],f"({b[1]})") if isinstance(b,tuple) else (b,str(b))
        if a>b : a,sa, b,sb = b,sb, a,sa
        if (a,b) in seen or seen.add((a,b)) :return
        yield a+b, f"{sa}+{sb}"
        yield a-b, f"{sa}-{sb}"
        yield b-a, f"{sb}-{sa}"
        if b != 0 and a != 0 and a%b==0: yield a//b, f"{sa}/{sb}"
        if a != 0 and b != 0 and b%a==0: yield b//a, f"{sb}/{sa}"
        if a != 0 and b !=0: yield a*b, f"{sa}*{sb}"
        return
    pairs = ((i,j) for i in range(len(values)-1) for j in range(i+1,len(values)))
    for i,j in pairs:
        rest = [*values]
        a,b  = rest.pop(j),rest.pop(i)
        for paired in calcAll(a,b,seen=seen):
            for result in calcAll(paired,*rest):
               if result in seen or seen.add(result): continue
               yield result

def resolve():
    n1=int(input())
    n2=int(input())
    n3=int(input())
    n4=int(input())
    n5=int(input())

    r_min = -1
    sr_min = ""
    r_list = []
    sr_list = []
    for r,sr in sorted(calcAll(n1, n2, n3, n4, n5)):
        if r>=0 and (r_min > r or r_min == -1):
            r_min = r
            sr_min = sr
            r_list = [r]
            sr_list = [sr]
        elif r>=0 and r_min == r:
            r_list.append(r)
            sr_list.append(sr)

#    for i in range (len(r_list)):
#        print(sr_list[i],"=",r_list[i])

    print(sr_list[0],"=",r_list[0])


if __name__ == "__main__":
    while True:
        resolve()

