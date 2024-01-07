from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#for add article to site with this subect's
class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(default='default.jpg',blank=True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    
    #for view title instans to forexample article1 , article 2,....
    def __str__(self):
        return self.title

#for view to 40 character from passage & else inner article or object
    def snippet(self):  
        return self.body[:40] + '....' 


#forever change to article necesary to migrate & migrations 