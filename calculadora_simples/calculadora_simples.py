### print("qual operação voce deseja ? \n")
print("[1]para somar \n[2]para subtrair \n[3]para dividir \n[4]para multiplicar\n")
opc = int(input("digite sua opção: "))

if opc == 1 :
    n1 = int(input("digite um valor: "))
    n2 = int(input("digite outro valor: "))
    print(f"o primeiro numero é: {n1}")
    print(f"o segundo numero é: {n2}")
    print (f"a soma entre eles é:   {n1+n2} ")
elif opc == 2:
    n1 = int(input("digite um valor: "))
    n2 = int(input("digite outro valor: "))
    print(f"o primeiro numero é: {n1}")
    print(f"o segundo numero é: {n2}")
    print (f"a subtraçaõ entre eles é:   {n1-n2} ")
elif opc == 3:
    n1 = int(input("digite um valor: "))
    n2 = int(input("digite outro valor: "))
    print(f"o primeiro numero é: {n1}")
    print(f"o segundo numero é: {n2}")
    print (f"a divisão entre eles é:   {n1/n2} ")
elif opc == 4:
    n1 = int(input("digite um valor: "))
    n2 = int(input("digite outro valor: "))
    print(f"o primeiro numero é: {n1}")
    print(f"o segundo numero é: {n2}")
    print (f"a multiplicação entre eles é:   {n1*n2} ")
else:
    print("ERROR!!!")
    