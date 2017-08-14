from __future__ import unicode_literals
from .models import Staff, all_object, ReturnManagement
from .forms import UserForm, SearchForm
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render_to_response
from django.db.models import Q
# from django.core import serializers
# from django.forms.models import model_to_dict


# Create your views here.
# -*- coding: utf-8 -*-

import json
from django.shortcuts import render


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
            materials = materials.values()
            #materials = list(materials)
            #result_dict = model_to_dict(materials)
            #result_dict = {}
            #title = ['name', 'type', 'modelNum', 'roomNum', 'state', 'number', 'location', 'department', 'meteringNum', 'useLife', 'serialNum', 'countingUnit', 'coreNum', 'measurement', 'mountingNum', 'threshold', 'remarks']
            #for i in range(len(materials)):
                #materials[i] = model_to_dict(materials[i])
            ele = {}
            a = len(materials)
            i = 0
            if i < a:
                ele['库房编号'] = materials[i]['meteringNum']
                ele['名称'] = materials[i]['name']
                ele['类型'] = materials[i]['type']
                ele['型号'] = materials[i]['serialNum']
                ele['库存状态'] = materials[i]['state']
                ele['库存数量'] = materials[i]['number']
                ele['存放地点'] = materials[i]['location']
                ele['备注'] = materials[i]['remarks']
                i = i + 1
                if ele:
                    return render(request, 'main.html', ele)
                else:
                    return render(request, 'main.html',ele)
            else:
                return render(request, 'main.html', ele)

            #materials = serializers.serialize('json', materials)


        else:
            render(request, 'error.html')
        return render(request, 'main.html')
    else:
        return render(request, 'error.html')


def base_return(request):
    #if request.method == 'POST':
        #flag = request.POST.get('flag')
        #if flag:
            #return render(request,'return.html')
        #bf = BorrowForm(request.GET)
    if 'borrow_message' in request.GET:
        key= request.GET['borrow_message']
        if key:
            #bm = bf.cleaned_data['borrow_message']
            return_list = ReturnManagement.objects.filter(Q(formNum_de__icontains=key) | Q(operator_re__icontains=key))
            return_list = return_list.values()
            ele = {}
            #result_dict = model_to_dict(return_list)
            #result = return_list.values_list()
            a = len(return_list)
            i = 0
            if i < a:
                ele['单号'] = return_list[i]['formNum_de']
                ele['借出人'] = return_list[i]['operator_re']
                ele['借出日期'] = return_list[i]['deliveryDate']
                i = i + 1
                if ele:
                    return render(request,'return.html',ele)
                else:
                    return render(request, 'return.html')
            else:
                return render(request,'return.html',ele)

        else:
            render(request, 'error.html')
    else:
        return render_to_response('return.html', locals())



