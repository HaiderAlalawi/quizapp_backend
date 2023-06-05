import uuid
from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    category_title=models.CharField(max_length=255)
    category_image=models.ImageField(upload_to='images/categories')
    category_descrition=models.CharField(max_length=1000, blank=True, null=True)


    def __str__(self):
        return self.category_title



class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,auto_created=True)
    title=models.CharField(max_length=500)
    points=models.IntegerField()
    seconds=models.IntegerField()
    category=models.ForeignKey(Category, related_name='category',on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}".format(self.title)


class Answer(models.Model):
    question=models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    title=models.CharField(max_length=255,verbose_name='answer')
    isTrue=models.BooleanField(default=False)
    def __str__(self):
            return "{}".format(self.title)

