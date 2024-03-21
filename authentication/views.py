from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST";
        # username = request.POST.get('username')
        username = request.POST['username']
        pnom = request.POST['pnom']
        fnom = request.POST['fnom']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(userename, tel, pass1)
        myuser.prenom = pnom
        myuser.nom_de_famille = fnom

        myuser.save()

        messages.success(request, "Bravo!!!!!! Ton compte a ete cree avec succes. Bienvenue dans la BBB communaute")

        return redirect('signin')


    return render(request, "authentication/signup.html")

def signin(request):

    if request.method =='POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user =authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            pnom = user.prenom

            return render(request, "authentication/index.html",{'pnom':pnom})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')


    return render(request, "authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request, "deconnection reussi!")
    return redirect('home')

