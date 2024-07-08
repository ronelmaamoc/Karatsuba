def Karatsuba(A, B):
    g = abs(A)
    k = abs(B)

    if len(str(g)) == 1 or len(str(k)) == 1:
        return A*B

    m = max(len(str(g)), len(str(k)))
    n = m//2
    A1,A0 = divmod(A,10**n)
    B1,B0 = divmod(B,10**n)
    C00 = Karatsuba(A0, B0)
    C10 = Karatsuba(A1, B1)
    C11 = Karatsuba((A0-A1), (B0-B1))

    return C00+10**(n)*(C00+C10-C11)+10**(2*n)*C10

print("\n")
A = int(input("entrez le premier nombre: "))
B = int(input("entrez le deuxieme nombre: "))
C = Karatsuba(A, B)
print(f"\nKARATSUBA({A}, {B}) = {C}\n")
