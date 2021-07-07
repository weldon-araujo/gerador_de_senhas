from string import ascii_letters, punctuation


class gera_senha:
    def __init__(self, tam):
        self.tam = tam
        self.l = 0

    def mostra(self):
        from string import ascii_letters, punctuation
        from random import choice
        self.l = list
        for i in range(0, self.tam):
            self.l = choice(ascii_letters + punctuation)
            print(self.l, end='')


def resp_tamanho():
    print('\033[1;31m Tamanho mínimo de 8 caracteres e máximo de 30:\033[1;31m  ')


def resp_letra():
    print('Não é permtido letras ou caracteres: ')


tamanho = 0
n = ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26',
     '27', '28', '29', '30', 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

while not tamanho in n:
    tamanho = input('Quantidade de caracteres: ')
    if tamanho in ascii_letters or tamanho in punctuation:
        resp_letra()
    else:
        resp_tamanho()
    if tamanho in n:
        tamanho = int(tamanho)

if type(tamanho) is int and tamanho >= 8 and tamanho <= 30:
    tam_ger = gera_senha(tamanho)
    tam_ger.mostra()
