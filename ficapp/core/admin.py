from django.contrib import admin
from .models import Aplicativos, Combustivel, Ganhos_Diarios


class Ganhos_DiariosAdmin(admin.ModelAdmin):
    list_display = ['data', 'app', 'horas', 'corridas', 'total_recebido', 'km_percorrido',
                    'total_gasto_comb', 'preventivo', 'extras', 'liquido']
    search_fields = ['data', 'app']
    list_filter = ['data', 'app']


admin.site.register(Aplicativos)
admin.site.register(Combustivel)
admin.site.register(Ganhos_Diarios, Ganhos_DiariosAdmin)
