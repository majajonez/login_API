import time
from time import perf_counter_ns

# wypisanie nazwy wywolanej funkcji
# wypisanie parametrow
# wypisanie wyniku funkcji
# wypisanie czasu wykonania funkcji

def debug(funkcja):
    def wewnetrzna(*args):
        print("naza f: " + str(funkcja.__name__))           # wypisanie nazwy wywolanej funkcji
        t = perf_counter_ns()
        w = funkcja(*args)
        t = perf_counter_ns() - t
        print('parametry funkcji:')
        for a in args:
            print(a)                                        # wypisanie parametrów funkcji
        print("wynik: " + str(w))                           # wypisanie wyniku funkcji
        print("czas w milisekundach: " + str(t /1000000))      # czas wykonywania funkcji
        return w
    return wewnetrzna


@debug
def f_do_dekorowania(m, n):
    print("wewnatrz dupa")
    a = 2 + m
    b = 3 + n
    return a


def razy2(f):
    x = 2 * f
    return x

def zawsze1(f):
    def cos():
        return 1
    return cos

def witaj(f):
    def srodek():
        print("hello")
        return f()
    return srodek


def zawsze2():
    return 2

def kaczka():
    print("kaczka")


# print(dupa(2))
# print("==============")
# print(razy2(dupa)(2))

# wynik = witaj(kaczka)
# print('==========')
# wynik()
# wynik()

f_do_dekorowania(2, 3)

# def wypisz_duzo(n):
#     def stary_wypisz_duzo(f):
#         def wewnetrzna():
#             for i in range(n):
#                 f()
#
#         return wewnetrzna
#     return stary_wypisz_duzo
#
# @wypisz_duzo(4)
# def blabla():
#     print('blabla')
#
# blabla()