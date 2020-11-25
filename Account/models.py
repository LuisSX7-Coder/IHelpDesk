from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from phone_field import PhoneNumber

# Create your models here.
class HelpDesk_AccountManager(BaseUserManager):
    def create_user(self, user_name, user_first_name, user_last_name, email, birthday, address, user_role, password=None):
        
        if not user_name:
            raise ValueError('User name must be written')

        if not user_first_name:
            raise ValueError('A name must be written')

        if not user_last_name:
            raise ValueError('A last name must be written')

        if not user_role:
            raise ValueError('A user role must be written')

        if not email:
            raise ValueError('An email must be written')

        if not birthday:
            raise ValueError('A birthday must be written')

        if not address:
            raise ValueError('An address must be written')

        user = self.model(
            user_name = user_name,
            user_first_name = user_first_name,
            user_last_name = user_last_name,
            user_role = user_role,
            email = self.normalize_email(email),
            birthday = birthday,
            address = address
        )

        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self, user_name, user_first_name, user_last_name, email, birthday, address, password):
        user = self.create_user(  
            user_name = user_name,
            user_first_name = user_first_name,
            user_last_name = user_last_name,
            email = self.normalize_email(email),
            birthday = birthday,
            address = address,
            password = password
        )

        user.user_role = 1
        user.is_admin = True
        user.is_active = True
        user.is_staff =  True
        user.save(using=self.db)

        return user



class Account(AbstractBaseUser):
    id_user = models.IntegerField(primary_key=True, unique=True)
    user_name = models.CharField(max_length=25, blank=False, null=False, unique=True)
    user_first_name = models.CharField(max_length=25, blank=False, null=False)
    user_last_name = models.CharField(max_length=25, blank=False, null=False)
    user_role = models.IntegerField()
    user_image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    email = models.EmailField(max_length=254, blank=False, null=False, unique=True)
    birthday = models.DateTimeField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    phone = PhoneNumber(txt=None)
    cellphone = PhoneNumber(txt=None)
    project = models.CharField(max_length=50, blank=True,null=True)
    team = models.CharField(max_length=50, blank=True,null=True)
    hours_worked = models.IntegerField(blank=True, null=True)
    salary_per_hour = models.IntegerField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = HelpDesk_AccountManager()

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['user_first_name', 'user_last_name', 'email', 'birthday', 'address', 'user_role']

    def __str__(self):
        return "User name: " + self.user_name + "; Name: " + self.user_first_name + " " + self.user_last_name + "  " + str(self.user_image)
    
    def has_perm(self, perm, obj = None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return self.is_admin

# class User(models.Model):
#     user_first_name = models.CharField(max_length=25, blank=False, null=False)
#     user_last_name = models.CharField(max_length=25, blank=False, null=False)
#     birth_day = models.DateTimeField(auto_now=False, auto_now_add=False)
#     address = models.CharField(max_length=50, blank=False, null=False)
#     phone = models.CharField(max_length=13, blank=False, null=False)
#     cellphone =models.CharField(max_length=13, blank=True, null=True)
#     project = models.CharField(max_length=50, blank=True,null=True)
#     team = models.CharField(max_length=50, blank=True,null=True)
#     task = models.CharField(max_length=100)
#     hours_worked = models.IntegerField(blank=False, null=False)
#     salary_per_hour = models.IntegerField(blank=False, null=False)