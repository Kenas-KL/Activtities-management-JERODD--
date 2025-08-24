from operator import truediv

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

# Create your models here.


class MemberUserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError("Nom d'utilisateur membre obligatoire")
        username = self.model.normalize_username(username)
        user = self.model(
            username = username
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, username, password = None):
        user = self.create_user(username, password)

        user.id_admin = True
        user.is_staff = True

        user.save()

        return user

class MemberUser(AbstractBaseUser):
    username = models.CharField(max_length=255,blank=False, unique=True, verbose_name="nom utilisateur membre")
    is_staff = models.BooleanField(default=False)
    thumbnail = models.ImageField(blank=True, null=True)
    in_community=models.BooleanField(default=False)
    commission =models.CharField(max_length=255, blank=False, choices=[
        ("Partenariat","partenariat"),
        ("Personne","personne"),
        ("Prosperité","prosperité"),
        ("Planète","Planète"),
        ("paix","paix"),
    ])

    fonction = models.CharField(max_length=155, blank=False, choices=[
        ("Coodonateur","coodonateur"),
        ("Chef de commission","Chef de commission"),
        ("Chef adjoint commission","Chef adjoint commission"),
        ("Membre","Membre")
    ])

    object = MemberUserManager()
    USERNAME_FIELD = "username"

    def has_perm(self, perm, obj=None): return True

    def has_module_perms(self, app_label): return True

    class Meta:
        verbose_name = "Membre utilisateur"


class Activity(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name='Titre')
    thumbnail = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=False)
    begin = models.DateTimeField(verbose_name="Date debut", blank=False)
    end = models.DateTimeField(verbose_name="date final", blank=False)
    rapport = models.TextField (blank=True, null=True)
    done = models.BooleanField(default=False)
    member = models.ManyToManyField(MemberUser, blank=True, null=True)

    class Meta:
        verbose_name = "Activité"


class InfoOut(models.Model):
    reason = models.TextField(blank=False)
    member=models.ForeignKey(MemberUser, on_delete=models.CASCADE)
    done_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-pk']

