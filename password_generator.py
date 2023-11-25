import random
import PySimpleGUI as sg

layout = [
    [sg.Text('Bem-vindo ao seu Gerador de Senhas')],
    [sg.Text('Quantidade de senhas a serem geradas')],
    [sg.Input(key='qtdSenhas')],
    [sg.Text('qtdSenhas')],
    [sg.Text('Digite o comprimento da senha:')],
    [sg.Input(key='qtdCaracteres')],
    [sg.Text('qtdCaracteres')]

]

window = sg.Window('qtdCaracteres', layout=layout)
#print('Bem-vindo ao seu Gerador de Senhas')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
number = int(input('Quantidade de senhas a serem geradas: '))
length = int(input('Digite o comprimento da senha: '))

print('\nAqui estão suas senhas: ')

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
