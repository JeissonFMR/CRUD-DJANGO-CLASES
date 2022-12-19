from contextlib import nullcontext
from distutils.command.clean import clean
from filecmp import clear_cache
from multiprocessing import context
from operator import truediv
import re
from turtle import clear, pos
from urllib import request
from django.http import HttpResponse, HttpRequest
from genericpath import exists
from django.views.generic import ListView, View, CreateView, UpdateView, DeleteView

from django.shortcuts import get_object_or_404, redirect, render

from .models import   *
from django.contrib import messages
from .forms import ProcesosFormulario
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from software_caracterizacion.utils import render_to_pdf
from django.http import JsonResponse


from django.urls import reverse_lazy
import json
#PDF
class ListaProcesosView(ListView):
    model = Procesos
    template_name = "report/pdf.html"
    context_object_name = 'procesos'

class ListProcesosPdf(View):
    def get(self, request, *args, **kwargs):
        procesos = Procesos.objects.filter(user=request.user)
        data = {
            'procesos': procesos
        }
        
        pdf = render_to_pdf('report/lista.html', data)
        
        return HttpResponse(pdf, content_type='application/pdf')
#PDF
# Create your views here.
@login_required(login_url="user-login")
def inicio(request):
    return render(request, 'login/inicio.html')

#LOGIN
def index_Login(request):
    return render(request, 'login/index_Login.html')


def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            
            login(request, user)
            
            return redirect('inicio')
        else:
            messages.warning(request,'No te has identificado correctamente.')
    return render(request,'login/index_Login.html')

def logout_user(request):
    logout(request)
    return redirect('user-login')

# def cities(request):
#     data = json.loads(request.body)
#     cities = City.objects.filter(country__id=data['user_id'])
#     print(cities)
#     return JsonResponse(list(cities.values("id", "name")), safe=False)

@login_required(login_url="user-login")
def detalle_proceso(request, id):
    #proceso = Procesos.objects.get(pk=ide_pro)
    proceso = get_object_or_404(Procesos, pk=id)
    return render(request,'procesos/detallemodal.html', {'proceso': proceso})

# automatizacion proceso
@login_required(login_url="user-login")
def automatizacion_proceso(request, id):
    proceso = get_object_or_404(Procesos, pk=id)
    
    print("SI PASAAAAAAAAAAAAAA por fueraaaaaaaaa")
    if request.method == 'POST':
        print("SI PASAAAAAAAAAAAAAA editaaaaaaaaaar")
        form_procesos = ProcesosFormulario(request.POST, instance=proceso)
        if form_procesos.is_valid():
            form_procesos.save()
            messages.success(request, 'Proceso editado correctamente')
            return redirect('procesos')
    else:
        # crear nuevoi objeto
        print("SI PASAAAAAAAAAAAAAA222")
        form_procesos = ProcesosFormulario(instance=proceso)
    return render(request, 'procesos/automatizar/detalles_Automatizar.html', {'form_procesos': form_procesos, 'proceso': proceso})
    # proceso = get_object_or_404(Procesos, pk=id)
    #return render(request,'procesos/automatizar/detalles_Automatizar.html', {'proceso': proceso})


# def get_programa(_request):
#     programas = list(Programa.objects.values())

#     if (len(programas) > 0):
#         data = {'message': "Success", 'programas': programas}
#     else:
#         data = {'message': "Not Found"}

#     return JsonResponse(data)


# def get_responsable(_request, programa_id):
#     responsables = list(Responsable.objects.filter(programa_id=programa_id).values())

#     if (len(responsables) > 0):
#         data = {'message': "Success", 'responsables': responsables}
#     else:
#         data = {'message': "Not Found"}

#     return JsonResponse(data)


##CLASES
class ProcesosListView(ListView):
    model = Procesos
    template_name = 'procesos/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Procesos.objects.filter(user= self.request.user)
        context['numero_procesos'] = Procesos.objects.filter(user= self.request.user).count()
        return context

class ProcesosCreateView(CreateView):
    model = Procesos
    form_class = ProcesosFormulario
    template_name = 'procesos/crear.html'
    success_url: reverse_lazy('procesos: procesos')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
class ProcesosUpdateView(UpdateView):
    model = Procesos
    form_class = ProcesosFormulario
    template_name = 'procesos/editar.html'
    success_url: reverse_lazy('procesos: procesos')
    
class ProcesosDeleteView(DeleteView):
    model = Procesos
    template_name = 'procesos/procesos_confirm_delete.html'
    success_url = '/procesos'