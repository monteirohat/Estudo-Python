# ----------------------------------------------------------
# Mad Libs: É um jogo em que se substitui as palavras de
# uma historia, gerando uma história engraçada e divertida
# ----------------------------------------------------------

# 1° - Menu de escolha das histórias
print("*************************************************************")
print("|                         Mad Libs                          |")
print("*************************************************************")
print("""Mad Libs: É um jogo em que se substitui as palavras de
uma historia, gerando uma história engraçada e divertida.

Veja abaixo as histórias disponíveis:
""")
historias = {
    "1": "Caipora", "2": "Curupira", "3": "Boitatá","4":"Lobisomem","5":"Iara"
}
cont = 0
text_line = ""

for i in historias:
    text_line += f"[{i}] - {historias[i]} \n"

    if int(i) == len(historias):
        print(text_line)

    cont += 1
print("*************************************************************")
print(">>>>>>>>>> Escolha uma história informando o número <<<<<<<<<")

option = ""
print_history =""
while not option.isdigit():
    try:
        option = input("Número:")
        
        print("\nVocê escolheu a história: " + historias[option])
        print("-----------------------------------------------")
        if int(option) == 1:
            print(""" 
Informações da história:
Caipora é um personagem do folclore, representado tanto por uma mulher, índia, 
como por um homem matuto, baixo, que aparece montado em um caititu ou porco-do-mato. 
Antes era conhecido como Caiçara, entidade que protegia as caças.

As características principais do Caipora são: 
ser anão, ter cabelos vermelhos, orelhas pontudas e dentes esverdeados.
            
Bom, antes de começar nossa história, iremos lhe perguntar algumas palavras.
Vamos lá!
""")
            nome = input("Informe um nome:")


            print_history = """
Conta a lenda que o {0} é protetor dos animais de pele, couro ou chifre, como porcos, tamanduás, cobras, tatus, veados, etc.
Em sua missão, assusta os caçadores que matam esses animais de forma cruel e predatória. 
Muitas fêmeas são mortas quando estão prenhas e esses homens, insensíveis, não têm a mínima compaixão por esses animais.

{0} é muito danado, prega peças nos homens que chegam às matas, mal intencionados, querendo matar animais. 
Vendo isso, {0} solta uivos e gritos, assombrando-os.
Outra forma de defender os bichos é espantando-os para longe dos caçadores ou ressuscitando os que foram mortos.

{0} fica furioso e lança seu barulho, persegue os caçadores, bate em seus cachorros, até que os mesmos fujam da floresta, deixando a arma jogada ao chão.

Porém  {0} não é totalmente correto, pois gosta de fumo e bebida. 
Com isso, alguns caçadores levam esses presentinhos para ele em troca de uma boa caçada. 
Mas a caça deve acontecer sem maltratar o animal, nem matar uma fêmea que espera um filhote.
""".format(nome)
            print(print_history)
        elif int(option) == 2:
            print(historias[option])
        elif int(option) == 3:
            print(historias[option])
        elif int(option) == 4:
            print(historias[option])
        elif int(option) == 5:
            print(historias[option])    


        break
    except:
        continue

        
