"""
    取一个任意小于1 美元的金额，然后计算可以换成最少多少枚硬币。硬币有1
    美分，5 美分，10 美分，25 美分四种。1 美元等于100 美分。举例来说，0.76 美元换算结果
    应该是 3 枚25 美分，1 枚1 美分。类似76 枚1 美分，2 枚25 美分+2 枚10 美分+1 枚5 美分+1
    枚1 美分这样的结果都是不符合要求的。
"""
import random


def exchange(dollar):
    dollars = int(100 * dollar)
    print("%.2f美元为%d美分" % (dollar, dollars))
    meifens = [25, 10, 5, 1]
    mappingResult = {}
    while dollars > 0:
        for meifen in meifens:
            dollars = exchange_adv(dollar, dollars, meifen, mappingResult)
            if dollars == 0:
                break
    # print(mappingResult)
    return mappingResult


def exchange_adv(dollar, dollars, meifen, mappingResult):
    n = dollars % meifen
    count = dollars // meifen
    if n == 0:
        mappingResult[meifen] = count
        print("%.2f美元可以兑换%d个%d美分硬币" % (dollar, count, meifen))
        dollars = 0
    else:
        if count > 0:
            mappingResult[meifen] = count
            print("%.2f美元可以兑换%d个%d美分的硬币" % (dollar, count, meifen))
        dollars -= count * meifen
    return dollars


if __name__ == '__main__':
    for num in range(50):
        dollor = round(random.random(), 2)
        mapping = exchange(dollor)
        total = 0
        for key, value in mapping.items():
            total += key * value
        print(total)
        if total == int(dollor * 100):
            print('yeah.....good')
