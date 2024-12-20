from decouple import config
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .form import MyForm
import logging
from telegram import Bot

bot = Bot(token=config('TELEGRAM_BOT_TOKEN'))

class HomePageListView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = MyForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            bot.send_message(chat_id=config('CHAT_ID'), text=f"Yangi mijoz !\nIsm: {name}\nTelefon raqam: {phone_number}")
        return self.render_to_response({'form': form})