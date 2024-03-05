from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField


# Create your models here.

class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    activate = models.BooleanField(default=True)

    class Meta:
        abstract = True


class User(BaseModel):
    name = models.CharField(max_length=255)


class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(BaseModel):
    name = models.CharField(max_length=50)
    description = RichTextField()
    image = models.ImageField(upload_to='course/%Y/%m/', null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Lesson (BaseModel):
    subject = models.CharField(max_length= 255)
    content = RichTextField()
    image = models.ImageField(upload_to='course/%Y/%m/', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject


class Interaction (BaseModel):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        abstract = True



