from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'buter_2': {
        'хлебббббббб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def index(request):
    template_name = "calculator/index.html"
    i = request.path[1:-1]
    if request.GET.get('serving') != None:
        n = int(request.GET.get('serving'))
        data = DATA[i]
        for ingr, quant in data.items():
            data[ingr] = quant * n
        context = {
            'recipe': data
        }
        return render(request, template_name, context)
    else:
        context = {
            'recipe': DATA[i]
        }
        return render(request, template_name, context)
    # Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }