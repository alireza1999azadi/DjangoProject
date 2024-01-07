from django.shortcuts import render,HttpResponse,redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def articles_list(request):
    articles = models.Article.objects.all().order_by('date')
    args= {'articles':articles}
    return render(request , 'articles/articleslist.html',args)

def article_detail(request,slug): #capture
   #return HttpResponse(slug) 
    article1=models.Article.objects.get(slug=slug)#peymayesh dar saf line 12,13
    return render(request,'articles/article_details.html',{'article':article1}) #article1 ro tarif mikonim

@login_required(login_url = '/accounts/login') #login ekhtesassi
def create_article(request):
    if request.method =='POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid:
            instance =form.save(commit=False)
            instance.author=request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request ,'articles/create_article.html',{'form':form})