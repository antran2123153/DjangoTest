### Kích hoạt môi trường ảo

```
pip install virtualenv
virtualenv venv
./venv/Scripts/activate
```

### Tải các thư viện cần thiết

```
pip install django django-cors-headers djangorestframework_simplejwt pymysql djangorestframework
```

### Khởi tạo database

```
python manage.py makemigrations
python manage.py migrate
```

### Chạy app

```
python manage.py runserver
```
