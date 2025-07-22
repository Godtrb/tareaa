def fact(n):
    if n == 0:
        return 1
    else:
        if (n==1):
            print(f"{n}:", end="")
        else:
            print(f"{n}*", end="")
        return n * fact(n-1)
def SumNAt(n):
    if n == 0:
        return 1
    else:
        if (n==1):
            print(f"{n}:", end="")
        else:
            print(f"{n}+", end="")
        return n + SumNAt(n-1)
def Fibo(n):
    if n == 0:
        return 1
    elif n==1|n==2|n==3:
        return "1"
    elif (n>3):
        return Fibo(n-1) + Fibo(n-2)
def TextInvert(x):
    return x[::-1]
opt=0
while(opt!=7):
    print("----------Menu Mate---------------")
    print("1. Fact Num")
    print("2. Suma Nat Nums")
    print("3. Calc Fibonacci")
    print("4. Contar Letras")
    print("5. Invertir Texto")
    print("6. Pot Numero")
    print("7. Sair")
    opt=int(input(""))
    match (opt):
        case 1:
            num=int(input("Ingresa un numero: "))
            if(num<=0):
                print("Numero no puede ser 0 o negativo")
            else:
                print(fact(num))
        case 2:
            num = int(input("Ingresa un numero: "))
            if (num <= 0):
                print("Numero no puede ser 0 o negativo")
            else:
                print(SumNAt(num))
        case 3:
            num = int(input("Ingresa un numero: "))
            if (num <= 0):
                print("Numero no puede ser 0 o negativo")
            else:
                print(Fibo(num))
        case 4:
            text= input("Ingresa un texto: ")
            text = TextInvert(text)
            print(text)