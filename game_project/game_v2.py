import numpy as np

def random_predict(number: int = 1) -> int:
    """Угадываем число с помощью бинарного поиска."""
    count = 0
    low = 1
    high = 100

    while True:
        count += 1
        predict = (low + high) // 2

        if predict == number:
            return count
        elif predict < number:
            low = predict + 1
        else:
            high = predict - 1


def score_game(predict_function) -> int:
    """Запускаем игру 1000 раз, чтобы узнать среднее количество попыток."""
    random_array = np.random.randint(1, 101, size=1000)
    count_ls = []

    for number in random_array:
        count_ls.append(predict_function(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score


if __name__ == "__main__":
    score_game(random_predict)
