from django.shortcuts import render
from myapp.forms import NewUserForm
from myapp.models import MyUser
from myapp.forms import DjangoUserForm,UserProfileInfoForm


# for login
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth import authenticate , login, logout


# Create your views here.


def HomePageView(request):
    return render(request,'myapp/index.html')


def registerView(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid() :
            form.save(commit=True)
            return HomePageView(request)
        else:
            print('form is invalid')
    return render(request, 'myapp/register.html',{'theformfromteplate':form})



def UserListView(request):
    user_list = MyUser.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'myapp/userslist.html',context=user_dict)


def BaseView(request):
    return render(request,'myapp/header_and_footer.html')



def NewuserRegView(request):
    registered = False
    if request.method == "POST":
        user_form = DjangoUserForm(data=request.POST)
        profile_pic_form= UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_pic_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_pic_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                print('found it!')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_pic_form.errors)
    else:
        user_form =DjangoUserForm()
        profile_pic_form = UserProfileInfoForm()

    return render(request,'myapp/newuserreg.html',{'user_form':user_form,'profile_pic_form':profile_pic_form,'registered':registered})

@login_required
def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def loginview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username =username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                return HttpResponse("account isnt active.contact to this email : frosty8312@gmail.com")
        else:
            print('someone tried to login and failed!')
            print("Username : {} , Password : {}".format(username , password))
            return HttpResponse('invalid login details supplied')
    else:
        return render(request,'myapp/login.html',{})
