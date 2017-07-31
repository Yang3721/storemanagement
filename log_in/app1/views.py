from django.shortcuts import render
from .models import Staff, all_object,ReturnManagement
from .forms import UserForm, SearchForm,BorrowForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.db.models import Q
from django.forms.models import model_to_dict


# Create your views here.
def login(request):
    if request.method == 'POST':

        #ue = request.POST.get("username")
        #up = request.POST.get("password")
        uf = UserForm(request.POST)
        #ant = {}
        #ant['head'] = ue
        #return render(request, 'test1.html', ant)
        if uf.is_valid():

            #return HttpResponseRedirect('/main/')
            ue = uf.cleaned_data['username']
            up = uf.cleaned_data['password']
            #user = authenticate(username=ue, password=up)

            #ue = request.POST.get("username")
            #ant = {}
            #ant['head'] = ue
            #return render(request, 'test1.html', ant)
            #up = request.POST.get("password")
            user = Staff.objects.filter(name__exact=ue, password__exact=up)
            #user = list(user)
            #ant = {}
            #ant['head'] = user
            #return render(request, 'test1.html', ant)
            #u = user.objects.get(name=ue)
            #u_dict = model_to_dict(user)
            #mark = u_dict.remarks(name=ue)
            if user:
            # login(request,user)
                return render(request, 'main.html')
                #return HttpResponseRedirect('/main/')
            #elif mark == '无':
                #return HttpResponseRedirect('/login/')
                #return render(request, 'main_normal.html')
            else:
                return HttpResponseRedirect('/login/')
        else:

            return HttpResponseRedirect('/error/')
    else:
        return render(request, 'login.html')


def main(request):
    if request.method == 'POST':
        mf = SearchForm(request.POST)
        if mf.is_valid():
            kw = mf.cleaned_data['keyword']
            materials = all_object.objects.filter(Q(name__icontains=kw) | Q(type__icontains=kw) | Q(modelNum__icontains=kw) | Q(roomNum__icontains=kw) | Q(location__icontains=kw) | Q(department__icontains=kw) | Q(serialNum__icontains=kw) | Q(mountingNum__icontains=kw))
            #materials = 'a'
            ele = {}
            ele['head'] = materials
            if materials:
                return render(request,'main.html',ele)
            else:
                return render(request,'main.html',{'head':'No result.'})

        else:
            render(request, 'error.html')
        return render(request, 'main.html')
    else:
        return render(request, 'error.html')


def base_return(request):
    if request.method == 'POST':
        flag = request.POST.get('flag')
        if flag:
            return render(request,'return.html')
        bf = BorrowForm(request.POST)
        if bf.is_valid():
            bm = bf.cleaned_data['borrow_message']
            return_list = ReturnManagement.objects.filter(Q(formNum_de__icontains=bm) | Q(operator_re__icontains=bm))
            ele = {}
            ele['head'] = return_list
            if return_list:
                return render(request,'return.html',ele)
            else:
                return render(request,'return.html',{'head':'No result.'})

        else:
            render(request, 'error.html')
    else:
        return render_to_response('return.html', locals())



