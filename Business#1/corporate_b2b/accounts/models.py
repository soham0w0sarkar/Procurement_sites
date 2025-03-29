from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=50)
    address = models.TextField()

class CustomUser(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    is_approver = models.BooleanField(default=False)
    
    # Add these to resolve the clash
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="customuser_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set",
        related_query_name="user",
    )