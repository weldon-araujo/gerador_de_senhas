from string import ascii_letters, punctuation, digits


class gera_senha:
    def __init__(self, tam):
        self.tam = tam
        self.l = 0

    def mostra(self):
        from string import ascii_letters, punctuation
        from random import choice
        self.l = list
        for i in range(0, self.tam):
            self.l = choice(ascii_letters + punctuation + digits)
            print(self.l, end='')


def resp_tamanho():
    print('\033[1;31mTamanho mínimo de 8 caracteres e máximo de 40:\033[0;0m ')


def resp_letra():
    print('\033[1;31mNão é permtido letras ou caracteres:\033[0;0m   ')


tamanho = 0
n = ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26','27', '28', '29', '30','31','32','33','34','35','36','37','38','39','40', 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

while not tamanho in n:
    tamanho = input('Quantidade de caracteres: ')
    if tamanho in ascii_letters or tamanho in punctuation:
        resp_letra()
    else:
        resp_tamanho()
    if tamanho in n:
        tamanho = int(tamanho)

if type(tamanho) is int and tamanho >= 8 and tamanho <= 40:
    tam_ger = gera_senha(tamanho)
    tam_ger.mostra()
