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
            nome_masculino = input("Informe um nome masculino:")
            profissao = input("Informe uma profissão:") 
            defeito = input("Informe um defeito:")
            qualidade = input("Informe uma qualidade:") 
            qualidade_2 = input("Informe outra qualidade:")
            comida = input("Informe o nome de uma comida:")
            coisa_nojenta = input("Diga algo nojento:")
            objeto = input("Informe um objeto:")

            print_history = """
Conta a lenda que a caipora de nome {0} é protetor dos animais de pele, couro ou chifre, como porcos {3}, tamanduás {4}, cobras, tatus, veados, etc.
Em sua missão, assusta os {1} que matam esses animais de forma cruel e predatória. 
Muitas fêmeas são mortas quando estão prenhas e esses homens, {2}, não têm a mínima compaixão por esses animais.

{0} é muito danado, prega peças nos {1} que chegam às matas, mal intencionados, querendo matar animais. 
Vendo isso, {0} solta uivos e gritos, assombrando-os.
Outra forma de defender os bichos é espantando-os para longe dos {1} ou ressuscitando os que foram mortos.

{0} fica furioso e lança seu {6}, persegue os {1}, bate em seus cachorros, até que os mesmos fujam da floresta, deixando a {7} jogada ao chão.

Porém  {0} não é totalmente correto, pois gosta de fumo e bebida. 
Com isso, alguns {1} levam esses presentinhos para ele em troca de uma boa {5}. 
Mas a caça deve acontecer sem maltratar o animal, nem matar uma fêmea que espera um filhote.
""".format(nome_masculino,profissao,defeito,qualidade,qualidade_2,comida, coisa_nojenta,objeto)

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

        print("------------------------------------FIM----------------------------------")
