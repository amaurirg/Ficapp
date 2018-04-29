from django import forms


class FormularioForm(forms.Form):
	data = forms.DateField(label='Data')
	carro = forms.CharField(label='Carro', max_length=30)
	consumo = forms.DecimalField(label='Consumo(Km/L)', decimal_places=2, max_digits=5)
	combustivel = forms.DecimalField(label='Combustível', decimal_places=2, max_digits=6)
	app = forms.CharField(label='App')
	horas = forms.TimeField(label='Horas Trabalhadas')
	corridas = forms.IntegerField(label='Corridas')
	cancelados = forms.IntegerField(label='Cancelados')
	recebido = forms.DecimalField(label='Recebido', decimal_places=2, max_digits=6)
	incentivos = forms.DecimalField(label='Incentivos', decimal_places=2, max_digits=6)
	incentivos_pendentes = forms.DecimalField(label='Incentivos Pendentes', decimal_places=2, max_digits=6)
	cancelamentos = forms.DecimalField(label='Cancelamentos', decimal_places=2, max_digits=9)
	total_recebido = forms.DecimalField(label='Total Recebido', decimal_places=2, max_digits=9)
	km_inicial = forms.IntegerField(label='Km Inicial')
	km_final = forms.IntegerField(label='Km Final')
	km_percorrido = forms.IntegerField(label='Km Percorrido')
	valor_combustivel = forms.DecimalField(label='Valor Comb.', decimal_places=2, max_digits=5)
	extras = forms.DecimalField(label='Extras', decimal_places=2, max_digits=9)
	descricao = forms.CharField(label='Descrição dos Gastos', widget=forms.Textarea())
