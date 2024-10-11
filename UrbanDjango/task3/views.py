from django.shortcuts import render


# Create your views here.
def game_platform(request):
    return render(request, 'third_task/platform.html')


def games(request):
    games = {
        'first': 'Atomic Heart',
        'second': 'Cyberpunk',
        'third': 'PayDay2'
         }
    return render(request, 'third_task/games.html', context=games)


def cart(request):
    return render(request, 'third_task/cart.html')


