from django.shortcuts import render


def game_platform(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
    list = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay']
    context = {
        'games': list
    }
    return render(request, 'fourth_task/games.html', context)


def cart(request):
    return render(request, 'fourth_task/cart.html')