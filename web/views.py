from multiprocessing import context
from django.shortcuts import render, redirect
from datetime import datetime
from .forms import LoginForm
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.utils.html import strip_tags
from django.utils import timezone
from datetime import datetime
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import logging
logging.basicConfig(level = logging.INFO)
    
@login_required(login_url='/')
def index(request):
    context = dict()
    template = 'index.html'
    return render(request, template, context)


class UserLogin(LoginView):
     template = 'auth.html'
     form_class = LoginForm
     succes_url = reverse_lazy('index')

     def get_success_url(self) -> str:
         logging.info("Successful authorization, making redirect to Home page")
         return self.succes_url
     
     def form_invalid(self, form):
        logging.error("Invalid username or password")
        context = dict()
        context["auth"] = "Invalid username or password"
        context["form"] = LoginForm
        return self.render_to_response(context)


class UserLogOut(LogoutView):
     next_page = reverse_lazy('login_page')