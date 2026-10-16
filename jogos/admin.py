from django.contrib import admin
from .models import Modalidade, Tecnico, Equipe, Atleta


class AtletaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'equipe')
    search_fields = ('nome',)
    list_filter = ('equipe','modalidade')

admin.site.register(Atleta, AtletaAdmin)

class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'curso', 'atletas_count', 'tecnico')
    search_fields = ('nome',)
    list_filter = ('curso','tecnico')

admin.site.register(Equipe, EquipeAdmin)


admin.site.register(Modalidade)


admin.site.register(Tecnico)