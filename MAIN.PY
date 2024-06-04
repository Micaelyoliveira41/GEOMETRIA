'''
Crie um programa que o usuário possa escolher se deseja saber a área de um círculo, de um triângulo ou de um trapézio.

'''
import os

#função do menu
def exibir_menu():
   print('1-Gostaria de calcular qual geometria de um "círculo."')
   print('2-Gostaria de calcular qual geometria de um "triângulo."')
   print('3-Gostaria de calcular qual geometria de um "trapézio".')
   print('4-Sair do programa.')

#função da área do círculo
def calcular_circulo(r):
        a = 3.14*r** 2
        return a

#função da área do triângulo
def calcular_triângulo(base, altura):
            area = (base*altura)/2
            return area

#função da área do trapézio
def calcular_trapezio(base_menor, base_maior, h):
    a = ((base_menor + base_maior)*h)/2
    return a

#Usuario escolhe qual geometria deseja calcular
while True:
  exibir_menu()
  decisão = input('Informe a opção desejada: ')
  os.system('cls')
  
  match decisão:
    case '1': 
      print('Área do círculo: a = π*r²') 
      r = int(input('Informe o valor do raio: '))
      print(f'Área do círculo: {calcular_circulo(r)}.')
      continue
      
    case '2':
      print('Área do triângulo: a = (b*a)/2') 
      base = int(input('Informe o valor da base: '))
      altura = int(input('Informe o valor da altura: '))
      print(f'Área do triângulo: {calcular_triângulo(base, altura)}.')
      continue
      
    case '3':
       print('Área do trapézio: a = ((b+8)*h/2') 
       base_menor = int(input('Informe o valor da base menor: '))
       base_maior = int(input('Informe o valor da base maior: '))
       h = int(input('Informe o valor da altura do trapézio: '))
       print(f'Área do trapézio: {calcular_trapezio(base_menor, base_maior, h)}')
       continue
    case '4':
          break
    case '_':
      print('Resposta inválida!')
      
  

