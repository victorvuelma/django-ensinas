from django.shortcuts import render, redirect
from app.models import Estudante, Materia, Mentor, Solicitacao
from app.auth import mentor_auth

def home(request):
	return redirect('app_mentor_solicitacoes')

def solicitacoes(request):
	mentor = mentor_auth.get(request)
	
	if mentor is not None:
		solicitacoes = Solicitacao.objects.filter(mentor=mentor, oculto=False)

		return render(request, 'mentor_solicitacoes.html', {
			'mentor': mentor,
			'solicitacoes': solicitacoes
		})
	return redirect('app_auth_login')