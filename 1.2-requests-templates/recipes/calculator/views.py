from django.shortcuts import render
from django.http import HttpResponse
from random import choice
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def home_view(request):
    reci = ", ".join(DATA.keys())
    return HttpResponse(f'Введите в адресной рецепт (например: /pasta) и количество блюд (например: /pasta?servings=4). '
                        f'Доступные рецепты: {reci}.')


def quantity(request, rec):
    quan = request.GET.get("servings")
    if quan:
        data_copy = DATA[rec].copy()    # Копия данных DATA
        for i in data_copy.keys():      # Цикл модифицирует ингридиенты копии DATA по количеству порция
            data_copy[i] *= int(quan)
        context = {
            'recipe': data_copy
        }
        return render(request, 'calculator/index.html', context)
    else:
        context = {
            'recipe': DATA[rec]
        }
        return render(request, 'calculator/index.html', context)

