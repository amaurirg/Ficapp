from django.shortcuts import render
from ficapp.formularios.forms import FormularioForm


def formulario(request):
	context = {'form': FormularioForm()}
	return render(request, 'formulario.html', context)