from django.contrib import admin

# Register your models here.


from computiq.models import *


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['id','title','category', 'points', 'seconds']
    search_fields = ['id','title']
    
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id','question', 'title', 'isTrue']
    search_fields = ['id']
    list_filter = ['isTrue','question']
    ordering = ['question']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title','category_image','category_descrition']
    search_fields = ['category_title']
