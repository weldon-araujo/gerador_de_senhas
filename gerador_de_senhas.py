from string import ascii_letters, punctuation, digits, ascii_lowercase, ascii_uppercase


class gera_senha:
    def __init__(self, tam, arg):
        self.tam = tam
        self.arg = arg
        self.l = 0

    def full(self):
        from string import ascii_letters, punctuation, digits, ascii_lowercase, ascii_uppercase
        from random import choice
        self.l = list
        if self.arg == '1':
            for i in range(0, self.tam):
                self.l = choice(ascii_uppercase + ascii_lowercase + digits)
                print(self.l, end='')
        elif self.arg == '2':
            for i in range(0, self.tam):
                self.l = choice(ascii_uppercase + ascii_lowercase + punctuation)
                print(self.l, end='')
        elif self.arg == '3':
            for i in range(0, self.tam):
                self.l = choice(ascii_uppercase + ascii_lowercase)
                print(self.l, end='')
        elif self.arg == '4':
            for i in range(0, self.tam):
                self.l = choice(ascii_uppercase)
                print(self.l, end='')
        elif self.arg == '5':
            for i in range(0, self.tam):
                self.l = choice(digits + punctuation + ascii_uppercase)
                print(self.l, end='')
        elif self.arg == '6':
            for i in range(0, self.tam):
                self.l = choice(digits + punctuation + ascii_lowercase)
                print(self.l, end='')
        elif self.arg == '7':
            for i in range(0, self.tam):
                self.l = choice(digits + punctuation)
                print(self.l, end='')
        elif self.arg == '8':
            for i in range(0, self.tam):
                self.l = choice(digits + ascii_uppercase)
                print(self.l, end='')
        elif self.arg == '9':
            for i in range(0, self.tam):
                self.l = choice(digits + ascii_lowercase)
                print(self.l, end='')
        elif self.arg == '10':
            for i in range(0, self.tam):
                self.l = choice(punctuation + ascii_uppercase)
                print(self.l, end='')
        elif self.arg == '11':
            for i in range(0, self.tam):
                self.l = choice(punctuation + ascii_lowercase)
                print(self.l, end='')
        elif self.arg == '12':
            for i in range(0, self.tam):
                self.l = choice(ascii_letters + punctuation + digits)
                print(self.l, end='')



def resp_tamanho():
    print('\033[1;31m[ERRO FATAL ! TAMANHO MINIMO DE 8 CARACTERES E MAXIMO DE 40:]\033[0;0m')


def resp_letra():
    print('\033[1;31m[ERRO FATAL ! NÃO É PERMITIDO LETRAS, SIMBOLOS OU ESPAÇOS EM BRANCO:]\033[0;0m   ')


tamanho = 0
n = ['8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26','27', '28', '29', '30','31','32','33','34','35','36','37','38','39','40',8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

while not tamanho in n:
    tamanho = input('TAMANHO DO PASSWORD: ')
    if tamanho in ascii_letters or tamanho in punctuation:
        resp_letra()
    elif tamanho not in n:
        resp_tamanho()
    else:
        tamanho = int(tamanho)


def men():
    p = input('''
    \033[1;31mOPÇÕES DE PASSWORD:\033[0;0m
    [  1 ] LETRAS MAIUSCULAS + LETRAS MINUSCULAS + NUMEROS 
    [  2 ] LETRAS MAIUSCULAS + LETRAS MINUSCULAS + SIMBOLOS
    [  3 ] LETRAS MAIUSCULAS + LETRAS MINUSCULAS
    [  4 ] LETRAS MAIUSCULAS  
    [  5 ] NUMEROS + SIMBOLOS + LETRAS MAIUSCULAS
    [  6 ] NUMEROS + SIMBOLOS + LETRAS MINUSCULAS
    [  7 ] NUMEROS + SIMBOLOS
    [  8 ] NUMEROS + LETRAS MAIUSCULAS
    [  9 ] NUMEROS + LETRAS MINUSCULAS
    [ 10 ] SIMBOLOS + LETRAS MAIUSCULAS
    [ 11 ] SIMBOLOS + LETRAS MINUSCULAS
    [ 12 ] TODOS OS VALORES
    ''')
    return p

inst = men()

esc_men = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

if type(tamanho) is int and tamanho >= 8 and tamanho <= 40:
    if inst in esc_men:
        arg = inst
        tam_ger = gera_senha(tamanho, arg)
        tam_ger.full()