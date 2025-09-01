from django.shortcuts import render, redirect
from .forms import AcaoForm
from .models import Acao

def acoes_view(request):
    if request.method == 'POST':
        form = AcaoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva no banco
            return redirect('acoes')  # Redireciona para atualizar a página
    else:
        form = AcaoForm()

    acoes = Acao.objects.all()  # Pega todos os registros do banco
    return render(request, 'acoes.html', {'form': form, 'acoes': acoes})