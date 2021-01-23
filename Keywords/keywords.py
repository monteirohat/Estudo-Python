#Arquivo para testar as palavras reservadas do PYTHON

#Criando um dicionário das palavras reservadas
palavras_reservadas = {
    "1":"and","2":"as","3":"assert","4":"break",
    "5":"class","6":"continue","7":"def","8":"del",
    "9":"elif","10":"else","11":"except","12":"False","13":"finally",
    "14":"for","15":"from","16":"global","17":"if",
    "18":"import","19":"in","20":"is","21":"lambda",
    "22":"None","23":"nonlocal","24":"not","25":"or",
    "26":"pass","27":"raise","28":"return","29":"True",
    "30":"try","31":"while","32":"with","33":"yield"
}
print("*************************************************************")
print("|                Palavras reservadas do Python              |")
print("*************************************************************")

cont = 1
text_line = ""

# foi adicionado regras de espaço para ficar formatado o texto apresentado
for i in palavras_reservadas:
    if int(i) < 10:
        text_line += f"{i}  - {palavras_reservadas[i]}"
    else:
        text_line += f"{i} - {palavras_reservadas[i]}"

    falta = 10-len(palavras_reservadas[i]) 
    cont2 = 0

    while cont2 < falta:
        text_line += " "
        cont2 +=1
    

    if int(i) == len(palavras_reservadas):
        print(text_line)

    if cont == 4:
        print(text_line)
        cont = 0
        text_line = ""
    cont +=1
    
print("------------------------------------------------------------")
option = ""

#Verifica se o usuário coloco um número válido
while not option.isdigit():
    option = input("Escolha a opção:")

option = int(option)

#Verifica a opção que o usuário escolheu
if option == 1:
    print(f"Opção escolhida: {option} - {palavras_reservadas[option]}")

    


elif option == 2:
    print(f"{option}")
elif option == 3:
    print(f"{option}")
elif option == 4:
    print(f"{option}")
elif option == 5:
    print(f"{option}")
elif option == 6:
    print(f"{option}")
elif option == 7:
    print(f"{option}")
elif option == 8:
    print(f"{option}")
elif option == 9:
    print(f"{option}")
elif option == 10:
    print(f"{option}")
elif option == 11:
    print(f"{option}")
elif option == 12:
    print(f"{option}")
elif option == 13:
    print(f"{option}")
elif option == 14:
    print(f"{option}")
elif option == 15:
    print(f"{option}")
elif option == 16:
    print(f"{option}")
elif option == 17:
    print(f"{option}")
elif option == 18:
    print(f"{option}")
elif option == 19:
    print(f"{option}")    
elif option == 20:
    print(f"{option}")
elif option == 21:
    print(f"{option}")
elif option == 22:
    print(f"{option}")
elif option == 23:
    print(f"{option}")
elif option == 24:
    print(f"{option}")
elif option == 25:
    print(f"{option}")
elif option == 26:
    print(f"{option}")
elif option == 27:
    print(f"{option}")
elif option == 26:
    print(f"{option}")
elif option == 29:
    print(f"{option}")
elif option == 30:
    print(f"{option}")
elif option == 31:
    print(f"{option}")
elif option == 32:
    print(f"{option}")
elif option == 33:
    print(f"{option}")
else:
    print("Opção inválida.")

#assert
# x = "Hello"

# assert x == "goodbye", "x should be 'hello'"

# class MyClass:
#   name = "John"

# del MyClass

# print(MyClass) 