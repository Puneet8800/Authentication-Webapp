# Authentication Webapp

### Instructions to run

- Install python3. On MacOS:
```
brew install python3
```
- Run:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install django-searchable-encrypted-fields
$ sudo pip install django-throttle-requests
$ python manage.py migrate
$ python manage.py runserver
```

- Visit http://localhost:8000/register.

Security Measures:
1. Properly Handled the user sensitive information, Encrypting SSN of user by AES-256 encryption by using the third party library "django-searchable-encrypted-fields"

2. Authenticating user securely
3. Handling Credential management by hashing the password in database.
4. Rate limiting the request so that application can be prevented against (Brute Force and DDOS attacks) by using throttle library. If someone hit 50 request in 5 mins user will get a 403.
5. Implemented CSRF.
6. Sanitizing Input properly to prevent Injections Attacks.
7. Properly managing session.
