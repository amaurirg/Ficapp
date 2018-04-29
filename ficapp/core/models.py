from django.db import models


class Aplicativos(models.Model):
    aplicativo = models.CharField('Aplicativo', max_length=30)

    class Meta:
        verbose_name = 'Aplicativo'
        verbose_name_plural = 'Aplicativos'
        ordering = ['aplicativo']

    def __str__(self):
        return self.aplicativo


class Combustivel(models.Model):
    combustivel = models.CharField('Tipo de Combustível', max_length=10)

    class Meta:
        verbose_name = 'Combustível'
        verbose_name_plural = 'Combustível'
        ordering = ['combustivel']

    def __str__(self):
        return self.combustivel


class Ganhos_Diarios(models.Model):
    data = models.DateField('Data')
    carro = models.CharField('Carro', max_length=30)
    consumo = models.DecimalField('Consumo(Km/L)', decimal_places=2, max_digits=5)
    combustivel = models.ForeignKey(Combustivel, verbose_name='Combustível', on_delete=models.PROTECT)
    app = models.ForeignKey(Aplicativos, verbose_name='App', on_delete=models.PROTECT)
    horas = models.TimeField('Horas Trabalhadas')
    corridas = models.IntegerField('Corridas')
    cancelados = models.IntegerField('Cancelados')
    recebido = models.DecimalField('Recebido', decimal_places=2, max_digits=6)
    incentivos = models.DecimalField('Incentivos', decimal_places=2, max_digits=6)
    incentivos_pendentes = models.DecimalField('Incentivos Pendentes', decimal_places=2, max_digits=6)
    cancelamentos = models.DecimalField('Cancelamentos', decimal_places=2, max_digits=9)
    total_recebido = models.DecimalField('Total Recebido', decimal_places=2, max_digits=9)
    km_inicial = models.IntegerField('Km Inicial')
    km_final = models.IntegerField('Km Final')
    km_percorrido = models.IntegerField('Km Percorrido')
    comb_l = models.DecimalField('Litros Comb. Gasto', decimal_places=2, max_digits=5)
    valor_comb = models.DecimalField('Valor Comb.', decimal_places=2, max_digits=5)
    total_gasto_comb = models.DecimalField('Total Gasto Comb.', decimal_places=2, max_digits=9)
    preventivo = models.DecimalField('Preventivo', decimal_places=2, max_digits=9)
    extras = models.DecimalField('Extras', decimal_places=2, max_digits=9)
    descricao = models.TextField('Descrição dos Gastos')
    liquido = models.DecimalField('Líquido', decimal_places=2, max_digits=9)

    class Meta:
        verbose_name = 'Ganho Diário'
        verbose_name_plural = 'Ganhos Diários'
        ordering = ['data']
