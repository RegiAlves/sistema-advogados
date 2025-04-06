from django.shortcuts import render, redirect
from .forms import ProcessoForm
from .forms import CompromissoForm

def cadastrar_processo(request):
    if request.method == 'POST':
        form = ProcessoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ProcessoForm()

    return render(request, 'processos/cadastrar_processo.html', {'form': form})

def cadastrar_compromisso(request):
    if request.method == 'POST':
        form = CompromissoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  # Pode trocar pela página que quiser
    else:
        form = CompromissoForm()

    return render(request, 'processos/cadastrar_compromisso.html', {'form': form})