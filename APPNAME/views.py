
from django.contrib.auth.models import User
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
import random
from django.core.mail import send_mail
from cryptography.fernet import Fernet
from mechanize import Browser
import favicon
from .models import Password
import hashlib
# from ratelimit.decorators import ratelimit




br = Browser()
br.set_handle_robots(False)
fernet = Fernet(settings.KEY)

def new_page_view(request):
    return render(request, 'success_page.html',success_page_data)


def print_and_exit(request, msg,verdict):
    if verdict=="success":
        messages.success(request, msg)
        return HttpResponseRedirect(request.path)
    else:
        messages.error(request, msg)
        return HttpResponseRedirect(request.path)
        
search_text = ""
success_page_data = None
new_user_data = None

# @ratelimit(key='user', rate='5/m', block=True)
def home(request):
    global search_text,global_code,success_page_data,new_user_data
    if request.method == "POST":
        if "signup_page" in request.POST:
            user_name = request.POST.get("username")
            email = request.POST.get("email")
            pswd = request.POST.get("password")
            pswd2 = request.POST.get("password2")
            #if password are not identical
            if pswd != pswd2:
                msg = "Your passwords are not matching !"
                success_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("success_page.html")

                
            #if username exists
            elif User.objects.filter(username=user_name).exists():
                msg = "This username already exists!"
                success_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("success_page.html")
                # print_and_exit(request, msg,"error")
            #if email exists
            elif User.objects.filter(email=email).exists():
                msg = "This email already exists!"
                success_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("success_page.html")
                # print_and_exit(request, msg,"error")
            else:
                new_user_data = [user_name, email, pswd]
                # user = User.objects.get(username=user_name)
                otp = str(random.randint(100000, 999999))
                global_code = otp
                send_mail(
                    "AllPass Password Manager: Passsword Reset",
                    f"Your otp for email verification is {otp}.",
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                return render(request, "home.html", {
                    "code4":True,
                })
                # User.objects.create_user(user_name, email, pswd)
                # new_user = authenticate(request, username=user_name, password=pswd2)
                # if not new_user==None:
                #     login(request, new_user)
                #     msg = f"{user_name}. Thanks for registering."
                #     print_and_exit(request, msg,"success")

        if "psr_page" in request.POST:
            user_name = request.POST.get("user")
            pswd = request.POST.get("password")
            pswd2 = request.POST.get("password2")
            #if password are not identical
            if pswd != pswd2:
                msg = "Your passwords are not matching !"
                success_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("success_page.html")
                # print_and_exit(request, msg,"error")
            else:
                user = User.objects.get(username=user_name)
                user.set_password(pswd)
                user.save()
                if not user==None:
                    login(request, user)
                    msg = f"{user_name}. Password reset successfully."
                    success_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("success_page.html")
                    # print_and_exit(request, msg,"success")

        elif "logout_page" in request.POST:
            # msg = f"{request.user}. This user logged out."
            logout(request)
            success_page_data = {
                        "text":"Logged Out", 
                        "code":True, 
                    }
            return HttpResponseRedirect("success_page.html")
            # print_and_exit(request, msg,"success")

        elif 'login_form_page' in request.POST:
            user_name = request.POST.get("username")
            pswd = request.POST.get("password")
            new_user = authenticate(request, username=user_name, password=pswd)
            if new_user is None:
                msg = "Login failed! Invalid login credentials"
                success_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("success_page.html")
                # print_and_exit(request, msg,"error")
            else:
                otp = str(random.randint(100000, 999999))
                global_code = otp
                send_mail(
                    "AllPass Password Manager: confirm email",
                    f"Your otp for login verification is {otp}.",
                    settings.EMAIL_HOST_USER,
                    [new_user.email],
                    fail_silently=False,
                )
                return render(request, "home.html", {
                    "code":otp, 
                    "user":new_user,
                })
            
        elif 'pswd_reset_username_entry' in request.POST:
            user_name = request.POST.get("username")
            if not User.objects.filter(username=user_name).exists():
                msg = "Username does not exist"
                success_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("success_page.html")
                # print_and_exit(request, msg,"error")
            else:
                user = User.objects.get(username=user_name)
                otp = str(random.randint(100000, 999999))
                global_code = otp
                send_mail(
                    "AllPass Password Manager: Passsword Reset",
                    f"Your otp for password reset verification is {otp}.",
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )
                return render(request, "home.html", {
                    "code2":True,
                    "user":user,
                })
            
        elif "confirm_button" in request.POST:
            input_otp = request.POST.get("code")
            user = request.POST.get("user")
            if input_otp != global_code:
                msg = f"{input_otp} is wrong!"
                success_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("success_page.html")
                # print_and_exit(request, msg,"error")
            else:
                login(request, User.objects.get(username=user))
                msg = f"{request.user} welcome back."
                success_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("success_page.html")
                # print_and_exit(request, msg,"success")

        elif "new_user_otp" in request.POST:
            input_otp = request.POST.get("code")
            if input_otp != global_code:
                msg = f"{input_otp} is wrong!"
                success_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("success_page.html")
                # print_and_exit(request, msg,"error")
            else:
                User.objects.create_user(new_user_data[0], new_user_data[1], new_user_data[2])
                new_user = authenticate(request, username=new_user_data[0], password=new_user_data[2])
                if not new_user==None:
                    login(request, new_user)
                    msg = f"{new_user_data[0]}. Thanks for registering."
                    success_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("success_page.html")
                    # print_and_exit(request, msg,"success")

                

        elif "pswd-reset-otp-entry" in request.POST:
            input_otp = request.POST.get("code")
            user = request.POST.get("user")
            print("user pswd-reset-otp-entry = ",user)
            if input_otp != global_code:
                msg = f"{input_otp} is wrong!"
                success_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("success_page.html")
                # print_and_exit(request, msg,"error")
            else:
                return render(request, "home.html", {
                    "code3":True, 
                    "user":user,
                })


        elif "search_button" in request.POST:
            search_text = request.POST.get("search_text")

        elif "show_all_btn" in request.POST:
            search_text = ""
        
        elif "add_password_page" in request.POST:
            url = request.POST.get("url")
            email = request.POST.get("email")
            pswd = request.POST.get("password")
            #ecrypt data
            encrypted_email = fernet.encrypt(email.encode())
            encrypted_password = fernet.encrypt(pswd.encode())
            #get title of the website
            icon = "https://cdn-icons-png.flaticon.com/128/1006/1006771.png"
            # try:
            #     br.open(url)
            #     title = br.title()
            # except:
            #     title = url
            title = url
            #get the logo's URL
            try:
                icon = favicon.get(url)[0].url
            except:
                pass
            #Save data in database
            hash_val = hashlib.sha256((str(request.user) + email + url).encode()).hexdigest()
            if Password.objects.filter(val=hash_val).exists():
                success_page_data = {
                        "text":"Entry already exists.", 
                        "code":True, 
                    }
                return HttpResponseRedirect("success_page.html")
            else:
                new_password = Password.objects.create(
                    user=request.user,
                    name=title,
                    logo=icon,
                    email=encrypted_email.decode(),
                    password=encrypted_password.decode(),
                    val  = hash_val
                )
                success_page_data = {
                        "text":"Password added successfully", 
                        "code":True, 
                    }
                return HttpResponseRedirect("success_page.html")
            # print_and_exit(request, msg,"success")

        elif "delete_button" in request.POST:
            to_delete = request.POST.get("password-val")
            msg = f"{Password.objects.get(val=to_delete).name} deleted."
            Password.objects.get(val=to_delete).delete()
            success_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
            return HttpResponseRedirect("success_page.html")
        
        elif "modify_button" in request.POST:
            hash_val = request.POST.get("password-val")
            return render(request, "home.html", {
                    "code5":True,
                    "password_val":hash_val,
                })
        

        elif "modify_password_page" in request.POST:
            url = request.POST.get("url")
            email = request.POST.get("email")
            pswd = request.POST.get("password")
            old_hash_val = request.POST.get("password-val")
            encrypted_email = fernet.encrypt(email.encode())
            encrypted_password = fernet.encrypt(pswd.encode())
            icon = "https://cdn-icons-png.flaticon.com/128/1006/1006771.png"
            title = url
            try:
                icon = favicon.get(url)[0].url
            except:
                pass
            hash_val = hashlib.sha256((str(request.user) + email + url).encode()).hexdigest()
            if Password.objects.filter(val=hash_val).exists():
                success_page_data = {
                        "text":"Entry already exists.", 
                        "code":True, 
                    }
                return HttpResponseRedirect("success_page.html")
            else:
                Password.objects.get(val=old_hash_val).delete()
                new_password = Password.objects.create(
                    user=request.user,
                    name=title,
                    logo=icon,
                    email=encrypted_email.decode(),
                    password=encrypted_password.decode(),
                    val  = hash_val
                )
                success_page_data = {
                        "text":"Password modified successfully", 
                        "code":True, 
                    }
                return HttpResponseRedirect("success_page.html")
            
            # return print_and_exit(request,msg,"error")
        
        # elif "back_button" in request.POST:
        #     print("ok works 1")

    context = {}
    if request.user.is_authenticated:
        if(search_text!=""):
            passwords = Password.objects.all().filter(user=request.user,name__icontains=search_text)
        else:
            passwords = Password.objects.all().filter(user=request.user) 
        for pswd in passwords:
            pswd.email = fernet.decrypt(pswd.email.encode()).decode()
            pswd.password = fernet.decrypt(pswd.password.encode()).decode()
        context = {
            "passwords":passwords,
            "search_text":search_text,
        }   

    return render(request, "home.html", context)

