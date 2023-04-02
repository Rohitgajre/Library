# exec(open(r'D:\Python_Course\b8_django\Library\firstapp\db_shell.py').read())

from django.contrib.auth.models import User

print(User.objects.all())    # to get the all user or supeeruser 

# User.objects.create_superuser(username='Rahul', password='python@123')  # for creating the superuser and use alway create_user if you not create using this then you will get password in database in readable mode
# from django.utils.crypto import get_random_string
# print(get_random_string(2))