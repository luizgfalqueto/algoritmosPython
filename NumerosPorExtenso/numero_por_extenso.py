unidades = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
teens = ('onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
dezenas = ('dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')
longs = ['mil', 'milhão', 'bilhão', 'trilhão', 'quatrilhão', 'quintilhão']
longp = ['mil', 'milhões', 'bilhões', 'trilhões', 'quatrilhões', 'quintilhões']


def extenso(number): //trata de gerar o extenso do numero de 0 a 999
    num, tam = str(number).strip(), len(str(number).strip())
    result = ''
    if tam == 1:
        result = result + unidades[number]
    elif tam == 2:
        if number == 10:
            result += dezenas[0]
        elif 10 < number < 20:
            result += teens[int(num[1]) - 1]
        else:
            if num[1] != '0':
                result += dezenas[int(num[0]) - 1]
                result += ' e '
                result += unidades[int(num[1])]
            else:
                result += dezenas[int(num[0]) - 1]
    elif tam == 3:
        if num[0] == '1':
            if num[1] == '0' and num[2] == '0':
                result += 'cem'
            else:
                result += 'cento e ' + extenso(int(num[1:]))
        elif num[0] == '2':
            if num[1] == '0' and num[2] == '0':
                result += 'duzentos'
            else:
                result += 'duzentos e ' + extenso(int(num[1:]))
        elif num[0] == '3':
            if num[1] == '0' and num[2] == '0':
                result += 'trezentos'
            else:
                result += 'trezentos e ' + extenso(int(num[1:]))
        elif num[0] == '4':
            if num[1] == '0' and num[2] == '0':
                result += 'quatrocentos'
            else:
                result += 'quatrocentos e ' + extenso(int(num[1:]))
        elif num[0] == '5':
            if num[1] == '0' and num[2] == '0':
                result += 'quinhentos'
            else:
                result += 'quinhentos e ' + extenso(int(num[1:]))
        elif num[0] == '6':
            if num[1] == '0' and num[2] == '0':
                result += 'seiscentos'
            else:
                result += 'seiscentos e ' + extenso(int(num[1:]))
        elif num[0] == '7':
            if num[1] == '0' and num[2] == '0':
                result += 'setecentos'
            else:
                result += 'setecentos e ' + extenso(int(num[1:]))
        elif num[0] == '8':
            if num[1] == '0' and num[2] == '0':
                result += 'oitocentos'
            else:
                result += 'oitocentos e ' + extenso(int(num[1:]))
        elif num[0] == '9':
            if num[1] == '0' and num[2] == '0':
                result += 'novecentos'
            else:
                result += 'novecentos e ' + extenso(int(num[1:]))

    return result


def main(number):
    num, tam = str(number).strip(), len(str(number).strip())
    result = ''
    if tam <= 3:
        result += extenso(number)

    elif tam % 3 == 0:
        var = int((tam - 3) / 3) - 1
        invlong = longp[var::-1]
        for i in range(0, tam - 3, 3):
            infixo = invlong.pop(0)
            result += extenso(int(num[i:i + 3])) + ' ' + infixo + ' '
        result += extenso(int(num[tam - 3: tam]))
        
    else:
        # Calculara a ordem do numero
        ordem = int((tam - 3) / 3)
        invlong = longp[ordem::-1]

        # Calcular o extenso dos numeros de maior ordem
        if len(num[1:]) % 3 == 0:
            auxnum = num[0]
            num = num[1:]
        else:
            auxnum = num[:2]
            num = num[2:]
        
        result += extenso(int(auxnum)) + ' ' + invlong.pop(0) + ' ' #Se é da ordem de milhoes ->invlong[milhoes, mil]

        # Calcular o extenso do resto dos digitos #calcula o extenso de cada ordem e retira a ordem de invlong
        for i in range(0, tam - 3, 3):
            if len(invlong) != 0:
                infixo = invlong.pop(0)
            else:
                infixo = ''
            result += extenso(int(num[i:i + 3])) + ' ' + infixo + ' '

    print(result)


if __name__ == '__main__':
    main(13456)
