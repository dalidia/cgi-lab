#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

import json
from templates import login_page, secret_page, after_login_incorrect
# import secret
import os
import secret
from http.cookies import SimpleCookie

# set up cgi form
s = cgi.FieldStorage()

# get data from login_page form fields
username = s.getfirst("username")
password = s.getfirst("password")

# set up cookie
cookie = SimpleCookie(os.environ["HTTP_COOKIE"])
cookie_username = None
cookie_password = None
if cookie.get("username"):
    cookie_username = cookie.get("username").value
if cookie.get("password"):
    cookie_password = cookie.get("password").value

is_cookie_ok = cookie_username == secret.username and cookie_password == secret.password
is_form_ok = username == secret.username and password == secret.password

print("Content-Type: text/html")

# if information in the cookie is correct, autofill that info!
if is_cookie_ok:
    username = cookie_username
    password = cookie_password
if is_form_ok:
    # set cookie if login info is correct
    print(f"Set-Cookie: username={username}")
    print(f"Set-Cookie: password={password}")

print()

if username == secret.username and password == secret.password:
    # set the cookie here
    print(secret_page(username, password))
elif not username and not password:
    print(login_page())
else:
    print(after_login_incorrect())