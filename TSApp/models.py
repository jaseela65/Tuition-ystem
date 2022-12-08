from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

def validate_capitalized(value):
    if value != value.capitalize():
        raise ValidationError('Invalid (not capitalized) value: %(value)s',
                              code='invalid',
                              params={'value': value})

# Create your models here.
class TSclass(models.Model):
    classes=models.TextField()
    syllabus=models.TextField()

    def __str__(self):
        return self.classes
   



class TSsubject(models.Model):
    subject=models.TextField()

    def __str__(self):
        return self.subject

    


class TSteacher(models.Model):
    subject=models.ForeignKey(TSsubject,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,validators=[validate_capitalized])
    address=models.TextField()
    gender=models.TextField()
    age=models.IntegerField()
    mobile=models.TextField()
    email=models.TextField()
    image=models.ImageField(upload_to='image/',null=True)
    
    
    def __str__(self):
        return self.subject.subject
    def __str__(self):
        return self.user.username
    
class TSstudent(models.Model):
    classes=models.ForeignKey(TSclass,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,validators=[validate_capitalized])
    sid=models.TextField()
    subjects=models.TextField()
    address=models.TextField()
    gender=models.TextField()
    age=models.IntegerField()
    mobile=models.TextField()
    email=models.TextField()
    image=models.ImageField(upload_to='image/',null=True)
    
    def __str__(self):
        return self.sid
    def __str__(self):
        return self.classes.classes
    def __str__(self):
        return self.user.username




class Atndns(models.Model):
    sid=models.ForeignKey(TSstudent,on_delete=models.CASCADE,null=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date=models.DateField()
    atndns=models.TextField()

    
    def __str__(self):
        return self.sid.sid

    def __str__(self):
        return self.username.username

    
class fee(models.Model):
    sid=models.ForeignKey(TSstudent,on_delete=models.CASCADE,null=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date=models.DateField()
    amount=models.IntegerField()
    paid=models.TextField()

    
    def __str__(self):
        return self.sid.sid

    def __str__(self):
        return self.username.username

class lv(models.Model):
    sid=models.ForeignKey(TSstudent,on_delete=models.CASCADE,null=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    f_date=models.DateField()
    T_date=models.DateField()
    reason=models.TextField()
    status=models.IntegerField(default=False,null=True)
    def __str__(self):
        return self.sid.sid

    def __str__(self):
        return self.username.username

class lvs(models.Model):
    sid=models.ForeignKey(TSstudent,on_delete=models.CASCADE,null=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    f_date=models.DateField()
    T_date=models.DateField()
    status=models.TextField()

    def __str__(self):
        return self.sid.sid

    def __str__(self):
        return self.username.username
class axept(models.Model):
    sid=models.ForeignKey(lv,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.sid.sid

    def __str__(self):
        return self.user.username

  
class rjt(models.Model):
    sid=models.ForeignKey(lv,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.sid.sid.sid

    def __str__(self):
        return self.user.username


class results(models.Model):
    sid=models.ForeignKey(TSstudent,on_delete=models.CASCADE,null=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    classes=models.ForeignKey(TSclass,on_delete=models.CASCADE,null=True)
    exam=models.TextField()
    mal=models.IntegerField()
    hid=models.IntegerField()
    es=models.IntegerField()
    ms=models.IntegerField()
    ps=models.IntegerField()
    cmy=models.IntegerField()
    bgy=models.IntegerField()
    ss=models.IntegerField()
    inft=models.IntegerField()

    
    def __str__(self):
        return self.sid.sid

    def __str__(self):
        return self.username.username

    def __str__(self):
        return self.classes.classes


class task(models.Model):
    sid=models.ForeignKey(TSstudent,on_delete=models.CASCADE,null=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    subject=models.TextField()
    taske=models.TextField()
    s_date=models.DateField()
    e_date=models.DateField()

    def __str__(self):
        return self.sid.sid

    def __str__(self):
        return self.username.username


class ctask(models.Model):
    sid=models.ForeignKey(task,on_delete=models.CASCADE)
    username=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    subject=models.TextField()
    taske=models.TextField()
    s_date=models.TextField()
    e_date=models.TextField()
    attachment = models.FileField(upload_to='files/', null=True)
    pgrs=models.IntegerField(null=True, default='', blank=True)
    
    def __str__(self):
        return self.sid.sid.sid

    def __str__(self):
        return self.username.username
 