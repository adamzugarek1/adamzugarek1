def funkce_rada(delka_rady):

    ret = []
    a = 0
    b = 1
    while  len(ret) < delka_rady:
        ret.append(a)
        a, b = b, b+a
    return ret

delka_rady = int(input("Zadejte délku seznamu"))
fibonaciho_rada = funkce_rada(delka_rady)  


print("Fibonnaciho řada o délce",delka_rady,"je:",fibonaciho_rada)


