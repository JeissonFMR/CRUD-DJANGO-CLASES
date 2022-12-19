from django.contrib import admin
from .models import   Procesos, Programa, Responsable, TipoProceso, Country, City
# Register your models here.

# Register your models here.
#PARA EL ADMINISTRADOR





# class ProcesosAdmin(admin.ModelAdmin):
    
#     def save_model(self, request, obj, form, change):
#         if not obj.user_id:
#             obj.user_id = request.user.id
#         obj.save()

admin.site.register(Procesos)
admin.site.register(TipoProceso)
admin.site.register(Programa)
admin.site.register(Responsable)

admin.site.register([Country, City])