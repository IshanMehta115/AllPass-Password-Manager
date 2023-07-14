from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
import random
from cryptography.fernet import Fernet
import hashlib
from .models import Password



msg_page_data = None
global_code = None
otp_purpose = None
new_user_data = None
search_text = ""
fernet = Fernet(settings.KEY)

def new_page_view(request):
    return render(request, 'msg.html',msg_page_data)

def home(request):
    global global_code, new_user_data, msg_page_data, otp_purpose, search_text
    if request.method == "POST":
        if "signup_post" in request.POST:
            user_name = request.POST.get("username")
            email = request.POST.get("email")
            pswd = request.POST.get("password")
            pswd2 = request.POST.get("password2")
            #if passwords are not same
            if pswd != pswd2:
                msg = "Your passwords are not matching!"
                msg_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("msg.html")

                
            #if username exists
            elif User.objects.filter(username=user_name).exists():
                msg = "This username already exists!"
                msg_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("msg.html")
            

            #if email exists
            elif User.objects.filter(email=email).exists():
                msg = "This email already exists!"
                msg_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("msg.html")
            

            else:
                new_user_data = [user_name, email, pswd]
                # otp = str(random.randint(100000, 999999))
                otp = str(1234)
                global_code = otp
                otp_purpose = "signup"
                send_mail(
                    "AllPass Password Manager: Confirm Email",
                    f"Your otp for email verification is {otp}.",
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                return render(request, "home.html", {
                    "otp":True,
                })
            
            
        elif "otp_post" in request.POST:
            input_otp = request.POST.get("code")
            if input_otp != global_code:
                msg = f"{input_otp} is wrong!"
                msg_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("msg.html")
            
            else:
                if(otp_purpose=="signup"):
                    User.objects.create_user(new_user_data[0], new_user_data[1], new_user_data[2])
                    new_user = authenticate(request, username=new_user_data[0], password=new_user_data[2])
                    if not new_user==None:
                        login(request, new_user)
                        msg = f"{new_user_data[0]}. Thanks for registering."
                        msg_page_data = {
                            "text":msg, 
                            "code":True, 
                        }
                    return HttpResponseRedirect("msg.html")
                
                elif(otp_purpose=="login"):
                    login(request, User.objects.get(username=new_user_data))
                    msg = f"{request.user} welcome back."
                    msg_page_data = {
                            "text":msg, 
                            "code":True, 
                        }
                    return HttpResponseRedirect("msg.html")
                
                elif(otp_purpose=="password_reset"):
                    return render(request, "home.html", {
                    "change_password":True, 
                    "email":new_user_data,
                })

                elif(otp_purpose=="account_delete"):
                    user = request.user
                    user.delete()
                    logout(request)
                    msg = "Account deleted successfully."
                    msg_page_data = {
                            "text":msg, 
                            "code":True, 
                        }
                return HttpResponseRedirect("msg.html")



        elif 'login_post' in request.POST:
            user_name = request.POST.get("username")
            pswd = request.POST.get("password")
            new_user = authenticate(request, username=user_name, password=pswd)
            new_user_data = user_name
            if new_user is None:
                msg = "Login failed! Invalid login credentials."
                msg_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("msg.html")
                # print_and_exit(request, msg,"error")
            else:
                # otp = str(random.randint(100000, 999999))
                otp = str(1234)
                global_code = otp
                otp_purpose = "login"
                send_mail(
                    "AllPass Password Manager: Confirm Login",
                    f"Your otp for login verification is {otp}.",
                    settings.EMAIL_HOST_USER,
                    [new_user.email],
                    fail_silently=False,
                )
                return render(request, "home.html", {
                    "otp":True,
                })
        
        elif "logout_post" in request.POST:
            logout(request)
            msg = "Logged Out."
            msg_page_data = {
                    "text":msg, 
                    "code":True, 
                }
            return HttpResponseRedirect("msg.html")

        elif 'password_reset_post' in request.POST:
            email = request.POST.get("email")
            new_user_data = email
            if not User.objects.filter(email=email).exists():
                msg = "Email not registered. Sign Up to register."
                msg_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("msg.html")
            
            else:
                # otp = str(random.randint(100000, 999999))
                otp = str(1234)
                global_code = otp
                otp_purpose = "password_reset"
                send_mail(
                    "AllPass Password Manager: Passsword Reset",
                    f"Your otp for password reset verification is {otp}.",
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )
                return render(request, "home.html", {
                    "otp":True,
                })
            
        elif "change_password_post" in request.POST:
            # user_name = request.POST.get("user")
            pswd = request.POST.get("password")
            pswd2 = request.POST.get("password2")
            #if password are not identical
            if pswd != pswd2:
                msg = "Your passwords are not matching!"
                msg_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("msg.html")
            
            else:
                user = User.objects.get(email=new_user_data)
                user.set_password(pswd)
                user.save()
                if not user==None:
                    login(request, user)
                    msg = f"{user.username}. Password reset successfully."
                    msg_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
                return HttpResponseRedirect("msg.html")
            
        elif "add_password_post" in request.POST:
            application_name = request.POST.get("application_name")
            email = request.POST.get("email")
            pswd = request.POST.get("password")
            #ecrypt data
            encrypted_email = fernet.encrypt(email.encode())
            encrypted_password = fernet.encrypt(pswd.encode())

            application_name = application_name.strip()
            application_name = application_name.lower()
            temp = application_name.split()
            name = ' '.join(temp).capitalize()
            icon = '_'.join(temp)
            hash_val = hashlib.sha256((str(request.user) + email + application_name).encode()).hexdigest()
            if Password.objects.filter(val=hash_val).exists():
                msg_page_data = {
                        "text":"Entry already exists.", 
                        "code":True, 
                    }
                return HttpResponseRedirect("msg.html")
            else:
                Password.objects.create(
                    user=request.user,
                    name=name,
                    logo=icon,
                    email=encrypted_email.decode(),
                    password=encrypted_password.decode(),
                    val  = hash_val
                )
                msg_page_data = {
                        "text":"Password added successfully", 
                        "code":True, 
                    }
                return HttpResponseRedirect("msg.html")
        
        elif "modify_password_post" in request.POST:
            application_name = request.POST.get("application_name")
            email = request.POST.get("email")
            pswd = request.POST.get("password")
            old_hash_val = request.POST.get("password-val")
            encrypted_email = fernet.encrypt(email.encode())
            encrypted_password = fernet.encrypt(pswd.encode())

            application_name = application_name.strip()
            application_name = application_name.lower()
            temp = application_name.split()
            name = ' '.join(temp).capitalize()
            icon = '_'.join(temp)

            hash_val = hashlib.sha256((str(request.user) + email + application_name).encode()).hexdigest()
            if Password.objects.filter(val=hash_val).exists():
                msg_page_data = {
                        "text":"Entry already exists.", 
                        "code":True, 
                    }
                return HttpResponseRedirect("msg.html")
            else:
                Password.objects.get(val=old_hash_val).delete()
                Password.objects.create(
                    user=request.user,
                    name=name,
                    logo=icon,
                    email=encrypted_email.decode(),
                    password=encrypted_password.decode(),
                    val  = hash_val
                )
                msg_page_data = {
                        "text":"Password modified successfully", 
                        "code":True, 
                    }
                return HttpResponseRedirect("msg.html")
            
        elif "delete_password_post" in request.POST:
            to_delete = request.POST.get("password-val")
            msg = "Password entry deleted!"
            Password.objects.get(val=to_delete).delete()
            msg_page_data = {
                        "text":msg, 
                        "code":True, 
                    }
            return HttpResponseRedirect("msg.html") 
        
        elif "search_post" in request.POST:
            search_text = request.POST.get("search_text")
        elif "show_all_post" in request.POST:
            search_text = ""


        elif 'delete_account_post' in request.POST:
            # otp = str(random.randint(100000, 999999))
            otp = str(1234)
            global_code = otp
            otp_purpose = "account_delete"
            send_mail(
                "AllPass Password Manager: Account Delete",
                f"Your otp for password account deletion is {otp}.",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return render(request, "home.html", {
                "otp":True,
            })

       
    
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
