from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #LOGIN
    # path('', views.index_Login,name='index_Login'),
    path('inicio', views.inicio,name='inicio'),
    # path('panelsession',views.panelsession,name='panelsession'),
    # path('cerrarSesionP',views.cerrarSesionP,name='cerrarSesionP'),
    path('', views.userLogin, name='user-login'),
    path('logout/', views.logout_user, name='logout'),

    #PROCESOS
    path('procesos',views.ProcesosListView.as_view(),name='procesos'),
    #path('view_proceso/', views.ProcesosCreateView.index,name='view_proceso'),
    path('crear_proceso/', views.ProcesosCreateView.as_view(),name='crear_proceso'),
    path('editar_proceso/<int:pk>',views.ProcesosUpdateView.as_view(),name='editar_proceso'),
    # path('actualizar_proceso/<int:id_proceso>',views.ProcesosCreateView.actualizar_proceso,name='actualizar_proceso'),
    path('eliminar_proceso/<int:pk>',views.ProcesosDeleteView.as_view(),name='eliminar_proceso'),

     path('detalle_proceso/<int:id>', views.detalle_proceso,name='detalle_proceso'),

    #AUTOMATIZACION PROCESO
    path('automatizacion_proceso/<int:id>', views.automatizacion_proceso,name='automatizacion_proceso'),
    #  ####
     path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
     path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
     path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

    path('lista/', views.ListaProcesosView.as_view(), name='lista'),
    path('listar-procesos/', views.ListProcesosPdf.as_view(), name='procesos_all'),
    # 
    # path('get_programa/', views.get_programa, name='get_programa'),
    # path('get_responsable/<int:programa_id>', views.get_responsable, name='get_responsable'),
    
    
#     path('cities', views.cities, name = "cities")
 ]