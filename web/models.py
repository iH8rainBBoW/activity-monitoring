from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)


class UserInfo(BaseModel):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=22) #+7 (707) 147 - 07 - 05 is 22 symbols
    mail = models.CharField(max_length=50)
    role_id = models.IntegerField() #Id роли, 1 - переводчик, 2 - шеф-реадктор, 3 - менеджер
    chat_id = models.IntegerField(null = True) #Для сохранения Id чата в телеграме
    
    class Meta:
        db_table = 'user_info'


class Role(BaseModel):
    role_name = models.CharField(max_length=25, null=True)
    
    class Meta:
        db_table = 'role'