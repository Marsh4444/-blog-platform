from email.headerregistry import Group
from urllib import request
from django.shortcuts import render, redirect, get_object_or_404
from bloggss.models import Category, Blog
from .utils import user_in_group 
from .forms import RegisterForm
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login , logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .decorators import group_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import RoleRequest


# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Assign default role
            user_group = Group.objects.get(name="User")
            user.groups.add(user_group)

            messages.success(request, "Your account has been created successfully!")
            return redirect('login')
        
            
    else:
        form = RegisterForm()

    context = {
        'form' : form
    }

    return render(request, 'users/register.html', context)


# def login_view(request):

#     #handle post request
#     form = AuthenticationForm(request, data=request.POST or None)

#     if request.method == "POST":
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)

#             messages.success(request, "Login successful 🎉")

#             return redirect("home")
#         else:
#             messages.error(request, "Invalid username or password")
   
#2  
    # # #handle post request
    # if request.method == 'POST':
    #     form = AuthenticationForm(request, request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user = auth.authenticate(username=username, password=password)
    #         if user is not None:
    #             auth.login(request, user)
    #             return redirect('home')

    # # #handle get request
    # form = AuthenticationForm()
    # context = {
    #     'form': form
    # }
    # return render(request, 'users/login.html', context)

def login_view(request):
    # Handle POST request
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(request, "Login successful 🎉")

            # 🔥 ROLE-BASED REDIRECT
            if user.groups.filter(name="Manager").exists():
                return redirect("manager_dashboard")

            elif user.groups.filter(name="Editor").exists():
                return redirect("editor_dashboard")

            elif user.groups.filter(name="Author").exists():
                return redirect("author_dashboard")

            else:
                messages.error(request, "No role assigned. Request for Author access, or contact admin to start writing!")
                return redirect("home")  # fallback if no group

        else:
            messages.error(request, "Invalid username or password")

        

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)

def logout_view(request):
    # Log the user out
    auth_logout(request)

    # Add a success message
    messages.success(request, "You have successfully logged out.")

    # Redirect to home (or login page if you prefer)
    return redirect("home")

User = get_user_model()  # get the custom user model if you have one

@login_required
@group_required("Manager")# 1️⃣ Check if the user is in the Manager group redirect to home if not a manager
def manager_dashboard(request):

    # 2️⃣ Count total posts, categories, and users
    posts_count = Blog.objects.count()
    categories_count = Category.objects.count()
    users_count = User.objects.count()

    # 3️⃣ Prepare the context dictionary to pass to the template
    context = {
        "posts_count": posts_count,
        "categories_count": categories_count,
        "users_count": users_count,
    }

    # 4️⃣ Render the template with the context
    return render(request, "users/manager/dashboard.html", context)

@login_required
@group_required("Editor")
def editor_dashboard(request):
    return render(request, "users/editor/dashboard.html")


@login_required
@group_required("Author")
def author_dashboard(request):
    return render(request, "users/author/dashboard.html")


#role request view
@login_required
def request_author_role(request):

    # Check if user already has Author role
    if request.user.groups.filter(name="Author").exists():
        messages.info(request, "You are already an Author.")
        return redirect("author_dashboard")

    # Prevent duplicate pending requests
    existing_request = RoleRequest.objects.filter(
        user=request.user,
        status="Pending"
    ).exists()

    if existing_request:
        messages.warning(request, "You already have a pending request.")
        return redirect("home")

    # Create new request
    RoleRequest.objects.create(
        user=request.user,
        requested_role="Author"
    )

    messages.success(request, "Your request has been submitted and is pending approval.")
    return redirect("home")


#MAnager Views for handling role requests will be implemented in the manager dashboard view, 
# allowing them to approve or reject pending requests.
@login_required
@group_required("Manager")
def manage_role_requests(request):
    requests = RoleRequest.objects.filter(status="Pending").order_by("-created_at")
    return render(request, "users/dashboard/manage_role_requests.html", {"requests": requests})


@login_required
@group_required("Manager")
def approve_role_request(request, pk):

    role_request = get_object_or_404(RoleRequest, id=pk, status="Pending")

    user = role_request.user
    author_group = Group.objects.get(name="Author")

    # Remove old roles (User)
    user.groups.clear()

    # Assign Author role
    user.groups.add(author_group)

    # Mark request approved
    role_request.status = "Approved"
    role_request.save()

    # Mark request approved
    role_request.status = "Approved"
    role_request.save()

    # Add session flag to show message on next login
    request.session['role_assigned'] = True

    return redirect("manage_role_requests")


@login_required
@group_required("Manager")
def reject_role_request(request, pk):

    role_request = get_object_or_404(RoleRequest, id=pk, status="Pending")

    role_request.status = "Rejected"
    role_request.save()

    return redirect("manage_role_requests")