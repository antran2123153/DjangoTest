from django.db import models
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    description = models.TextField()


class AccountManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class TypeBook(models.Model):
    name = models.CharField(max_length=100, blank=True)


class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True)
    author = models.ForeignKey(Author ,on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    types = models.ForeignKey(TypeBook, on_delete=models.CASCADE)
    like = models.IntegerField()

    class Meta:
        ordering = ['created']


class Comment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book ,on_delete=models.CASCADE)
    description  = models.TextField()

    class Meta:
        ordering = ['created']


class Cart(models.Model):
    books = models.ManyToManyField(Book)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    total_price = models.IntegerField()


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    discount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=300)
    message = models.CharField(max_length=1000)

    class Meta:
        ordering = ['created']