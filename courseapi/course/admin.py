from django.contrib import admin
from course.models import Category,Course,User,Lesson
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class LessonForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

# Register your models here.
class MyCourseAdmin(admin.ModelAdmin):
    form = LessonForm
admin.site.register(Category)
admin.site.register(Course, MyCourseAdmin)
admin.site.register(User)
admin.site.register(Lesson)




