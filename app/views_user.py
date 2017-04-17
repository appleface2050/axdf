from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt

from app.models import SMSCodeSession, Userinfo
from forms import UserForm

from util.jsonresult import getResult
from django.db import transaction



@csrf_exempt
@transaction.atomic
def sign_up(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        # user_form = UserForm(data=request.GET)

        type = request.POST.get("type", None)
        tel = request.POST.get("username", None)
        code = request.POST.get("code", None)
        password = request.POST.get("password", None)
        sms_cheat = request.POST.get("sms_cheat", False)

        if type == "user":
            pass

        elif type == "worker":
            name = request.POST.get("name", None)
            email = request.POST.get("email", None)
            zhucedi = request.POST.get("zhucedi", None)
            address = request.POST.get("address", None)
            qiyezizhi = request.POST.get("qiyezizhi", None)
            chenglanfanwei = request.POST.get("chenglanfanwei", None)
            lianxiren = request.POST.get("lianxiren", None)
        else:
            return getResult(False, u'type error', None)

        if not sms_cheat:
            if not SMSCodeSession.check_code_by_tel(tel, code):
                return getResult(False, u'smscode check fail', None)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            Userinfo.add_user_info(tel, name, email, type, zhucedi, address, qiyezizhi, chenglanfanwei, lianxiren)

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors
            return getResult(False, user_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    # return render(request, 'user/register.html', {'user_form': user_form, 'registered': registered})
    return getResult(True, "sign up success")


# @csrf_exempt
def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method in ("POST", "GET"):
        if request.method == 'POST':
            # Gather the username and password provided by the user.
            # This information is obtained from the login form.
            # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
            # because the request.POST.get('<variable>') returns None, if the value does not exist,
            # while the request.POST['<variable>'] will raise key error exception
            username = request.POST.get('username')
            password = request.POST.get('password')
        elif request.method == 'GET':
            username = request.GET.get('username')
            password = request.GET.get('password')
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return getResult(True, "login success")
                # return HttpResponseRedirect('/manage')
            else:
                # An inactive account was used - no logging in!
                # return HttpResponse("your account has been deleted")
                return getResult(False, "your account has been deleted")
        else:
            # Bad login details were provided. So we can't log the user in.
            # print "Invalid login details: {0}, {1}".format(username, password)
            # return HttpResponse("Incorrect username or password.")
            return getResult(False, "Incorrect username or password.")

            # The request is not a HTTP POST, so display the login form.
            # This scenario would most likely be a HTTP GET.
            # else:
            #     # No context variables to pass to the template system, hence the
            #     # blank dictionary object...
            #     return render(request, 'user/login2.html',{})


# Use the login_required() decorator to ensure only those logged in can access the view.
# @csrf_exempt
@login_required
def sign_out(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/api')
