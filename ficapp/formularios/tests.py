from django.test import TestCase
from ficapp.formularios.forms import FormularioForm


class FormularioTest(TestCase):
	def setUp(self):
		self.resp = self.client.get('/formulario/')

	def test_get(self):
		"""Retornar status_code = 200"""
		self.assertEqual(200, self.resp.status_code)

	def test_template(self):
		"""Precisa usar formulario.html"""
		self.assertTemplateUsed(self.resp, 'formulario.html')

	def test_html(self):
		"""Precisa conter tags do input"""
		self.assertContains(self.resp, '<form')
		self.assertContains(self.resp, '<input', 20)
		self.assertContains(self.resp, 'type="text"', 5)
		self.assertContains(self.resp, 'type="number"', 13)
		self.assertContains(self.resp, 'type="submit"')

	def test_csrf(self):
		"""Precisa conter csrf"""
		self.assertContains(self.resp, 'csrfmiddlewaretoken')

	def test_has_form(self):
		"""O contexto precisa conter form=formulario"""
		form = self.resp.context['form']
		self.assertIsInstance(form, FormularioForm)

	def test_form_has_fields(self):
		"""Formulário precisa conter 19 campos"""
		form = self.resp.context['form']
		self.assertSequenceEqual(['data', 'carro', 'consumo', 'combustivel', 'app', 'horas', 'corridas',
		                          'cancelados', 'recebido', 'incentivos', 'incentivos_pendentes', 'cancelamentos',
		                          'total_recebido', 'km_inicial', 'km_final', 'km_percorrido',
		                          'valor_combustivel', 'extras', 'descricao'], list(form.fields))