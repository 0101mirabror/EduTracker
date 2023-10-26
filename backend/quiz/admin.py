from django.contrib import admin

# Register your models here.
from .models import Result, Question, Course

admin.site.register(Result)
admin.site.register(Question)
admin.site.register(Course)