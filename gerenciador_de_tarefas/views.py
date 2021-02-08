import os, time, psutil
from datetime import datetime, timezone
from django.shortcuts import render 
from django.http import HttpResponse

class InfoArquivos():
    def __init__(self, nome, tamanho, atime, mtime):
        self.nome = nome
        self.tamanho = tamanho//1024
        self.atime = datetime.fromtimestamp(atime, tz=timezone.utc).strftime('%d/%m/%Y-%H:%M')
        self.mtime = datetime.fromtimestamp(mtime, tz=timezone.utc).strftime('%d/%m/%Y-%H:%M')

def arquivos(request):
    caminho = "C:\\Users\Pedro Fonseca\Downloads"
    lista_arquivos = os.listdir(caminho)

    lista = []

    for arquivo in lista_arquivos:
        caminho_arquivo = os.path.join(caminho, arquivo)
        if os.path.isfile(caminho_arquivo):
            arquivo_stat = os.stat(caminho_arquivo)
            info = InfoArquivos(nome=arquivo, 
            tamanho=arquivo_stat.st_size, 
            atime=arquivo_stat.st_atime, 
            mtime=arquivo_stat.st_mtime)
            lista.append(info)
    context = {"lista" : lista}
    return render(request, 'lista_arquivos.html', context)

def processos(request):
    processos = []
    for p in psutil.process_iter():
        processos.append(p.as_dict(attrs=['pid', 'name', 'status', 'cpu_times', 'memory_info']))
    context = {"processos" : processos}
    return render(request, 'lista_processos.html', context)

def detalhar(request, pid):
    context = {"processo" : psutil.Process(pid)}
    return render(request, 'detalhar.html', context)