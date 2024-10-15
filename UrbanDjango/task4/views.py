from django.shortcuts import render


def game_platform(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
    variables = {
        'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay']
    }
    return render(request, 'fourth_task/games.html', context=variables)


def cart(request):
    return render(request, 'fourth_task/cart.html')