from django.contrib import admin

# Register your models here.


from computiq.models import *


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'points', 'seconds')
    list_filter = ('category__category_title',)
    search_fields = ('title',)
    
@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'title', 'isTrue')
    search_fields = ('question', 'title')
    list_filter = ('isTrue',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_title','category_image','category_descrition')
    search_fields = ('category_title','category_descrition')    
