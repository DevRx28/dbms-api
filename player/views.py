from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from .models import Player
from django.core.paginator import Paginator

@csrf_exempt
def basic_view(request):
    if request.method == 'POST':
        players = Player.objects.all()

        # Set search parameters
        try:
            Name = request.POST['PlayerName']
            if Name != '':
                players = players.filter(Name=Name)
        except KeyError:
            pass

        try:
            Age = request.POST['Age']
            players = players.filter(Age=Age)
        except KeyError:
            pass
        except ValueError:
            pass

        try:
            Nationality = request.POST['Nationality']
            if Nationality != '':
                players = players.filter(Nationality=Nationality)
        except KeyError:
            pass

        try:
            Club = request.POST['Club']
            if Club != '':
                players = players.filter(Club=Club)
        except KeyError:
            pass

        try:
            Position = request.POST['Position']
            if Position != '':
                players = players.filter(Position=Position)
        except KeyError:
            pass

        try:
            Overall = request.POST['Overall']
            players = players.filter(Overall__gte=Overall)
        except KeyError:
            pass
        except ValueError:
            pass

        try:
            Potential = request.POST['Potential']
            players = players.filter(Potential=Potential)
        except KeyError:
            pass
        except ValueError:
            pass


        try:
            WeakFoot = request.POST['WeakFoot']
            players = players.filter(WeakFoot=WeakFoot)
        except KeyError:
            pass
        except ValueError:
            pass

        try:
            SkillMoves = request.POST['SkillMoves']
            players = players.filter(SkillMoves=SkillMoves)
        except KeyError:
            pass
        except ValueError:
            pass
        
        try:
            PreferredFoot = request.POST['PreferredFoot']
            if PreferredFoot != '':
                players = players.filter(PreferredFoot=PreferredFoot)
        except KeyError:
            pass

        try:
            InternationalReputation = request.POST['InternationalReputation']
            players = players.filter(InternationalReputation=InternationalReputation)
        except KeyError:
            pass
        except ValueError:
            pass

        # Generating output
        player_list = list(players)
        # player_list = Paginator(players, 50)
        print(player_list)

        context = {
			'results': 'yes',
			'some_list': player_list
		}
        
        return render(request, 'players.html', context)
    else:
        return render(request, 'players.html')
