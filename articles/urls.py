from django.urls import path 
from . import views

app_name="articles" #baraye in k agar dar app digar name list dashtim jango gati nakone #name='list'
urlpatterns = [
    path('' ,views.articles_list,name="list"),
    path ('create',views.create_article , name='create' ),
    path('<slug>',views.article_detail , name='detail') #capture
]
