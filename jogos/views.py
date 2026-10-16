from django.shortcuts import get_object_or_404, render
from .models import Equipe, Modalidade

def index(request):
    equipes = Equipe.objects.all()
    modalidades = Modalidade.objects.all()
    return render(request, 'jogos/index.html', {'equipes': equipes, 'modalidades': modalidades})

def equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, id=equipe_id)
    return render(request, 'jogos/equipe.html', {'equipe': equipe})

def modalidade(request, modalidade_id):
    modalidade = get_object_or_404(Modalidade, id=modalidade_id)
    return render(request, 'jogos/modalidade.html', {'modalidade': modalidade})