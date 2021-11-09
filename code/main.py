import time

import matplotlib.pyplot as plt
from loguru import logger

# region logger
logger.remove()
logger.info("старт программы")
# endregion loggin
plt.figure("График")
plt.grid()


def dec(func):
    '''Деократор чтобы узнать время выполнения функции'''

    def decorator(*args):
        start_time = time.time()
        f = func(*args)
        print(f"время работы = {time.time() - start_time}")
        return f

    return decorator


def file_in() -> (list, list):
    logger.info("Вызванна функция file_in")
    with open("../text/in_file_wiki.txt", "r") as file:
        in_list = file.readlines()
    in_list = [i for i in in_list if "%" not in i]
    in_list = [i.removesuffix("\n") for i in in_list]
    in_list = [i.split() for i in in_list]
    x = [i[0] for i in in_list]
    y = [i[1] for i in in_list]
    x = list(map(float, x))
    y = list(map(float, y))

    ######обрезание начального списка
    # x = x[10000:30000]
    # y = y[10000:30000]
    # x = x[0:10]
    # y = y[0:10]
    ######

    logger.info(f"Количество элементов: {len(x)}")
    # logger.info(f"x= {x}")
    # logger.info(f"y= {y}")
    logger.info("file_in exit")
    return x, y


def file_out(out_x: list, out_y: list) -> None:
    logger.info("Вызвана функция file_out")
    out_x = list(map(str, out_x))
    out_y = list(map(str, out_y))
    out = [f"{out_x[i]} {out_y[i]}\n" for i in range(len(out_x))]
    # logger.info(f"{out=}")
    with open("../text/out_file.txt", "w") as file:
        file.writelines(out)
    logger.info("file_out exit")


def paint_plot(x: list, y: list, name="Название не указано") -> None:
    logger.info("Вызванна функция paint_plot")
    plt.plot(x, y, label=name)
    plt.legend()
    logger.info("paint_plot exit")


def f(x: list, y: list, window: int) -> (list, list):
    if window >= len(x) or window in (0, 1) or window % 2 == 0:
        logger.error(
            "ОШИБКА: Некоректная длина окна. Длина окна должна быть целым, положительным, нечётным числом не равным 0, 1 и не больше длины списка.")
        print(
            "ОШИБКА: Некоректная длина окна.\n Длина окна должна быть целым, положительным, нечётным числом не равным 0, 1 и не больше длины списка.\n")
        exit()
    logger.info("Вызванна функция f")
    out_x = []
    out_y = []
    shag = window - 1 - int(window / 2)
    logger.info(f"{window=}")
    logger.info(f"shag={shag}")
    logger.info(f"первый элемент: {x[shag]}")
    for i in range(window - 1 - int(window / 2), len(y) - shag):
        sum = 0
        out_x.append(x[i])
        for j in range(i - shag, i + shag):
            sum += y[j]
        sum /= window
        out_y.append(sum)
    file_out(out_x, out_y)
    # logger.info(f"{out_x=}")
    # logger.info(f"{out_y=}")
    logger.info("f exit")
    return out_x, out_y


in_x, in_y = file_in()
# window = int(input("введите ширину окна"))
window = 5

paint_plot(in_x, in_y, "Исходный график")
out_x, out_y = f(in_x, in_y, window)
paint_plot(out_x, out_y, f"Новый график: окно={window}")
# for i in range(51, 551, 50):
#     out_x, out_y = f(in_x, in_y, i)
#     paint_plot(out_x, out_y, f"Новый график: окно={i}")
logger.info("Конец программы\n")
plt.show()
