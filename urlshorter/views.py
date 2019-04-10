from django.shortcuts import render,redirect
from django.views import View
from .judge import IsRE
from .transfer import get_hash_key
from .models import *
from .visit_time import *
from django.http import HttpResponse

# Create your views here.


hashes = {}


def post(request):
    visit_time(request) #访问计数
    urls = request.POST.get('url')
    short_link = ''
    if request.method == 'POST':
        if not urls:
            #防空处理
            return HttpResponse('网站不能为空')
        if IsRE(urls):
            #判断网站格式是否正确
            links = Link.objects.filter(url=urls)
            if links.count() == 0:
                su = get_hash_key(urls)[0]
                short_url = 'https://'+(su) #长url转化成短url
                if hashes.get(su):
                    a = 1
                else:
                    hashes[su] = short_url #字符串和短url映射
                link = Link.objects.create(url=urls, short_link=short_url)
                link.save()
        short_link += Link.objects.get(url=urls).short_link
    return render(request, '1.html', {'short_link':short_link})


def redirect_short(request):
    short_url = request.POST.get('short_url')
    if request.method == 'POST':
        if not short_url:
            #防空处理
            return HttpResponse('网站不能为空')
        link = Link.objects.filter(short_link=short_url)
        if link:
            return redirect(link[0].url)
    return render(request, '2.html')