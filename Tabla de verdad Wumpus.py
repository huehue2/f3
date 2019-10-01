def bicondicional(p,q):
    z = (p and q) or (not p and not q)
    return z

def conjuncion(p,q):
    z= (p and q)
    return z

def disyuncion(p,q):
    z= (p or q)
    return z

def implicacion(p,q):
    if (p == False):
        z = True
    else:
        z = q
    return z

def xor(p,q):
    z= (p and not q) or (not p and q)
    return z

def negacion(p):
    z= not p
    return z

if __name__ == '__main__':
    Datos = []
    b11 = [False, True]
    b21 = [False, True]
    p11 = [False, True]
    p12 = [False, True]
    p21 = [False, True]
    p22 = [False, True]
    p31 = [False, True]
    
    for b11val in b11:
        for b21val in b21:
             for p11val in p11:
                  for p12val in p12:
                       for p21val in p21:
                            for p22val in p22:
                                 for p31val in p31:
                                    Lista = []
                                    Lista.append(b11val)
                                    Lista.append(b21val)
                                    Lista.append(p11val)
                                    Lista.append(p12val)
                                    Lista.append(p21val)
                                    Lista.append(p22val)
                                    Lista.append(p31val)
                                    Datos.append(Lista)

    i = 0        
    for (b11,b21,p11,p12,p21,p22,p31) in Datos:
        r1=negacion(p11)
        r2=bicondicional(b11,disyuncion(p12,p21))
        r3=bicondicional(b21,disyuncion(p11,disyuncion(p22,p31)))
        r4=negacion(b11)
        r5=b21
        bc=conjuncion(r1,conjuncion(r2,conjuncion(r3,conjuncion(r4,r5))))

        i =i+1
        print(i,"-",b11," ",b21," ",p11," ",p12," ",p21," ",p22," ",p31,"->",r1," ",r2," ",r3," ",r4," ",r5," ",bc)
        
       





