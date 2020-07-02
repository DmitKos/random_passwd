import string
import random


def random_passwd(num: int = 8):
    list_words_digits = list((string.ascii_letters) + (string.digits) + (string.punctuation))
    r = random.choices(list_words_digits, k=num)
    print(''.join(map(str, r)))
