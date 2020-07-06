import sys

base_words = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'thousand',
        1000000: 'million',
        1000000000: 'billion',
    }

def get_digit_place(num):
    digit_places = {}
    current_place = 1
    while num > 0:
        quotient, remainder = divmod(num, 10)
        digit_places[current_place] = remainder
        num = quotient
        current_place *= 10
    return digit_places


# 345 is three hundred and forty-five
# 59,321 is fifty nine thousand, three hundred and twenty one
# 1,345,612 is one million, three hundred and forty five thousand, six hundred and twelve
# 153,200 is one hundred and fifty three thousand, two hundred


def main(num):
   digit_places = get_digit_place(num)
   pass

if __name__ == '__main__':
    print(main(sys.argv[1]))    
