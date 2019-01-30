from django.contrib import admin
from .models import Question,Comment
# Register your models here.
class QuestionModelAdmin(admin.ModelAdmin): #클레스는 무조건 camelCase
    readonly_fields = ("created_at",)#수정되지않는 시간을 보여주기위해
admin.site.register(Question,QuestionModelAdmin)
admin.site.register(Comment)