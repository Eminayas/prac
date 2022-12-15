from django.shortcuts import render 
from .forms import formUsuarios

# Create your views here.
def home (request):
    return render(request, 'index.html')

def tasks(request):
    return render(request, 'tasks.html')

def Estudiante(request):
    form = formUsuarios()

    return render(request, '_estudiante.html', {'form': form})



def usuario(request):

    if request.method == 'POST':
    
        N_Identificacion = request.POST['txtid']
        T_Identificacion = request.POST['txtidt']
        Nombre = request.POST['txtnom']
        Apellido_P = request.POST['txtapep']
        Apellido_M = request.POST['txtapem']
        Fecha_Nac = request.POST['txtfnca']
        Usu_Django = request.POST['fnac']
        Ciudad = request.POST['fnac']
        Telf_Celular = request.POST['fnac']

        usuario = usuario.objects.create(
         N_Identificacion=N_Identificacion, T_Identificacion=T_Identificacion, Nombre=Nombre, Apellido_P=Apellido_P, Apellido_M=Apellido_M,
         Fecha_Nac=Fecha_Nac, Usu_Django=Usu_Django, Pais=Pais, Provincia=Provincia, Ciudad=Ciudad, Telf_Celular=Telf_Celular)
        messages.success(request, '¡Usuario registrado!')

        return render(request, '_usuario.html')
        
    else:

        return render(request, '_usuario.html')