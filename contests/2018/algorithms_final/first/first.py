#description
"""
В этот жаркий Санкт-Петербургский полдень стажёр Яндекса Аркадий сидел в офисе и вносил последние правки в свою дипломную работу. После нескольких часов тяжких трудов он решил развеяться и прогуляться до торгового автомата на первом этаже, чтобы купить бутылку своего любимого напитка Квас-Класс.

Стоит отметить, что в офисе установлен довольно необычный торговый автомат. Он принимает только монеты достоинством один рубль и купюры достоинством один миллион рублей, и при этом продаёт только бутылки напитка Квас-Класс ценой r рублей за штуку. Изначально у Аркадия есть b банкнот достоинством миллион рублей и c монет по одному рублю. В автомате изначально находятся d рублёвых монет, которыми он может давать сдачу. Процесс покупки одной бутылки напитка устроен следующим образом.

    Аркадий вставляет в автомат x банкнот и y монет, то есть общая загруженная сумма составляет z = 106 ⋅ x + y.
    Затем он нажимает на кнопку совершения покупки. Если z оказывается меньше r, то автомат просит внести ещё денег.
    Если z больше либо равно r, то автомат пытается выдать Аркадию сдачу. Поскольку автомат может выдавать сдачу только монетами, то количество находящихся в нём монет в один рубль (при этом не учитываются монеты, вставленные для совершения именно этой покупки) должно быть не менее z - r. Если монет для выдачи сдачи недостаточно, то покупка не состоится.
    Если z ≥ r и в автомате достаточно монет для того, чтобы выдать Аркадию сдачу (или сдача вообще не требуется, то есть z = r), происходит покупка. Автомат забирает себе x банкнот и y монет (которые могут быть использованы для выдачи сдачи при следующих покупках), после чего возвращает Аркадию z - r монет и выдаёт бутылку желанного напитка.

Хотя Аркадий пришёл купить только одну бутылку, он всё же программист, так что ему интересно, какое максимально количество бутылок он смог бы приобрести, если бы действовал оптимально? Можете считать, что в автомат загружено заведомо достаточное количество бутылок напитка Квас-Класс (что, к сожалению, далеко не всегда выполнено в реальной жизни).
Формат ввода

В первой строке входных данных записаны два целых числа b и c (0 ≤ b, c ≤ 109) — количество банкнот достоинством в один миллион рублей и количество монет в один рубль в распоряжении Аркадия.

Во второй строке записаны два целых числа r и d (1 ≤ r ≤ 109, 0 ≤ d ≤ 109) — цена одной бутылки напитка Квас-Класс и количество монет в торговом автомате до покупок Аркадия. Обратите внимание, что количество купюр внутри автомата значения не имеет.
Формат вывода

Выведите одно целое число равное максимальному количеству бутылок напитка Квас-Класс, которые Аркадий сможет купить если будет действовать оптимально.

"""

#Python 3.6 не поддержвиает set() с порядком, напишем свою set
class Set:
    def __init__(self):
        self.dictionary = {}

    def add(self, elem: int):
        self.dictionary[elem] = ''

    def isExist(self, elem):
        return True if elem in self.dictionary else False

def maxBottles(cost, bills, coins, multiplay = 10**6):
   return (bills*multiplay + coins)//cost

def isPerfectCycle(coins, change, multiplay = 10 ** 6):
    return coins + change > multiplay - 1
def cycleWithSet(func):
    def wrapper(*args):
        def ElemInCoinsSet(dictionary, elem):
            return True if elem in dictionary else False

        cost, bills, coins, change = args

        CoinsSet = Set()
        CoinsSet.add(coins)



        x = 0
        res = True

        while res:
            result = func(cost, bills, coins, change)

            if result:
                bills, coins, change = result

                if ElemInCoinsSet(CoinsSet.dictionary, coins):

                    return True, CoinsSet

                CoinsSet.add(coins)
                x += 1
            else:
                res = False

        return x,

    return wrapper

@cycleWithSet
def getChange(cost, bills, coins, change, multiplay = 10 ** 6):

    if bills * multiplay + coins >= cost:
        costBills = cost // multiplay
        costCoins = cost % multiplay


        if cost <= bills*multiplay:
            if costCoins <= coins:
                change += costCoins
                coins -= costCoins
                bills -= costBills
                return bills, coins, change

            else:
                if costBills + 1 <= bills:
                    if (costBills + 1) * multiplay - cost <= change:
                        change -= ((costBills + 1) * multiplay - cost)
                        coins += ((costBills + 1) * multiplay - cost)
                        bills -= (costBills + 1)
                        return bills, coins, change

        elif coins > cost:
            coins -= cost
            change += cost

        elif bills*multiplay + coins >= cost:
            needed = costBills - bills
            bills = 0

            coins -= (needed*multiplay + costCoins)
            change += (needed*multiplay + costCoins)
            return bills, coins, change



bills, coins = map(int, input().split())
cost, change = map(int, input().split())

#
# 10 700000
# 350000 200000


# 21 1000000
# 1100000 0


if coins + change >= 999999:
    print(maxBottles(cost, bills, coins, multiplay = 10**6))

else:
    result = getChange(cost, bills, coins, change)

    if result[0] == True:
        print(maxBottles(cost, bills, coins, multiplay = 10**6))
    else:
        print(result[0])

