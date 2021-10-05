# 1- imports bibliotecas

# 2- Classe

# 3- Metodos e Funções

# def = Definition - Definição
def print_hi(name):
    print(f'Oi, {name}')  # a partir do python 3
    print('Oi, +{name}')  # a partir do python 3

def calcular_area_do_retangulo(largura, comprimento):
     return largura * comprimento

def calcular_area_do_quadrado(lado):
    return  lado ** 2

def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento / 2

def contagem_regressiva(inicio, fim):
    for numero  in range(fim): # repetir bloco de zero até fim
        print (numero)

def apoiar_candidato(nome,  vezes):
    for nemro in range(vezes):
        print(f"{numero}-{nome}")

    if numero <= 9:
        print(f'00, {numero + 1}, -, {nome}')

    elif < 99:
        print(f'0, {numero + 1}, -, {nome}')

    else:
        print(numero + 1, '-', nome)

def brincar_de_plin(fim)
    for numero in range (fim)
      if numero % 4 == 0
          print('PLIM!')
      else:
          print('0{:0>9}'.format(numero))
def sair()



 # estrutura de identificação/ execução do script
if __name__ == '__main__':
    continua = true

    while continua true:
        print('##########################')
        print('#                   #     ')
        print('   Menu de Opções         ')
        print('# 1- Olá Mundo      #     ')
        print('# 2- Área do Retângulo #  ')
        print('# 3- Área do Quadrado #   ')
        print('# 4- Área do Triângulo #  ')
        print('# 5- Contagem Regressiva #')
        print('# 6- Apoia Candidadto    #')
        print('# 7- Brincar de Plim     #')
        print('#                        #')
        print('# Z-Sair                 #')
        print('# # # # # # # # # # # # # ')

        escolha = input('Escolha a sua opçãp')
        

        Opção = {
        print_hi('Lene')
        1- (calcular_area_do_retangulo(8,5)
        2- (calcular_area_do_Quadrado(7)
        3- (calcular_area_do_triangulo(5,4)
        4- (Contagem_Regressiva()
        5-
        6-
        }
  # Chamar a função de calculo  da area do retangulo
  resultado = calcular_area_do_retangulo(3,4)
  print(f"A area do retangulo é de {resultado} m2")

  #Chamar a função de calculo  da area do quadrado
  resultado = calcular_area_do_quadrado(5)
 print(f"A area do quadrado é de {resultado} m2")

 #Chamar a função de calculo  da area do triangulo
 resultado = calcular_area_do_triangulo(6,7)
 print(f"A area do triangulo é de {resultado} m2")

 #executar contagem progressiva
 contagem_progressiva(11)

 # exibir nome de candidato varias vezes

 # brincar de plim até (100)