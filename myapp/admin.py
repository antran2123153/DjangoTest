from django.contrib import admin

from .models import Book, TypeBook, Account, Order, Comment, Cart, Author

admin.site.register(Book)
admin.site.register(TypeBook)
admin.site.register(Order)
admin.site.register(Account)
admin.site.register(Comment)
admin.site.register(Cart) 
admin.site.register(Author) 